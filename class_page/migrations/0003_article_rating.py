# Generated by Django 4.0.3 on 2022-10-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_page', '0002_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
