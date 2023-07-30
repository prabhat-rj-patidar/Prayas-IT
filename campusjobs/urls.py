"""campusjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from job.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('adminLogin', adminLogin, name='adminLogin'),
    path('userLogin', userLogin, name='userLogin'),
    path('recruiterLogin', recruiterLogin, name='recruiterLogin'),
    path('userSignup', userSignup, name='userSignup'),
    path('userHome', userHome, name='userHome'),
    path('logoutUser', logoutUser, name='logoutUser'),
    path('recruiterSignup', recruiterSignup, name='recruiterSignup'),
    path('recruiterHome', recruiterHome, name='recruiterHome'),
    path('adminHome', adminHome, name='adminHome'),
    path('viewUsers', viewUsers, name='viewUsers'),
    path('deleteUser/<int:pid>', deleteUser, name='deleteUser'),
    path('recruiterPending', recruiterPending, name='recruiterPending'),
    path('changeStatus/<int:pid>', changeStatus, name='changeStatus'),
    path('viewRecruiters', viewRecruiters, name='viewRecruiters'),
    path('deleteRecruiter/<int:pid>', deleteRecruiter, name='deleteRecruiter'),
    path('changePwdAdmin', changePwdAdmin, name='changePwdAdmin'),
    path('logoutAdmin', logoutAdmin, name='logoutAdmin'),
    path('changePwdUser', changePwdUser, name='changePwdUser'),
    path('logoutRecruiter', logoutRecruiter, name='logoutRecruiter'),
    path('changePwdRecruiter', changePwdRecruiter, name='changePwdRecruiter'),
    path('jobPosting', jobPosting, name='jobPosting'),
    path('jobList', jobList, name='jobList'),
    path('editJob/<int:pid>', editJob, name='editJob'),
    path('jobsList', jobsList, name='jobsList'),
    path('userJobList', userJobList, name='userJobList'),
    path('description/<int:pid>', description, name='description'),
    path('deleteJob/<int:pid>', deleteJob, name='deleteJob'),
    path('contactUs', contactUs, name='contactUs'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
