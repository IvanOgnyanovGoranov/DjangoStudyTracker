from django.contrib import admin

from tracker.models import Subject, StudyProgress


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'created_at',
                    'daily_goal',
                    )


@admin.register(StudyProgress)
class StudyProgressAdmin(admin.ModelAdmin):
    list_display = ('subject',
                    )







