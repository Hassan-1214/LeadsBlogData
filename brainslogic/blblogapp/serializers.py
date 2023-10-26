from rest_framework import serializers, status
from blblogapp.models import Blog, Categorie, Tag, Comment


class CategorieSerializer(serializers.ModelSerializer):
    catg_name =serializers.CharField()
    class Meta:
        model = Categorie
        fields = ('catg_name',) 
    
class TagSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField()
    class Meta:
        model = Tag
        fields = ('tag_name',)

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        model = Comment
        fields = '__all__'

    
class BlogSerializer(serializers.ModelSerializer):
    catg_name = serializers.CharField()
    blog_title = serializers.CharField()
    blog_description = serializers.CharField()  # Change to TextField
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    blog_author = serializers.CharField()
    tag_name = serializers.StringRelatedField(many=True)
    # blog_image = serializers.ImageField()  # Change to ImageField
    # blog_isactive = serializers.BooleanField()

    def get_tag_name(self, obj):
        return[self.tag_name for tag_name in Tag.objects.all()]
    
    class Meta:
        model = Blog
        fields = '__all__'

   