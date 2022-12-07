from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('education/',views.education_page,name='education'),
    path('workexperience/',views.work_experience_page,name='work experience'),
    path('projects/',views.projects_page,name='projects')
]