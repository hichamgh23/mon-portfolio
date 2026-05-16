from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date')
    list_filter = ('categorie',)
    search_fields = ('titre',)
    fieldsets = (
        ("Informations générales", {
            "fields": ("titre", "categorie", "date", "image", "video", "lien_github", "lien_demo")
        }),
        ("Contenu", {
            "fields": ("description", "defi_technique")
        }),
    )
