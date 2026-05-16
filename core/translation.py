from modeltranslation.translator import register, TranslationOptions
from .models import GlobalSettings, GroupeCompetence, Competence, ModuleAcademique, AutoFormation


@register(GlobalSettings)
class GlobalSettingsTranslationOptions(TranslationOptions):
    fields = ('titre_poste', 'bio', 'hero_sous_titre', 'formation_sous_titre', 'formation_description')


@register(GroupeCompetence)
class GroupeCompetenceTranslationOptions(TranslationOptions):
    fields = ('nom',)


@register(Competence)
class CompetenceTranslationOptions(TranslationOptions):
    fields = ('nom',)


@register(ModuleAcademique)
class ModuleAcademiqueTranslationOptions(TranslationOptions):
    fields = ('texte',)


@register(AutoFormation)
class AutoFormationTranslationOptions(TranslationOptions):
    fields = ('titre', 'description')
