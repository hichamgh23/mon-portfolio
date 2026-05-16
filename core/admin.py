from django.contrib import admin
from .models import GlobalSettings, ContactMessage, GroupeCompetence, Competence, ModuleAcademique, AutoFormation


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'objet', 'date_envoi', 'lu')
    list_filter = ('lu',)
    readonly_fields = ('prenom', 'nom', 'email', 'objet', 'message', 'date_envoi')
    list_display_links = ('nom',)

    def has_add_permission(self, request):
        return False


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identité", {
            "fields": ("nom_proprietaire", "titre_poste", "photo_profil")
        }),
        ("Accueil", {
            "fields": ("hero_sous_titre",)
        }),
        ("À propos", {
            "fields": ("bio",)
        }),
        ("Formation académique", {
            "fields": ("formation_sous_titre", "formation_description")
        }),
        ("Liens sociaux", {
            "fields": ("lien_github", "lien_linkedin", "lien_email", "lien_facebook", "lien_instagram", "lien_whatsapp", "telephone")
        }),
    )

    def has_add_permission(self, request):
        return not GlobalSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CompetenceInline(admin.TabularInline):
    model = Competence
    extra = 1


@admin.register(GroupeCompetence)
class GroupeCompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'icone', 'ordre')
    inlines = [CompetenceInline]


@admin.register(ModuleAcademique)
class ModuleAcademiqueAdmin(admin.ModelAdmin):
    list_display = ('texte', 'ordre')


@admin.register(AutoFormation)
class AutoFormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'statut', 'ordre')
    list_editable = ('ordre',)
