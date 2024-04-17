from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated_date',
        help_text=''
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created_date',
        help_text=''
    )
    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameters = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Parameters',
        help_text=''
    )

    def __str__(self):
        return f'General Setting: {self.name}'



    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

class ImageSetting(AbstractModel):

    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',

    )


    def __str__(self):
        return f'Image Setting: {self.name}'
    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)