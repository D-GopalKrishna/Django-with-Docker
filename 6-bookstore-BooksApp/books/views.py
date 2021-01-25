from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'                     ## Can access it with this name else would had to use 
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'