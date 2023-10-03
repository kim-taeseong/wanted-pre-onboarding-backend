from django.urls import path

from . import views
urlpatterns = [
    path('job/', views.job, name='job'),
    path('cookie/', views.csrf_cookie, name='csrf_cookie'),
]