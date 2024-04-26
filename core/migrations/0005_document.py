# Generated by Django 5.0.2 on 2024-04-26 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created_date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('slug', models.SlugField(blank=True, default='', max_length=255, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, default='', max_length=255, verbose_name='Button Text')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='Description')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]