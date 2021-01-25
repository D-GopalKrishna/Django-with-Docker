from django.contrib import admin
from .models import Book
# Register your models here.


## Which field to be displayed in admin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")


admin.site.register(Book, BookAdmin)