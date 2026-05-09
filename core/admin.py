from django.contrib import admin
from .models import GlobalSettings


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identité", {
            "fields": ("nom_proprietaire", "titre_poste", "photo_profil")
        }),
        ("À propos", {
            "fields": ("bio",)
        }),
        ("Liens sociaux", {
            "fields": ("lien_github", "lien_linkedin", "lien_email")
        }),
    )

    def has_add_permission(self, request):
        return not GlobalSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
