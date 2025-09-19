from django import forms

class EditSubject(forms.Form):
    new_daily_goal = forms.IntegerField()


class AddSubject(forms.Form):
    subject_name = forms.CharField(max_length=50)
    daily_goal = forms.IntegerField(min_value=1, max_value=1440)