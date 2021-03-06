from django.contrib import admin

from .models import Vit, Plustag, Comment, Embed

class PlustagAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating']
    list_filter = ['name', 'rating']
    search_fields = ['name']
    list_per_page = 10

class CommentAdmin(admin.TabularInline):
    readonly_fields = ['body','user', 'vit', 'date']
    extra = 0
    model = Comment
class EmbedAdmin(admin.TabularInline):
    readonly_fields = ['url', 'vit', 'title', 'description', 'image_url', 'video_url']
    extra = 0
    model = Embed

class VitAdmin(admin.ModelAdmin):
    list_display = ['body', 'user', 'image', 'video', 'like_count', 'date']
    inlines = [CommentAdmin, EmbedAdmin]
    list_filter = ['user', 'date']
    search_fields = ['body']
    list_per_page = 10
    readonly_fields = ['user', 'likes', 'like_count', 'mentions', 'plustag', 'date',]

    

admin.site.register(Vit, VitAdmin)
admin.site.register(Plustag, PlustagAdmin)