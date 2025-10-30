from django.shortcuts import render, get_object_or_404
from tracker.models import Subject
from tracker.utils.stats import minutes_to_hhmm, get_subject_summary

def detailed_subject_stats(request, pk):
    """Detailed overview of the subject's stats."""
    subject = get_object_or_404(Subject, pk=pk)
    stats = get_subject_summary(subject)

    context = {
        'subject': subject,
        # hero
        'avg_time_per_study_day': minutes_to_hhmm(stats['avg_minutes_per_study_day']),
        'avg_time_per_day_overall': minutes_to_hhmm(stats['avg_minutes_per_day_overall']),
        # context
        'total_time': minutes_to_hhmm(stats['total_minutes']),
        'study_days': stats['total_days_studied'],
        'days_since_started': stats['total_days_since_started'],
        'study_frequency_percent': round(stats['study_frequency_percent'], 1),
        # goal
        'daily_goal': subject.daily_goal,
        'goal_reached_days': stats['goal_reached_days'],
        'study_days_for_goal': stats['study_days_for_goal'],
        'goal_success_rate_percent': round(
            (stats['goal_reached_days'] / stats['study_days_for_goal'] * 100) if stats['study_days_for_goal'] > 0 else 0,
            1
        ),
    }

    return render(request, 'stats/detailed_subject.html', context)




