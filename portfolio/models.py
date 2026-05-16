from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    CATEGORIE_CHOICES = [
        ('django', 'Django'),
        ('react_native', 'React Native'),
    ]

    titre = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )
    categorie = models.CharField(
        max_length=20,
        choices=CATEGORIE_CHOICES,
        verbose_name="Catégorie"
    )
    description = RichTextField(
        verbose_name="Description"
    )
    defi_technique = models.TextField(
        verbose_name="Défi technique"
    )
    image = models.ImageField(
        upload_to='projets/',
        verbose_name="Image du projet"
    )
    video = models.FileField(
        upload_to='projets/videos/',
        blank=True,
        null=True,
        verbose_name="Vidéo de démonstration"
    )
    lien_github = models.URLField(
        blank=True,
        verbose_name="Lien GitHub"
    )
    lien_demo = models.URLField(
        blank=True,
        verbose_name="Lien démo (laisser vide si non déployé)"
    )
    date = models.DateField(
        verbose_name="Date de réalisation"
    )

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-date']

    def __str__(self):
        return self.titre
