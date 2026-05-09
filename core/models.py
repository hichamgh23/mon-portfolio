from django.db import models


class GlobalSettings(models.Model):
    nom_proprietaire = models.CharField(
        max_length=100,
        verbose_name="Nom complet"
    )
    titre_poste = models.CharField(
        max_length=150,
        verbose_name="Titre du poste"
    )
    bio = models.TextField(
        verbose_name="Biographie"
    )
    photo_profil = models.ImageField(
        upload_to='profil/',
        verbose_name="Photo de profil"
    )
    lien_github = models.URLField(
        blank=True,
        verbose_name="Lien GitHub"
    )
    lien_linkedin = models.URLField(
        blank=True,
        verbose_name="Lien LinkedIn"
    )
    lien_email = models.EmailField(
        blank=True,
        verbose_name="Adresse email"
    )

    class Meta:
        verbose_name = "Paramètres globaux"
        verbose_name_plural = "Paramètres globaux"

    def __str__(self):
        return self.nom_proprietaire

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
