from django.contrib import admin
from blblogapp.models import Blog, Categorie, Tag
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('catg_name', 'blog_title', 'created_at', 'updated_at', 'blog_author','catg_tag','blog_isactive')
    search_fields = ('catg_name', 'blog_title', 'blog_author')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag_name')
    search_fields = ('tag_name',)


@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','catg_name')
    search_fields = ('catg_name',)
