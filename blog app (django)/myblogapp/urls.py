from django.urls import path
from myblogapp import views
urlpatterns = [
  
    path('blog', views.hello,name= 'blog-index'),
    path('post_detail/<int:pk>/', views.post_details, name = 'blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name = 'blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name = 'blog-post-delete'),
    path('myblogs', views.myblogs, name = 'myblog'),
]