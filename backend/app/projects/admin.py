from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'links', 'description', 'created_at')
    search_fields = ('name',)
