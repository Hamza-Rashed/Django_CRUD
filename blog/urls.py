from .views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView
from django.urls import path, include

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_details'),
    path('new/', BlogCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]