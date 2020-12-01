""" Simple tags """
from django import template
from django.db.models import Count
from blog.models import BlogCategory, BlogTags


register = template.Library()


@register.simple_tag()
def get_categories():
    """Get categories where we have more that 0 posts and status = published
    cnt = posts in each category"""
    categories = BlogCategory.objects.filter(blogpost__status=1).annotate(cnt=Count('blogpost')).filter(cnt__gt=0).order_by('title')
    return categories


@register.simple_tag()
def get_tags():
    """Get tags where we have more that 0 posts and status = published
    posts = related name in model _BlogPost_ for field tags"""
    tags = BlogTags.objects.filter(posts__status=1).annotate(cnt=Count('posts')).filter(cnt__gt=0).order_by('title')
    return tags
