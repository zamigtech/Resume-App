from django.db import models

# Create your models here.

class GeneralSettings(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    parameters = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
