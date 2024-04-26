from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import datetime
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('applicant', 'Applicant'),
        ('employer', 'Employer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='applicant')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    cv = models.FileField(upload_to='resumes/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    employer = models.ForeignKey('Employer', related_name='employees', on_delete=models.SET_NULL, null=True, blank=True)
    # Contact Information Fields
    physical_address = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    po_box = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    alternate_email = models.EmailField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True)
    company_size = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    description = models.TextField()
    contact_person = models.ForeignKey('User', related_name='managing_companies', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("company_name", kwargs={"company_name": self.company_name})
    
    def __str__(self):
     return self.company_name



class JobCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
     return self.category_name
    

def default_application_deadline():
    return timezone.now() + datetime.timedelta(days=30)

class Job(models.Model):

    JOB_TYPE_CHOICES = [
    ('FT', 'Full-Time'),
    ('PT', 'Part-Time'),
    ('CT', 'Contract'),
    ('TP', 'Temporary'),
    ('IN', 'Internship'),
]
    employer = models.ForeignKey('Employer', on_delete=models.CASCADE)  # Assuming Employer is another model
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.ForeignKey('JobCategory', on_delete=models.SET_NULL, null=True)  # Assuming JobCategory is another model
    type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
  # Consider using choices for predefined types
    description = models.TextField()
    requirements = models.TextField()
    salary_range = models.PositiveIntegerField()
    posted_date = models.DateField(auto_now_add=True)
    application_deadline = models.DateField(default=default_application_deadline)
    interested_users = models.ManyToManyField('User', related_name='interested_jobs', blank=True)

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"


class Application(models.Model):

    STATUS_CHOICES = (
    ('pending', 'Pending'),  # Application has been submitted but not reviewed yet
    ('reviewed', 'Reviewed'),  # Application has been reviewed by the employer
    ('interviewing', 'Interviewing'),  # Applicant is in the interview process
    ('offer_made', 'Offer Made'),  # Employer has made an offer to the applicant
    ('rejected', 'Rejected'),  # Application has been rejected
    ('hired', 'Hired'),  # Applicant has been hired for the job
    # Add more status choices as needed
)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)  # Consider using choices for status

    def __str__(self):
     return f"Application by {self.user.username} for {self.job.title}"
    
def hire_applicant(self, user):
    # Method to set a user as an employee of the job's employer when hired
    if self.status == 'hired':
        user.employer = self.job.employer
        user.save()

Application.hire_applicant = hire_applicant 
 

class Skill(models.Model):
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name


class UserSkill(models.Model):

    PROFICIENCY_CHOICES = (
    (1, 'Beginner'),   # Basic understanding or introductory level
    (2, 'Intermediate'),  # Moderate level of skill and understanding
    (3, 'Advanced'),  # High level of skill and expertise
    (4, 'Expert')   # Mastery level
    # Add more proficiency levels as needed
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.IntegerField(choices=PROFICIENCY_CHOICES)  # Consider defining the scale

    def __str__(self):
     return f"{self.user.username} - {self.skill.skill_name}"


class JobSkill(models.Model):

    IMPORTANCE_CHOICES = (
    (1, 'Low'),    # Skill is of low importance for the job
    (2, 'Moderate'),  # Skill is moderately important for the job
    (3, 'High'),   # Skill is highly important for the job
    (4, 'Critical')  # Skill is critical or essential for the job
    # Add more importance levels as needed
)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    importance_level = models.IntegerField(choices=IMPORTANCE_CHOICES)  # Consider defining the scale

    def __str__(self):
     return f"{self.job.title} - {self.skill.skill_name}"


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"From {self.sender.username} to {self.receiver.username}"


class Notification(models.Model):
    NOTIFICATION_CHOICES = (
    ('general', 'General'),  # General notification
    ('reminder', 'Reminder'),  # Reminder notification
    ('announcement', 'Announcement'),  # Announcement notification
    ('update', 'Update'),  # Update notification
    # Add more notification types as needed
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=255, choices=NOTIFICATION_CHOICES)  # Consider using choices
    notification_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"Notification for {self.user.username}"
