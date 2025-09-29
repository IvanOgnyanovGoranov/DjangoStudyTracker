from django.db.models import Sum
from django.db.models.functions import Coalesce, TruncDate

from tracker.models import StudyProgress


def minutes_to_hhmm(minutes: int) -> str:
    hours, mins = divmod(int(minutes), 60)
    return f"{hours:02d}:{mins:02d}"

def calculate_total_minutes(subject):
    total_minutes = StudyProgress.objects.filter(subject=subject).aggregate(
        total=Coalesce(Sum('time_studied'), 0)
    )['total']

    return total_minutes

def calculate_total_days_studied(subject):
    total_days_studied = StudyProgress.objects.filter(subject=subject) \
        .annotate(study_date=TruncDate('studied_on')) \
        .values('study_date') \
        .distinct() \
        .count()

    return total_days_studied

def get_avg_per_study_day(subject):
    total_minutes = calculate_total_minutes(subject)
    total_days_studied = calculate_total_days_studied(subject)

    avg_minutes_per_study_day = (
        total_minutes / total_days_studied if total_days_studied > 0 else 0
    )
    avg_per_study_day = minutes_to_hhmm(avg_minutes_per_study_day)

    return avg_per_study_day