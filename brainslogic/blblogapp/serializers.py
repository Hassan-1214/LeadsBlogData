from rest_framework import serializers, status
from blblogapp.models import BlogModel

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
        model = BlogModel
        fields = '__all__'
        # extra_kwargs = {
        #     'blog_description': {'required': False},
        #     'created_at': {'required': False},
        #     'updated_at': {'required': False},
        #     'blog_author': {'required': False},
        #     'blog_image': {'required': False},
        # }

   