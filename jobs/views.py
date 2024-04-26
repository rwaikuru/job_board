from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, ListView
from .models import User, Employer, JobCategory, Job
from .forms import CustomUserCreationForm, CustomUserChangeForm, EmployerCreationForm, EmployerChangeForm

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')  # You need to define this URL in your urls.py

class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')  # Redirect after update, adjust as necessary

class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

class EmployerCreateView(CreateView):
    model = Employer
    form_class = EmployerCreationForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer_list')  # Define this URL in your urls.py

class EmployerUpdateView(UpdateView):
    model = Employer
    form_class = EmployerChangeForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer_list')  # Redirect after update, adjust as necessary

class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'employers/employer_detail.html'
    context_object_name = 'employer'

class JobCategoryListView(ListView):
    model = JobCategory
    template_name = 'category.html'
    context_object_name = 'job_categories'

class JobListView(ListView):
    model = Job
    template_name = 'joblist.html'
    context_object_name = 'jobs'
    select_related = ('employer',)

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'

class HomeView(ListView):
    model = JobCategory
    template_name = 'index.html'
    context_object_name = 'categories'  # Updated for categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().select_related('employer')  # Fetch jobs
        return context

# class HomeView(ListView):
#     model = Job
#     template_name = 'index.html'
#     context_object_name = 'jobs'
    
#     def get_queryset(self):
#         category_name = self.kwargs.get('category_name')
#         return Job.objects.filter(category__category_name=category_name).select_related('employer')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_name'] = self.kwargs.get('category_name')
#         return context

class AboutView(TemplateView):
    template_name = 'about.html'

# class JobListView(TemplateView):
#     template_name = 'joblist.html'

class JobDetailView(TemplateView):
    template_name = 'jobdetail.html'

# class JobCategoryView(TemplateView):
#     template_name = 'category.html'
