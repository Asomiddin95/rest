from django.contrib import admin
from .models import Category, Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['text','created_at']