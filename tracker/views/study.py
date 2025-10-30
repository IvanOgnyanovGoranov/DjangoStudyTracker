from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Subject, StudyProgress


def start_studying(request, pk):
    """Shows the timer with the specific subject the user chose."""
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'study/timer.html', {
        'subject': subject,
    })


def add_study_time(request, subject_id):
    """Adds the time studied to the subject."""
    if request.method == "POST":
        minutes = int(request.POST.get('minutes', 0))
        subject = get_object_or_404(Subject, pk=subject_id)

        if minutes >= 1:
            study_session = StudyProgress.objects.create(
                subject=subject,
                time_studied=minutes
            )

            study_session.save()

        else:
            messages.error(request, "Please enter a valid number of minutes.")

    return redirect('start_studying', pk=subject_id)