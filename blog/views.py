"""Views"""
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import BlogPost

PAGINATE_VALUE = 4


class PostListView(ListView):
    """ Post list """
    model = BlogPost
    context_object_name = 'post_list' #rename "object_list" for template
    #allow_empty = False #error 404 if queryset is empty
    queryset = BlogPost.objects.filter(status=1)
    paginate_by = PAGINATE_VALUE

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Main page"
        return context


class PostDetailView(DetailView):
    """ Post detail view """
    model = BlogPost


class CategoryView(ListView):
    """ Category list """
    model = BlogPost
    context_object_name = 'post_list'
    paginate_by = PAGINATE_VALUE

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BlogPost.objects.filter(category__slug=slug, status=1)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = f"Category: {self.kwargs['slug'].capitalize()}"
        return context


class UserView(ListView):
    """ User list """
    model = BlogPost
    context_object_name = 'post_list'
    paginate_by = PAGINATE_VALUE

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BlogPost.objects.filter(author__username=slug, status=1)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = f"User: {self.kwargs['slug'].capitalize()}"
        return context


class TagView(ListView):
    """ Tag list """
    model = BlogPost
    context_object_name = 'post_list'
    paginate_by = PAGINATE_VALUE

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BlogPost.objects.filter(tags__slug=slug, status=1)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = f"Tag: {self.kwargs['slug'].capitalize()}"
        return context


class SearchView(ListView):
    """ Search """
    context_object_name = 'post_list'
    paginate_by = PAGINATE_VALUE
    def get_queryset(self):
        queryset = BlogPost.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) |
            Q(text_short__icontains=self.request.GET.get('q')) |
            Q(text_full__icontains=self.request.GET.get('q')),
            status=1).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        context["title"] = f"Search result: {self.request.GET.get('q')}"
        return context
