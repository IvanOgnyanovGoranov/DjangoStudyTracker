from django.urls import path
from . import views


urlpatterns = [
    path("timer", views.show_timer),
    path('progress', views.show_progress),
]