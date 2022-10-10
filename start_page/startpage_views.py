from django.shortcuts import HttpResponseRedirect, render
from .forms import SearchForm

from class_page.models import Classes

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def start_page(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            classCode = form.cleaned_data['class_code']
            password = form.cleaned_data['password']

            classFromInst = Classes.objects.filter(
                codenumber=classCode).only('id', 'codeWord')[0]

            if classFromInst and password == classFromInst.codeWord:
                return HttpResponseRedirect(
                    f'/class/{classFromInst.id}'
                )

    return render(request, 'startpage\\index.html',
                  {'search_form': SearchForm}
                  )
