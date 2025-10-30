from django.contrib import admin
from tracker.models import Subject, StudyProgress, EditSubject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'created_at',
                    'daily_goal',
                    'user',
                    )
    list_filter = (
        'user',
        'name',
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
        'new_daily_goal',
    )
    readonly_fields = ('edited_at',)





