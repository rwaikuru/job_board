from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .models import User, Employer, JobCategory, JobSkill,Job,Application,Skill, UserSkill, Message,Notification

admin.site.register(User, UserAdmin)
admin.site.register(Employer)
admin.site.register(JobCategory)
admin.site.register(JobSkill)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Message)
admin.site.register(Notification)