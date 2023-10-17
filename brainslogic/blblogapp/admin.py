from django.contrib import admin
from blblogapp.models import BlogModel 
# Register your models here.
@admin.register(BlogModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catg_name', 'blog_title', 'created_at', 'updated_at', 'blog_author','catg_tag','blog_isactive')
    search_fields = ('catg_name', 'blog_title', 'blog_author')

