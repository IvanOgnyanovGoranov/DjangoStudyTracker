from django.contrib import messages
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Subject, StudyProgress
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib import messages
from tracker.forms import EditSubject, AddSubject


def my_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'my_subjects.html', {'subjects': subjects})


def manage_subject(request, pk):
    """Shows subject info with the option to edit or delete it."""
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'edit_goal':
            form = EditSubject(request.POST)

            if form.is_valid():
                entered_goal = form.cleaned_data
                subject.daily_goal = entered_goal['new_daily_goal']
                subject.save()
                messages.success(request, "Daily goal updated successfully!")
        elif action == 'delete_subject':
            subject.delete()
            messages.success(request, "Subject deleted successfully!") # Not displayed because of the redirect.
            # Add a form in form.py instead of redirect
            return redirect('my_subjects')
    else:
        form = EditSubject()

    subject_progress = StudyProgress.objects.filter(subject_id=subject.id).aggregate(total_minutes=Coalesce(Sum('time_studied'), Value(0)))
    return render(request, 'manage_subjects/subject_info.html', {'subject': subject, 'progress': subject_progress['total_minutes'], 'form': form})


def add_subject(request):
    """User chooses what subject to add."""
    # Add pop up if user doesn't enter minutes
    if request.method == "POST":
        form = AddSubject(request.POST)

        if form.is_valid():
            entered_data = form.cleaned_data
 
            if not Subject.objects.filter(name__iexact=entered_data['subject_name']).exists():
                Subject.objects.create(name=entered_data['subject_name'], daily_goal=entered_data['daily_goal'])
                return redirect('my_subjects')
            else:
                return render(request, 'subject_exists.html', {
                    'subject_name': entered_data
                })
    else:
        form = AddSubject()

    return render(request, 'add_subject.html', {'form': form})


def subject_exists(request):
    return render(request, 'subject_exists.html')


def redirect_to_view_stats(request):
    """Redirects to the stats view."""
    return HttpResponseRedirect(reverse('view_stats'))