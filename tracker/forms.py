from django import forms

from tracker.models import Subject, EditSubject


class EditSubjectForm(forms.ModelForm):
    class Meta:
        model = EditSubject
        fields = ['new_daily_goal']


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'daily_goal']
        labels = {
            'name': 'Subject Name',
        }
