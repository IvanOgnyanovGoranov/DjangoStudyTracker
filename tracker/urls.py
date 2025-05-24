from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('manage_subjects', views.manage_subjects, name='manage_subjects'),
    path('show_timer', views.show_timer, name='show_timer'),
    path('view_stats', views.view_stats, name='view_stats'),
]