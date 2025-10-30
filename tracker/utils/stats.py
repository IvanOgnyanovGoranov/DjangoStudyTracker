from typing import Dict, Tuple
from django.db.models import Sum
from django.db.models.functions import Coalesce, TruncDate
from django.utils import timezone

from tracker.models import StudyProgress, Subject


def minutes_to_hhmm(minutes: int) -> str:
    hours, mins = divmod(int(minutes), 60)

    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if mins > 0 or not parts:
        parts.append(f"{mins} minute{'s' if mins != 1 else ''}")

    return " and ".join(parts)


def calculate_total_minutes(subject: Subject) -> int:
    """Total minutes studied for a subject (sum)."""
    return StudyProgress.objects.filter(subject=subject).aggregate(
        total=Coalesce(Sum('time_studied'), 0)
    )['total']


def calculate_total_days_studied(subject: Subject) -> int:
    """Count of unique study days (distinct dates)."""
    return StudyProgress.objects.filter(subject=subject) \
        .annotate(study_date=TruncDate('studied_on')) \
        .values('study_date') \
        .distinct() \
        .count()


def calculate_total_days_since_started(subject: Subject) -> int:
    """Days since subject.created_at (inclusive)."""
    days = (timezone.now().date() - subject.created_at.date()).days + 1
    return max(days, 1)


def calculate_goal_reached(subject: Subject) -> Tuple[int, int]:
    """
    Returns (goal_reached_days, total_study_days).
    We aggregate StudyProgress per day and then count days meeting current subject.daily_goal.
    """
    daily_totals = list(
        StudyProgress.objects
        .filter(subject=subject)
        .annotate(study_date=TruncDate('studied_on'))
        .values('study_date')
        .annotate(total_minutes=Sum('time_studied'))
    )

    total_study_days = len(daily_totals)
    goal_reached_days = sum(1 for d in daily_totals if d['total_minutes'] >= subject.daily_goal)
    return goal_reached_days, total_study_days


def get_subject_summary(subject: Subject) -> Dict[str, object]:
    """
    Return a dict with numeric stats (raw minutes / counts). The view will format for display.
    Keys:
      total_minutes, total_days_studied, total_days_since_started,
      avg_minutes_per_study_day, avg_minutes_per_day_overall,
      study_frequency_percent, goal_reached_days, study_days_for_goal
    """
    total_minutes = calculate_total_minutes(subject)
    total_days_studied = calculate_total_days_studied(subject)
    total_days_since_started = calculate_total_days_since_started(subject)
    goal_reached_days, study_days_for_goal = calculate_goal_reached(subject)

    # averages: handle zero denominators
    if total_days_studied > 0:
        avg_minutes_per_study_day = total_minutes / total_days_studied
    else:
        avg_minutes_per_study_day = 0

    if total_days_since_started > 0:
        avg_minutes_per_day_overall = total_minutes / total_days_since_started
        study_frequency_percent = (total_days_studied / total_days_since_started) * 100
    else:
        avg_minutes_per_day_overall = 0
        study_frequency_percent = 0

    return {
        'total_minutes': int(total_minutes),
        'total_days_studied': int(total_days_studied),
        'total_days_since_started': int(total_days_since_started),
        'avg_minutes_per_study_day': float(avg_minutes_per_study_day),
        'avg_minutes_per_day_overall': float(avg_minutes_per_day_overall),
        'study_frequency_percent': float(study_frequency_percent),
        'goal_reached_days': int(goal_reached_days),
        'study_days_for_goal': int(study_days_for_goal),
    }
