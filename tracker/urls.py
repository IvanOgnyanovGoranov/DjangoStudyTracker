from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import home, subjects, study, stats, auth
from .views.auth import LogoutView, LoginView
from .views.subjects import ManageSubjectView, AddSubjectView

urlpatterns = [
    path('', login_required(home.home_page), name='home_page'),
    path('my-subjects/', login_required(subjects.my_subjects), name='my_subjects'),
    path('my-subjects/start-studying/<int:pk>/', login_required(views.study.start_studying), name='start_studying'),
    path('start_studying/timer/<int:subject_id>/add-study-time/', login_required(views.study.add_study_time), name='add_study_time'),
    path('my-subjects/manage/<int:pk>', login_required(ManageSubjectView.as_view()), name='manage_subject'),
    path('my-subjects/view_stats/<int:pk>/', login_required(views.stats.detailed_subject_stats), name='detailed_subject_stats'),
    path('add-subject/', login_required(AddSubjectView.as_view()), name='add_subject'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.auth.register_user, name='register'),
]