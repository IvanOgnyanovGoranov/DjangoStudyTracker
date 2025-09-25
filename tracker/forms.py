from django import forms

from tracker.models import Subject


class EditSubjectForm(forms.Form):
    new_daily_goal = forms.IntegerField(min_value=1, max_value=1080)


class AddSubjectForm(forms.ModelForm):
    daily_goal = forms.IntegerField(
        min_value=1,
        max_value=1080,
    )
    class Meta:
        model = Subject
        fields = ['name', 'daily_goal']
        labels = {
            'name': 'Subject Name',
        }
