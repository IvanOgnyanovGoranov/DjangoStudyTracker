from django.urls import path
from . import views
from .views import home, subjects, study, stats

urlpatterns = [
    path('', views.home.home_page, name='home_page'),
    path('manage_subjects/', views.subjects.manage_subjects, name='manage_subjects'),
    path('start_studying/', views.study.start_studying, name='start_studying'),
    path('start_studying/timer/', views.study.show_timer, name='show_timer'),
    path('view_stats/', views.stats.view_stats, name='view_stats'),
    path('<int:home_page>/', views.home.home_page_redirecting_numbers, name='home_page_redirecting_numbers'),
]