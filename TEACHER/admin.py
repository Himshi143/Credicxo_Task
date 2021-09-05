from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['teacher_id', 'teacher_name', 'teacher_department']
