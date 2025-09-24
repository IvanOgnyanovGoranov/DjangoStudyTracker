from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q


# Create your models here.


class Subject(models.Model):
    name = models.CharField(
        max_length=100
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    daily_goal = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1080)
        ]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(daily_goal__lte=1080) & Q(daily_goal__gte=1),
                name='daily_goal_range'
            )
        ]


class StudyProgress(models.Model):
    time_studied = models.PositiveIntegerField()
    date = models.DateField(
        auto_now_add=True
    )
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        related_name="progress_records",
    )
