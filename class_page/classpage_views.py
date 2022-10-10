from datetime import date
from os import remove
from traceback import print_tb
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ArticleFile, ArticleImage, Classes, Comment
from .models import Article

from .forms import ArticleForm, ClassCreateForm, CommentForm


def class_article_preview(request, URLcodenumber):
    Articles = Article.objects.filter(codenumber__id=URLcodenumber)\
        .only('headline', 'pub_date', 'id').order_by('-pub_date')

    classCodenumber = Classes.objects.filter(
        id=URLcodenumber).values_list('codenumber')[0]

    return render(
        request,
        'blogpage\\Articles_preview.html',

        {
            'clsName': ''.join(classCodenumber),
            'articles': Articles,
            'codenumber': URLcodenumber
        }
    )


def class_article_create(request, URLcodenumber):
    Class = Classes.objects.get(id=URLcodenumber)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        fileList = request.FILES.getlist('file_upload')

        if form.is_valid():
            form.save(commit=False)

            uuid = form.instance.id

            form.instance.codenumber = Class
            form.instance.pub_date = date.today()
            form.save()

            article2classCount = Article.objects.filter(
                codenumber__id=URLcodenumber).values_list('pub_date').count()

            if article2classCount > 30:
                print(article2classCount)

                Article.objects.filter(
                    codenumber__id=URLcodenumber)[0].delete()

            def ext_viewer(file):
                return file.name.split('.')[-1]

            image_exts = ('png', 'jpg', 'jpeg')

            for file in fileList:
                if ext_viewer(file) in image_exts:
                    ArticleImage.objects.create(
                        article=Article(id=uuid),
                        image=file
                    )
                else:
                    ArticleFile.objects.create(
                        article=Article(id=uuid),
                        file=file
                    )

            return HttpResponseRedirect(f'/class/{URLcodenumber}')
    else:
        form = ArticleForm()

    return render(
        request,
        'blogpage/create_article.html',
        {
            'clsName': Class.codenumber,
            'codenumber': URLcodenumber,
            'form': form,
        },
    )


def class_article_view(request, URLcodenumber, uuid):
    article = Article.objects.filter(
        id=uuid
    )[0]

    print(article.id)

    comments = Comment.objects.filter(
        article__id=uuid
    )

    classCode = Classes.objects.filter(
        id=URLcodenumber
    ).values_list('codenumber')[0]

    fileSet = ArticleFile.objects.prefetch_related(
        'article').filter(article__id=uuid).only('file')

    imageSet = ArticleImage.objects.prefetch_related(
        'article').filter(article__id=uuid).only('image')

    if request.method == 'POST':
        print('form cathed')
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.article = article
            print('saved')

            form.save()

            return HttpResponseRedirect(f'/view/{article.codenumber.id}/{article.id}')

        else:
            print('invalid form')

    return render(
        request,
        'blogpage\\article_view.html',

        {
            'clsName': ''.join(classCode),
            'codenumber': URLcodenumber,
            'article': article,
            'comments': comments,
            'form': CommentForm,
            'files': fileSet,
            'images': imageSet
        }
    )


def reaction_redirect(request, article_uuid, value):
    article = Article.objects.filter(
        id=article_uuid
    )[0]

    article.rating += int(value)
    article.save()

    print(article.save(), ' - saved article')

    return HttpResponseRedirect(f'/view/{article.codenumber.id}/{article_uuid}')


def create_class(request):
    if request.method == 'POST':
        model = Classes()
        form = ClassCreateForm(
            request.POST,
            instance=model
        )

        new_class = form.save(
            commit=False
        )

        if form.is_valid():
            new_class.save()

            return HttpResponseRedirect('/')

    return render(
        request,
        'blogpage\\create_class.html',

        {
            'form': ClassCreateForm
        }
    )
