from django.urls import path
from . import views


urlpatterns = [
    path('', views.pick_subject),
    path('timer', views.show_timer),
    path('<int:subject_number>', views.subject_as_number),
    path('<str:subject>', views.show_subject_info, name='subject_info'),
]