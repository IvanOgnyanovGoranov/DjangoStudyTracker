from django.urls import path
from . import views
from .views import home, subjects, study, stats
from .views.subjects import redirect_to_view_stats

urlpatterns = [
    path('', views.home.home_page, name='home_page'),
    path('my-subjects/', views.subjects.my_subjects, name='my_subjects'),
    path('my-subjects/start-studying/<int:pk>/', views.study.start_studying, name='start_studying'),
    path('start_studying/timer/<int:subject_id>/add-study-time/', views.study.add_study_time, name='add_study_time'),

    path('my-subjects/manage/<int:pk>', views.subjects.ManageSubjectView.as_view(), name='manage_subject'),
    path('my-subjects/view_stats/<int:pk>/', views.stats.detailed_subject_stats, name='detailed_subject_stats'),

    path('add-subject/', views.subjects.AddSubjectView.as_view(), name='add_subject'),
    path('add-subject/subject-exists/', views.subjects.subject_exists, name='subject_exists'),
]