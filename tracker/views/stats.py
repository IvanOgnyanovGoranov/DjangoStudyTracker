from enum import unique

from django.db.models.aggregates import Sum
from django.db.models.functions import Coalesce, TruncDate
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone

from tracker.models import Subject, StudyProgress
from django.urls import reverse
from django.template.loader import render_to_string


# Subject Statistics – [Subject Name]

# Hero section (top, big & obvious)
    # Average time per study day: HH:MM
    # Average time per week (including rest days): HH:MM
# Context section
    # Total time studied: HH:MM
    # Study days: X days
    # Average study days per week: X.X days/week
    # Current streak: N days
# Goal section (motivational)
    # Daily goal: N minutes (last updated on date)
    # Goal reached: X times / Y study days — Z% success rate

def detailed_subject_stats(request, pk):
    subject = Subject.objects.get(pk=pk)
    total_days_since_started = (timezone.now().date() - subject.created_at.date()).days + 1


    return HttpResponse(f"Here will be a detailed overview for {subject.name}")




