from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(
        max_length=100
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    daily_goal = models.PositiveIntegerField(
        default=0
    )


class StudyProgress(models.Model):
    time_studied_today = models.PositiveIntegerField()
    total_time_studied = models.PositiveIntegerField()
    total_days_studied = models.PositiveIntegerField()
    last_entry_date = models.DateTimeField()
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        related_name="progress_records",
    )
