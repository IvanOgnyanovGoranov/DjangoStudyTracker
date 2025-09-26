from datetime import date

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Subject, StudyProgress
from django.urls import reverse
from django.template.loader import render_to_string


# to be changed to a message (no straight redirect)
def redirect_if_no_subject(request):
    """User clicks on Add to add a subject and is redirected to add_subject"""
    return HttpResponseRedirect(reverse('add_subject'))


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
                studied_on=date.today(),
                time_studied=minutes
            )

            study_session.save()

        else:
            messages.error(request, "Please enter a valid number of minutes.")

    return redirect('start_studying', pk=subject_id)


# def subject_redirect_by_number(request, subject_number):
#     """Redirects to respective subject when a number is entered in the URL"""
#     subjects_count = Subject.objects.count()
#     if not (1 <= subject_number <= subjects_count):
#         raise Http404('The number is out of range!')
#
#     url = reverse('show_timer', kwargs={'pk': subject_number})
#     return HttpResponseRedirect(url)