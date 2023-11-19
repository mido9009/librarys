from django.contrib import admin
from .models import Book

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Book, ProductAdmin)
