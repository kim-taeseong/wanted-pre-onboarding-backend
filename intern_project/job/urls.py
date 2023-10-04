from django.urls import path

from . import views
urlpatterns = [
    path('job/', views.job, name='job'),
    path('job/<int:id>/', views.job_id, name='job_id'),
    path('cookie/', views.csrf_cookie, name='csrf_cookie'),
]