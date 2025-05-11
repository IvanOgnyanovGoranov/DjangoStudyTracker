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
    time_studied = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        related_name="progress_records",
    )
