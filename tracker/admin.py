from django.contrib import admin

from tracker.models import Subject, StudyProgress, EditSubject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'created_at',
                    'daily_goal',
                    'user',
                    )


@admin.register(StudyProgress)
class StudyProgressAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'time_studied',
        'studied_on',
                    )


@admin.register(EditSubject)
class EditSubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'edited_at',
        'new_daily_goal',
    )





