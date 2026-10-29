from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('settings/', views.settings_view, name='settings'),
]