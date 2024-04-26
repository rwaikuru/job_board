"""
URL configuration for jobsboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import UserCreateView,JobCategoryListView,JobListView,JobDetailView, AboutView, UserUpdateView, UserDetailView, EmployerCreateView, EmployerUpdateView, EmployerDetailView, TestimonialView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('joblist/', JobListView.as_view(), name='joblist'),
    path('jobdetail/', JobDetailView.as_view(), name='jobdetail'),
    path('category/', JobCategoryListView.as_view(), name='category'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('employers/create/', EmployerCreateView.as_view(), name='employer_create'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer_detail'),
    path('employers/<int:pk>/update/', EmployerUpdateView.as_view(), name='employer_update'),
    path('testimonials/', TestimonialView.as_view(), name='testimonials'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
