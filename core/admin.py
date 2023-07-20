from django.contrib import admin

from core import models


@admin.register(models.News)
class News(admin.ModelAdmin):
    list_display = ('title', 'origin', 'is_published',)
    search_fields = ('title', 'origin')
    list_filter = ('is_published',)


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(models.Origin)
class Origin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
