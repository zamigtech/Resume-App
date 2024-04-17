# Generated by Django 5.0.2 on 2024-04-17 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_imagesetting_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesetting',
            options={'ordering': ('name',), 'verbose_name': 'Image Setting', 'verbose_name_plural': 'Image Setting'},
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated_date'),
        ),
    ]