from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q

DAILY_GOAL_MSG = "Daily goal must be at least 1 minute and not exceed 1080 minutes."
STUDY_TIME_MSG = "Time studied must be at least 1 minute."

class Subject(models.Model):
    """Represents a study subject created by a user, with a daily goal entered."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subjects",
    )
    name = models.CharField(
        max_length=50,
        unique=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    daily_goal = models.SmallIntegerField(
        validators=[
            MinValueValidator(1, message=DAILY_GOAL_MSG),
            MaxValueValidator(1080, message=DAILY_GOAL_MSG),
        ]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(daily_goal__lte=1080) & Q(daily_goal__gte=1),
                name='daily_goal_range'
            )
        ]
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class StudyProgress(models.Model):
    """Represents study session entered by the user."""
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        related_name="progress_records",
    )

    time_studied = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, message=STUDY_TIME_MSG)]
    )
    studied_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(time_studied__gte=1),
                name='studyprogress_time_studied_gte_1',
            )
        ]

    def __str__(self):
        return f"{self.subject.name}: {self.time_studied}m on {self.studied_on}"

class EditSubject(models.Model):
    """Represents an edit of the daily goal made by the user."""
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        related_name="edit_history",
    )

    edited_at = models.DateTimeField(
        auto_now_add=True
    )

    new_daily_goal = models.SmallIntegerField(
        validators=[
            MinValueValidator(1, message=DAILY_GOAL_MSG),
            MaxValueValidator(1080, message=DAILY_GOAL_MSG),
        ]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(new_daily_goal__lte=1080) & Q(new_daily_goal__gte=1),
                name='edit_subject_daily_goal_range'
            )
        ]

    def __str__(self):
        return f"Edit of {self.subject.name} @ {self.edited_at}: {self.new_daily_goal}"
