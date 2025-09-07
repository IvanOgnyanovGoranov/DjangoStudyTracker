from django import forms

class EditSubject(forms.Form):
    new_daily_goal = forms.IntegerField()
