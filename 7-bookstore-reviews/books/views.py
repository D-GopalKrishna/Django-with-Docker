from django.shortcuts import render
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'                     ## Can access it with this name else would had to use 
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'             ## form what we created in models.py


class SearchResultsListView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    # queryset = Book.objects.filter(title__icontains='History')

    def get_queryset(self): 
        query = self.request.GET.get('q')

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

