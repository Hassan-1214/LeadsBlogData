from django.db import models

# Create your models here.
class Categorie(models.Model):
    catg_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catg_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    catg_name = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    blog_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    blog_author = models.CharField(max_length=100, blank=True, null=True)
    author_image = models.ImageField(blank=True, null=True, upload_to="media/")
    catg_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    catg_views = models.IntegerField(default=0)
    blog_image = models.ImageField(blank=True, null=True, help_text='Image size: Width=1301 pixel. Height=556 pixel', upload_to="media/")
    blog_isactive = models.BooleanField(default=True)


    def __str__(self):
        return self.blog_title
    
