from enum import unique

from django.db.models.aggregates import Sum
from django.db.models.functions import Coalesce, TruncDate
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from tracker.models import Subject, StudyProgress
from django.urls import reverse
from django.template.loader import render_to_string

from tracker.utils.stats import calculate_total_days_since_started, calculate_total_days_studied, \
    calculate_total_minutes, minutes_to_hhmm, calculate_goal_reached, get_subject_summary


# Subject Statistics – [Subject Name]

# # Hero section
#     Average time per study day: HH:MM
#     Average time per day (including rest days): HH:MM
#
# # Context section
#     Total time studied: HH:MM
#     Study days: X days (out of Y total days since start)
#     Study frequency: Z% of days

# # Goal section
#     Daily goal: N minutes (last updated on date)
#     Goal reached: X times / Y study days — Z% success rate

def detailed_subject_stats(request, pk):
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




