from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from LDHapp.models import Blog, Comment, Categorie,Leadsform
from LDHapp.serializers import BlogSerializer, CommentSerializer, Leads_form_serializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.db.models import Count
from django.utils import timezone
from .mypagination import myPageNumberPagination
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.exceptions import ValidationError
from LeadsData.settings import EMAIL_HOST_USER
from rest_framework.response import Response



# Create your views here.

class BlogApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = myPageNumberPagination

    def get_queryset(self,):
         # Get the most recent blog
        recent_blog = Blog.objects.filter(blog_isactive=True).order_by('-created_at').first()

        # Get all active blogs excluding the most recent one
        queryset = Blog.objects.filter(blog_isactive=True).exclude(pk=recent_blog.pk).order_by('-created_at')

        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecentBlogDetailView(APIView):
    def get(self, request, format=None):
        # Get the most recent blog
        recent_blog = Blog.objects.filter(blog_isactive=True).order_by('-created_at').first()

        if recent_blog:
            all_blogs = Blog.objects.filter(blog_isactive=True).exclude(pk=recent_blog.pk).order_by('-created_at')

            # Paginate the remaining blogs
            paginator = myPageNumberPagination()
            paginated_blogs = paginator.paginate_queryset(all_blogs, request)

            serializer = BlogSerializer(recent_blog, context={'request': request})

            # Calculate the time difference
            now = timezone.now()
            time_difference = now - recent_blog.created_at
            minutes_ago = time_difference.total_seconds() / 60
            hours_ago = minutes_ago / 60
            days_ago = hours_ago / 24

            # Add time difference to the response
            response_data = serializer.data
            response_data['time_difference'] = {
                'minutes': int(minutes_ago),
                'hours': int(hours_ago),
                'days': int(days_ago),
            }

            return Response(response_data)
        else:
            return Response({'message': 'No active blogs available'}, status=status.HTTP_404_NOT_FOUND)
class BlogDetailsAPIView(APIView):
    def get(self, request, blog_id):
        try:
            blog_post = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog_post, context={'request': request})
        data_length = len(serializer.data)
        all_blogs = Blog.objects.all()

        current_index = list(all_blogs).index(blog_post)

        next_blog = all_blogs[current_index + 1] if current_index + 1 < len(all_blogs) else None
        prev_blog = all_blogs[current_index - 1] if current_index > 0 else None

        serializer = BlogSerializer(blog_post, context={'request': request})
        data_length = len(serializer.data)
        next_blog_data = BlogSerializer(next_blog, context={'request': request}).data if next_blog else None
        prev_blog_data = BlogSerializer(prev_blog, context={'request': request}).data if prev_blog else None
        

        response_data = {
            "data": serializer.data,
            "data_length": data_length,
            "next_blog": next_blog_data,
            "prev_blog": prev_blog_data
        }

        return Response(response_data, status=status.HTTP_200_OK)



class NextBlogCount(APIView):
    def get(self, request, blog_id):
        try:
            current_blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)

        all_blogs = Blog.objects.all()
        current_index = list(all_blogs).index(current_blog)

        next_blog = all_blogs[current_index + 1] if current_index + 1 < len(all_blogs) else None
        prev_blog = all_blogs[current_index - 1] if current_index > 0 else None

        serializer = BlogSerializer(current_blog, context={'request': request})
        data_length = len(serializer.data)
        next_blog_data = BlogSerializer(next_blog, context={'request': request}).data if next_blog else None
        prev_blog_data = BlogSerializer(prev_blog, context={'request': request}).data if prev_blog else None

        response_data = {
            "data_length": data_length,
            "current_blog": serializer.data,
            "next_blog": next_blog_data,
            "prev_blog": prev_blog_data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

      
class CommentApiView(APIView):
    queryset = Blog.objects.all()
    serializer_class = CommentSerializer

   
class CommentApi(APIView):
  
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # image = request.data.get('image', '/media/authorimage.jpg')
            comment = Comment(
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                subject=serializer.validated_data['subject'],
                message=serializer.validated_data['message'],
                created_at=timezone.now(),
                # image=image,

            )
            comment.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           

# class CatNameCount(APIView):
  
#     def get(self, request):
        
#         categories_with_count = Categorie.objects.annotate(blog_count=Count('blog'))
        
#         # Create a dictionary to store the data
#         category_data = [{'category_name': category.catg_name, 'blog_count': category.blog_count} for category in categories_with_count]

#         # Return the data as JSON response
#         return JsonResponse({'categories': category_data})
    
class leads_form_view(APIView):
     
     def get(self, request):
        queryset = Leadsform.objects.all()
        serializer = Leads_form_serializer(queryset, many=True)
        
        return Response(serializer.data)
 
     def post(self, request):
        try:
            data = request.data
            
            serializer=Leads_form_serializer(data=data)
            if serializer.is_valid():
               
                subject="This is Test Mail From Codestudio Company"
                message="Dear "+ data['name'] + "\nThank you for your interest in LeadsDataHub. Our team is reviewing your inquiry and will be in touch soon with you. For immediate questions, please reply to this email. \n\nBest, \nJames Anderson \nLeads Data Hub"
                email=data['email']
                recipient_list= [email]
                emi =  send_mail(subject, message, EMAIL_HOST_USER , recipient_list, fail_silently=True)
                print(emi)
                print(EMAIL_HOST_USER)
                serializer.save()
                return Response({
                    'status':'200',
                    'Message':'Your data has saved succussfully',
                    'data':serializer.data

                })
            else:
                raise ValidationError('Something went wrong!')

            

        except Exception as e:
            print(e)
            raise ValidationError('Your Data is not valid!')