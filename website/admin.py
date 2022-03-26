from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'avatar1', 'avatar2', 'name_card', 'occupation', 'created_date')
    list_display_links = ['name_card']
    list_per_page = 20
    ordering = ['created_date']


class SocialAdmin(admin.ModelAdmin):
    list_display = ('social_network_name', 'social_network_link')
    list_display_links = ['social_network_name']
    list_per_page = 20
    ordering = ['created_date']


class ShareOnAdmin(admin.ModelAdmin):
    list_display = ('social_network_name', 'social_network_link')
    list_display_links = ['social_network_name']
    list_per_page = 20
    ordering = ['created_date']


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'text', 'created_date')
    list_display_links = ['title']
    list_per_page = 20
    ordering = ['created_date']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'project_link', 'created_date')
    list_display_links = ['title']
    list_per_page = 20
    ordering = ['created_date']


class HeadTagAdmin(admin.ModelAdmin):
    list_display = (
        'og_url', 'og_type', 'og_title', 'og_description',
        'og_image', 'og_site_name', 'description', 'author',
        'keywords', 'title', 'created_date'
    )
    list_display_links = ['title']
    list_per_page = 20
    ordering = ['created_date']


admin.site.register(Card, CardAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(ShareOn, ShareOnAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(HeadTag, HeadTagAdmin)
