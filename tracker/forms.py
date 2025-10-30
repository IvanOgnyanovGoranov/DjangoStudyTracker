from django import forms
from django.core.exceptions import ValidationError

from tracker.models import Subject, EditSubject


class EditSubjectForm(forms.ModelForm):
    """Form for editing the subject's daily goal"""
    class Meta:
        model = EditSubject
        fields = ['new_daily_goal']


class AddSubjectForm(forms.ModelForm):
    """Form for adding a new study subject with validation for duplicates."""
    class Meta:
        model = Subject
        fields = ['name', 'daily_goal']
        labels = {
            'name': 'Subject Name',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if Subject.objects.filter(user=self.user, name__iexact=name).exists():
            raise ValidationError("This subject already exists! Please enter a different name.")
        return name

