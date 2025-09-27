from django import forms

from tracker.models import Subject, EditSubject


class EditSubjectForm(forms.ModelForm):
    # new_daily_goal = forms.IntegerField(
    #     min_value=1,
    #     max_value=1080,
    # )

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

    def clean_name(self):
        name = self.cleaned_data['name']
        if Subject.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(
                f'Subject "{name}" already exists! Please enter a different name.'
            )
        return name