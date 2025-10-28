from django.contrib import admin

from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'fab_icon', 'url')
    search_fields = ('name',)
