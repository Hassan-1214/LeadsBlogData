from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Categorie(models.Model):
    catg_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catg_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(null= True, blank=True, default=timezone.now)
    image = models.ImageField(null=True, upload_to="media/", default="authorimage.jpg" )


class Leadsform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=20)
    leads_catg=models.CharField(max_length=100)
    catg_name=models.CharField(max_length=100, blank=True, null=True,)
    STATUS_CHOICES={
        ('pending','Pending'),
        ('completed','Completed'),
        ('canceled','Canceled')
    }
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")


    def __str__(self):
        return self.name 
    


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    catg_name = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    blog_description = RichTextField()
    short_description = RichTextField()
    main_heading = models.CharField(max_length=100,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    blog_author = models.CharField(max_length=100, blank=True, null=True)
    author_image = models.ImageField(blank=True, null=True, upload_to="media/")
    tag_name = models.ManyToManyField(Tag)
    catg_views = models.IntegerField(default=0)
    blog_image = models.ImageField(blank=True, null=True, help_text='Image size: Width=1301 pixel. Height=556 pixel', upload_to="media/")
    blog_isactive = models.BooleanField(default=True)


    def __str__(self):
        return self.blog_title
    
