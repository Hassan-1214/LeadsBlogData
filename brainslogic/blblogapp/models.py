from django.db import models

# Create your models here.
 

class BlogModel(models.Model):
    catg_name = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    blog_author = models.CharField(max_length=100, blank=True, null=True)
    catg_tag = models.JSONField(null=True)
    catg_views = models.IntegerField(default=0)
    blog_image = models.ImageField(blank=True, null=True, help_text='Image size: Width=1301 pixel. Height=556 pixel', upload_to="media/")
    blog_isactive = models.BooleanField(default=True)


    
