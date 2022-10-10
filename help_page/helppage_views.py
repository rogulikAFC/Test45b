from django.shortcuts import render
from .models import HelpArticle

def help_page(request, numpage):
    print(numpage)

    record = HelpArticle.objects.get(articleNum=numpage)


    return render(request, 'helppage/index.html', 
    {'num':int(numpage),
     'help_article':record})
