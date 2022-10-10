from django.contrib import admin
from .models import ArticleFile, ArticleImage, Classes, Article, Comment


admin.site.register(Classes)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleFile)
admin.site.register(ArticleImage)
