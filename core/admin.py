from django.contrib import admin

from core import models


@admin.register(models.News)
class News(admin.ModelAdmin):
    list_display = ('name', 'origin', 'is_published',)
    search_fields = ('name', 'origin')
    list_filter = ('is_published',)


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Origin)
class Origin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
