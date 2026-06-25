from django.contrib import admin
from .models import Project, Stack


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    search_fields = ('titre',)
    filter_horizontal = ('stacks',)
    fields = ('titre', 'video', 'stacks')

    class Media:
        js = ('js/admin_video_duration.js',)
