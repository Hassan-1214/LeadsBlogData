from django.contrib import admin
from LDHapp.models import Blog, Categorie, Tag, Comment, Leadsform
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('catg_name', 'blog_title', 'created_at', 'updated_at', 'blog_author','blog_isactive')
    search_fields = ('catg_name', 'blog_title', 'blog_author')
    ordering = ['blog_title']

    def get_tag_names(self, obj):
        return ", ".join([tag.tag_name for tag in obj.catg_tags.all()])
    get_tag_names.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag_name')
    search_fields = ('tag_name',)
    ordering = ['id']

@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','catg_name')
    search_fields = ('catg_name',)
    ordering = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','created_at')
    search_fields = ('name', 'email', 'subject', 'message','created_at')
    ordering = ['name']

class LeadsformAdmin(admin.ModelAdmin):
    
    # list_display = ('key', 'value')
    list_display = ('name', 'contact', 'email','leads_catg','catg_name','status')
    
    
admin.site.register(Leadsform,LeadsformAdmin)