from django.shortcuts import render
from django.views import View

from .forms import BooksearchForms
from .Documents import BookDocument
from .models import Book



class Home(View):
    from_class = BooksearchForms

    def get(self,request):
        results = {}
        if request.GET.get('search'):
            results = BookDocument.search().query('match', name=request.GET['search'])

        return render(request,
         'home/home.html',
         {'form':self.form_class,
         'results':request}
         )


class BookDetail(View):
    def get(self,request,book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'home/book_detail.html', {'book':book})
        

