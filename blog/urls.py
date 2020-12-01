""" URL's """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('user/<slug:slug>', views.UserView.as_view(), name='user'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
    path('tag/<slug:slug>', views.TagView.as_view(), name='tag'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
