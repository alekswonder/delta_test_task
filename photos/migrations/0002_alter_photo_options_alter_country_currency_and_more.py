# Generated by Django 4.2.3 on 2023-07-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'default_related_name': 'photos', 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='country',
            name='currency',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='country',
            name='government_type',
            field=models.CharField(blank=True, choices=[('absolute_monarchy', 'Абсолютная монархия'), ('constitutional_monarchy', 'Конституционная монархия'), ('dualistic_monarchy', 'Дуалистическая монархия'), ('parliament_monarchy', 'Парламентская монархия'), ('president_republic', 'Президентская республика'), ('parliament_republic', 'Парламентская республика'), ('mixed_republic', 'Смешанная республика')], max_length=23, null=True, verbose_name='Форма правления'),
        ),
    ]
