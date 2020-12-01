"""Blog's models"""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


DRAFT = (
    (0, 'Draft'),
    (1, 'Publish')
)


class BlogCategory(models.Model):
    """Category """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        """ Get url for category """
        return reverse('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Caregory'
        verbose_name_plural = 'Categories'


class BlogTags(models.Model):
    """Tags"""
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        """ Get url for tag """
        return reverse('tag', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class BlogPost(models.Model):
    """Posts"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    text_short = models.TextField()
    text_full = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #save only one time
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(BlogTags, blank=True, related_name='posts')
    status = models.PositiveSmallIntegerField(choices=DRAFT, default=1)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        """ Get url for post """
        return reverse('post_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_on']
