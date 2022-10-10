from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from help_page.helppage_views import help_page
from start_page import startpage_views
from help_page import helppage_views
from class_page import classpage_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        startpage_views.start_page,
        name='startpage'
    ),

    path(
        'help/<numpage>/',
        helppage_views.help_page,
        name='helppage'
    ),

    path(
        'class/<URLcodenumber>/',
        classpage_views.class_article_preview,
        name='classpage_articles_preview'
    ),

    path(
        'create/<URLcodenumber>',
        classpage_views.class_article_create,
        name='classpage_articles_create'
    ),

    path(
        'view/<URLcodenumber>/<uuid:uuid>',
        classpage_views.class_article_view,
        name='classpage_article_view'
    ),

    path(
        'createclass',
        classpage_views.create_class,
        name='create_class'
    ),

    path(
        'reaction_redirect/<article_uuid>/<value>',
        classpage_views.reaction_redirect,
        name='reaction_redirect'
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, 'FORCE_SERVE_STATIC', False):
    settings.DEBUG = True
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    settings.DEBUG = False
