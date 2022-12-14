# Generated by Django 4.0.4 on 2022-11-02 01:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cleanWater', '0004_articles_briefdesc_alter_articles_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
