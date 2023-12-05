from django.urls import path
from .views import *


urlpatterns = [
    path('blog/', BlogApiView.as_view(), name='blog'),
    path('comment/', CommentApi.as_view(), name='comment'),
    # path('cat-count/', CatNameCount.as_view(), name='count'),
    path('blog/<int:blog_id>/', BlogDetailsAPIView.as_view(), name='blog-details'),
    path('blog/<int:blog_id>/next/', NextBlogCount.as_view(), name='next-blog-count'),
    path('leadformview/', leads_form_view.as_view(), name='leads_form_view'),
    path('recent_blog/', RecentBlogDetailView.as_view(), name='recent-blog-detail'),

   
    
]
