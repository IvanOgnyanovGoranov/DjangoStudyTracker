from django.contrib import admin

from tracker.models import Subject, StudyProgress


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'creation_date',
                    'daily_goal',
                    )


@admin.register(StudyProgress)
class StudyProgressAdmin(admin.ModelAdmin):
    list_display = ('subject',
                    'total_time_studied',
                    )






