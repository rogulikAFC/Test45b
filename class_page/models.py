import os
from django.db import models
import uuid

from django.dispatch import receiver


class Classes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    codenumber = models.CharField(
        max_length=6,
        default=0
    )
    codeWord = models.CharField(
        max_length=20,
        default='None'
    )


class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    headline = models.CharField(
        max_length=50,
        default='Нет заголовка'
    )
    text = models.TextField(
        max_length=600,
    )
    pub_date = models.DateField()
    codenumber = models.ForeignKey(
        'Classes',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)


class Comment(models.Model):
    text = models.TextField(blank=False, default=None)
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )


class ArticleFile(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )
    file = models.FileField(
        upload_to='files'
    )

    def filename(self):
        return os.path.basename(self.file.name)

    def path(self):
        return f'/media/files/{os.path.basename(self.file.name)}'


@receiver(models.signals.post_delete, sender=ArticleFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


class ArticleImage(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='images'
    )

    def filename(self):
        return os.path.basename(self.image.name)

    def path(self):
        return f'/media/images/{os.path.basename(self.image.name)}'


@receiver(models.signals.post_delete, sender=ArticleImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
