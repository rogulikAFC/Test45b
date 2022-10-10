from django import forms

class SearchForm(forms.Form):
    class_code=forms.CharField(
        label='Код параллели:',
        max_length=6
    )
    password=forms.CharField(
        label='Пароль:',
        max_length=100
    )
