# Generated by Django 2.1.1 on 2018-10-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0008_auto_20181030_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='missao',
            name='nice_tempo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='missao',
            name='data',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
