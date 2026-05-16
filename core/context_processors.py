from .models import GlobalSettings


def global_settings(request):
    return {
        'gs': GlobalSettings.objects.first(),
        'lang_list': [
            ('fr', '🇫🇷', 'Français'),
            ('en', '🇬🇧', 'English'),
            ('nl', '🇳🇱', 'Nederlands'),
        ],
    }
