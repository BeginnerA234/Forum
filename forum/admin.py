from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    Chapter, SubSection,
    Theme, Comment
)


@admin.register(Chapter)
class ChapterAdmin(ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    readonly_fields = ('title', 'slug')


@admin.register(SubSection)
class SubSectionAdmin(ModelAdmin):
    list_display = ('title', 'chapter', 'slug')
    search_fields = ('title',)
    list_filter = ('chapter',)
    # readonly_fields = ('title', 'slug')


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('creator', 'theme', 'comment',)
    search_fields = ('creator__username', 'theme__title', 'comment',)
    list_filter = ('created', 'update',)
    readonly_fields = ('creator', 'theme', 'quote')



@admin.register(Theme)
class ThemeAdmin(ModelAdmin):
    list_display = ('creator', 'sub_section', 'title', 'slug', 'content')
    search_fields = ('creator__username', 'title', 'content', 'sub_section__title')
    list_filter = ('created', 'update',)
    # fieldsets = (
    #     (
    #         'Тема',
    #         {
    #             'fields': ('creator', 'sub_section', 'title', 'comment'),
    #         }
    #     ),
    # )
