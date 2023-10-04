from django.urls import path

from . import views
urlpatterns = [
    path('job/', views.create_job, name='create_job'),
    path('job/<int:id>/', views.update_job, name='update_job'),
    path('cookie/', views.csrf_cookie, name='csrf_cookie'),
]