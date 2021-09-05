from django.contrib import admin
from .models import Student


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['enrollment', 'name', 'branch']
    search_fields = ['enrollment', 'name']
    list_filter = ['branch']
