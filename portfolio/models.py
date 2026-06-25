from django.db import models


class Stack(models.Model):
    nom = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Stack technique"
    )

    class Meta:
        verbose_name = "Stack technique"
        verbose_name_plural = "Stacks techniques"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Project(models.Model):
    titre = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )
    video = models.FileField(
        upload_to='projets/videos/',
        verbose_name="Vidéo de démonstration (60s max)"
    )
    stacks = models.ManyToManyField(
        Stack,
        blank=True,
        related_name='projets',
        verbose_name="Stack technique"
    )

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-id']

    def __str__(self):
        return self.titre
