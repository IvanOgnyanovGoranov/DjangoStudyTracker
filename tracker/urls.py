from django.urls import path
from . import views
from .views import home, subjects, study, stats
from .views.subjects import add_subject, edit_or_delete_subject, redirect_to_view_stats

urlpatterns = [
    path('', views.home.home_page, name='home_page'),
    path('manage_subjects/', views.subjects.manage_subjects, name='manage_subjects'),
    path('manage_subjects/add-subject/', views.subjects.add_subject, name='add_subject'),
    path('manage_subjects/add-subject/subject-exists/', views.subjects.subject_exists, name='subject_exists'),
    path('manage_subjects/<int:pk>/edit-or-delete/', views.subjects.edit_or_delete_subject, name='edit_or_delete_subject'),
    path('manage_subjects/redirect-to-view-stats/', views.subjects.redirect_to_view_stats, name='redirect_to_view_stats'),
    path('start_studying/', views.study.start_studying, name='start_studying'),
    path('start_studying/redirect-if-no-subject', views.study.redirect_if_no_subject, name='redirect_if_no_subject'),
    path('start_studying/<int:subject_number>', views.study.subject_redirect_by_number, name='subject_redirect_by_number'),
    path('start_studying/timer/<int:pk>/', views.study.show_timer, name='show_timer'),
    path('start_studying/timer/<int:subject_id>/add-study-time/', views.study.add_study_time, name='add_study_time'),
    path('view_stats/', views.stats.view_stats, name='view_stats'),
    path('view_stats/<int:pk>/', views.stats.specific_subject_stats, name='specific_subject_stats'),
]