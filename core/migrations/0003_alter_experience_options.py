# Generated by Django 5.0.2 on 2024-04-26 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_education'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('start_date',), 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
    ]
