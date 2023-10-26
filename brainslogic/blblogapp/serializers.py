from rest_framework import serializers, status
from blblogapp.models import Blog, Categorie, Tag
import json
class BlogSerializer(serializers.ModelSerializer):
    catg_name = serializers.CharField()
    blog_title = serializers.CharField()
    blog_description = serializers.CharField()  # Change to TextField
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    blog_author = serializers.CharField()
    catg_tag = serializers.CharField()
    # blog_image = serializers.ImageField()  # Change to ImageField
    # blog_isactive = serializers.BooleanField()


    class Meta:
        model = Blog
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    catg_name = serializers.CharField()

    class Meta:
        model = Categorie
        fields = ['id', 'catg_name']
    
class TagSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ['id', 'tag_name']
    