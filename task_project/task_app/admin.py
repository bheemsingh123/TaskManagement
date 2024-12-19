from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','start_date', 'end_date', 'user')
    search_fields = ('title', 'description')

admin.site.register(Task)