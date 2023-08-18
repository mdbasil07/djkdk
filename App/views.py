from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
#from .models import Book

# Create your views here.

class Another(View):

    def get(self, request):
        return HttpResponse('hello')

   # book = Book.objects.get(id=1)
    #output = f"We have {book.title} book in our database with {book.id}<br>"

    #for book in books:
    #    output += f"We have {book.title} book in our database with {book.id}<br>"
def first(request):
        return HttpResponse('hey')