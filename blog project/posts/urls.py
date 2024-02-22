from django.urls import path
from . import views

urlpatterns = [
    path('' , views.blog_list , name='post_list' ),
    path("<int:pk>",views.blog_detail , name="blog_detail")
]
