from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Employer

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role', 'profile_picture', 'cv', 'location', 'summary', 'employer',
                  'physical_address', 'postal_address', 'postal_code', 'po_box', 'telephone', 'alternate_email',
                  'linkedin_url')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'role', 'profile_picture', 'cv', 'location', 'summary', 'employer',
                  'physical_address', 'postal_address', 'postal_code', 'po_box', 'telephone', 'alternate_email',
                  'linkedin_url')

class EmployerCreationForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('user', 'company_name', 'industry', 'website', 'company_size', 'location', 'company_logo',
                  'description', 'contact_person')

class EmployerChangeForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('user', 'company_name', 'industry', 'website', 'company_size', 'location', 'company_logo',
                  'description', 'contact_person')
