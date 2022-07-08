from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('skill-list/', views.showAllSkills, name='skill-list'),
    path('candidate-list/', views.showAllCandidates, name='candidate-list'),
    path('job-list/', views.showAllJobs, name='job-list'),
    path('best-candidate-list/<int:jobId>', views.showBestCandidates, name='best-candidate-list')
]