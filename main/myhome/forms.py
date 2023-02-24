from django import forms 


class BooksearchForms(forms.Form):
    search = forms.CharField()