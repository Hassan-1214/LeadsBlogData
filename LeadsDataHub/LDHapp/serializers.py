import re
from rest_framework import serializers, status
from LDHapp.models import Blog, Categorie, Tag, Comment, Leadsform


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
    created_at = serializers.DateTimeField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class Leads_form_serializer(serializers.ModelSerializer):

    class Meta:
       model=Leadsform
       fields='__all__'

# valdiating email here

    def validate(self, validated_data):
        if validated_data.get('email'):
            email=validated_data['email']
            regex=re.compile("/^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/gm")
            if not regex.search(email) == None:
                print(f"The email address {email} is not valid")
                raise serializers.ValidationError("Please enter a valid email address!")
        lc=validated_data.get('leads_catg')
        if lc =='Others' and lc != "":
            if validated_data.get('catg_name') == "":
                raise serializers.ValidationError("Please enter catogory name")
            
        
        return validated_data
    

class BlogSerializer(serializers.ModelSerializer):
    catg_name = serializers.CharField()
    blog_title = serializers.CharField()
    blog_description = serializers.CharField()  # Change to TextField
    short_description = serializers.CharField()
    main_heading = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    blog_author = serializers.CharField()
    tag_name = serializers.StringRelatedField(many=True)
    # blog_image = serializers.ImageField()  # Change to ImageField
    # blog_isactive = serializers.BooleanField()

    def get_tag_name(self, obj):
        return[self.tag_name for tag_name in Tag.objects.all()]
    
    
    def get_absolute_image_url(self, image_url):
        # Get the request from the serializer context
        request = self.context.get('request', None)
        if request:
            # Build the absolute URL using the request's build_absolute_uri method
            return request.build_absolute_uri(image_url)
        else:
            # If there's no request in the context, return the original URL
            return image_url

    # Override the to_representation method to modify the image URLs
    def to_representation(self, instance):
        # Call the parent class's to_representation method
        data = super().to_representation(instance)

        # Update the image URL fields with the absolute URL
        data['author_image'] = self.get_absolute_image_url(data['author_image'])
        data['blog_image'] = self.get_absolute_image_url(data['blog_image'])

        return data
    
    class Meta:
        model = Blog
        fields = '__all__'

   