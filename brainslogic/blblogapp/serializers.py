from rest_framework import serializers, status
from blblogapp.models import BlogModel
import json
class BlogSerializer(serializers.ModelSerializer):
    catg_name = serializers.CharField()
    blog_title = serializers.CharField()
    blog_description = serializers.CharField()  # Change to TextField
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    blog_author = serializers.CharField()
    catg_tag = serializers.JSONField()
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
    # def to_representation(self, instance):
    #     # Get the original representation
    #     data = super().to_representation(instance)
        
    #     # Parse the catg_tag field as JSON
    #     catg_tag = json.loads(data['catg_tag'])
        
    #     # Return catg_tag in the desired format
    #     data['catg_tag'] = json.dumps(catg_tag)
    #     print(data)
    #     return data
   