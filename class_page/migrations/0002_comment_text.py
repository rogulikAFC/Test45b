# Generated by Django 4.0.3 on 2022-09-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
