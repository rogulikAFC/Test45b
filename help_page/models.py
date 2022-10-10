from django.db import models

class HelpArticle(models.Model):
    articleNum = models.IntegerField()
    heading = models.CharField(max_length=30)
    article = models.TextField()
