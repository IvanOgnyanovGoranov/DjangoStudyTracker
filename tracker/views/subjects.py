from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Subject, StudyProgress
from django.contrib import messages
from tracker.forms import EditSubjectForm, AddSubjectForm
from django.views import View


def my_subjects(request):
    """Render all subjects belonging to the logged-in user."""
    subjects = Subject.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_subjects.html', {'subjects': subjects})


class ManageSubjectView(View):
    """View for displaying, editing, and deleting a user's subject."""

    def get_subject_and_progress(self, pk, user):
        """Return a subject (owned by user) and its total studied minutes."""
        subject = get_object_or_404(Subject, pk=pk, user=user)
        subject_progress = StudyProgress.objects.filter(subject_id=subject.id).aggregate(
            total_minutes=Coalesce(Sum('time_studied'), Value(0))
        )
        return subject, subject_progress['total_minutes']

    def get(self, request, pk):
        """Render the subject info page with progress and edit form."""
        subject, progress = self.get_subject_and_progress(pk, request.user)
        form = EditSubjectForm()
        return render(request, 'manage_subjects/subject_info.html', {
            'subject': subject,
            'progress': progress,
            'form': form
        })

    def post(self, request, pk):
        """Handle edit or delete actions for a subject."""
        subject, progress = self.get_subject_and_progress(pk, request.user)
        action = request.POST.get('action')

        if action == 'edit_goal':
            form = EditSubjectForm(request.POST)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.subject = subject
                edit.save()

                subject.daily_goal = form.cleaned_data['new_daily_goal']
                subject.save()
                messages.success(request, "Daily goal updated successfully!")
                return redirect('my_subjects')
            else:
                return render(request, 'manage_subjects/subject_info.html', {
                    'subject': subject,
                    'progress': progress,
                    'form': form
                })

        elif action == 'delete_subject':
            subject.delete()
            messages.success(request, "Subject deleted successfully!")
            return redirect('my_subjects')


class AddSubjectView(View):
    """User adds a new subject."""

    def get(self, request):
        form = AddSubjectForm()
        return render(request, 'add_subject.html', {'form': form})

    def post(self, request):
        form = AddSubjectForm(request.POST, user=request.user)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()  # Let model validation handle duplicates
            messages.success(request, "Subject added successfully!")
            return redirect('my_subjects')

        return render(request, 'add_subject.html', {'form': form})
