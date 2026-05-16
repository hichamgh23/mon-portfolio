from django.db import models


class ContactMessage(models.Model):
    prenom = models.CharField(max_length=100, verbose_name="Prénom", default='')
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    objet = models.CharField(max_length=200, verbose_name="Objet", default='')
    message = models.TextField(verbose_name="Message")
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Reçu le")
    lu = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-date_envoi']

    def __str__(self):
        return f"{self.nom} — {self.email}"


class GlobalSettings(models.Model):
    nom_proprietaire = models.CharField(max_length=100, verbose_name="Nom complet")
    titre_poste = models.CharField(max_length=150, verbose_name="Titre du poste")
    bio = models.TextField(verbose_name="Biographie")
    photo_profil = models.ImageField(upload_to='profil/', verbose_name="Photo de profil")
    lien_github = models.URLField(blank=True, verbose_name="Lien GitHub")
    lien_linkedin = models.URLField(blank=True, verbose_name="Lien LinkedIn")
    lien_email = models.EmailField(blank=True, verbose_name="Adresse email")
    lien_facebook = models.URLField(blank=True, verbose_name="Lien Facebook")
    lien_instagram = models.URLField(blank=True, verbose_name="Lien Instagram")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Numéro de téléphone")
    lien_whatsapp = models.CharField(max_length=20, blank=True, verbose_name="Numéro WhatsApp")
    hero_sous_titre = models.TextField(
        blank=True,
        verbose_name="Hero — Phrase d'accroche",
        help_text="Texte affiché sous le titre de poste dans la section d'accueil"
    )
    formation_sous_titre = models.CharField(
        max_length=100, default="Algérie / Belgique",
        verbose_name="Formation — Sous-titre (ex: Algérie / Belgique)"
    )
    formation_description = models.TextField(
        blank=True,
        verbose_name="Formation — Description académique"
    )

    class Meta:
        verbose_name = "Paramètres globaux"
        verbose_name_plural = "Paramètres globaux"

    def __str__(self):
        return self.nom_proprietaire

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


# ── COMPÉTENCES ──────────────────────────────────────────────────────────────

class GroupeCompetence(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du groupe")
    icone = models.CharField(
        max_length=60, verbose_name="Icône Bootstrap",
        help_text="Nom de l'icône Bootstrap Icons (ex: globe2, phone, database)"
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['ordre']
        verbose_name = "Groupe de compétences"
        verbose_name_plural = "Groupes de compétences"

    def __str__(self):
        return self.nom


class Competence(models.Model):
    NIVEAU_CHOICES = [
        ('strong', 'Maîtrisé'),
        ('normal', 'Connu'),
        ('learning', 'En apprentissage'),
    ]
    groupe = models.ForeignKey(
        GroupeCompetence, on_delete=models.CASCADE,
        related_name='competences', verbose_name="Groupe"
    )
    nom = models.CharField(max_length=100, verbose_name="Nom")
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES, default='normal', verbose_name="Niveau")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre")

    class Meta:
        ordering = ['ordre']
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.nom


# ── FORMATION ACADÉMIQUE ──────────────────────────────────────────────────────

class ModuleAcademique(models.Model):
    texte = models.CharField(max_length=200, verbose_name="Intitulé du module")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre")

    class Meta:
        ordering = ['ordre']
        verbose_name = "Module académique"
        verbose_name_plural = "Modules académiques"

    def __str__(self):
        return self.texte


# ── AUTO-FORMATION ────────────────────────────────────────────────────────────

class AutoFormation(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('en_approfondissement', 'En approfondissement'),
        ('acquis', 'Acquis'),
    ]
    statut = models.CharField(max_length=30, choices=STATUT_CHOICES, verbose_name="Statut")
    titre = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    tags = models.CharField(
        max_length=300, blank=True, verbose_name="Tags",
        help_text="Séparés par des virgules (ex: Python, Django, DRF)"
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre")

    class Meta:
        ordering = ['ordre']
        verbose_name = "Auto-formation"
        verbose_name_plural = "Auto-formations"

    def __str__(self):
        return self.titre

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
