from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('delete/<int:pk>/', views.deletePost, name='delete'),
  path('update/<int:pk>/', views.updatePost, name='update'),
  path('post/<int:pk>', views.post, name='post'),
  path('publish/', views.publish, name='publish')
]