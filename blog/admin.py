""" Admin """
from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTags


@admin.register(BlogPost)
class PostBlogAdmin(admin.ModelAdmin):
    """Customize post section"""
    list_display = ('title', 'category', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'category', 'tags')
    list_editable = ("status", )
    search_fields = ('title', 'text_short', 'text_full')
    prepopulated_fields = {'slug': ('title', )}
    actions = ["publish", "unpublish"]
    fieldsets = [
        (None, {
            'fields': (('title','slug'), 'category', 'tags')
        }),
        (None, {
            'fields': (('text_short','text_full', 'status'))
        }),
    ]

    def save_model(self, request, obj, form, change):
        """ Insert here automatically username """
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def unpublish(self, request, queryset):
        """ Unpublish selected posts """
        row_update = queryset.update(status=0)
        if row_update == 1:
            message = "1 post have been updated"
        else:
            message = f"{row_update} posts have been updated"
        self.message_user(request, message)

    def publish(self, request, queryset):
        """ Publish selected posts """
        row_update = queryset.update(status=1)
        if row_update == 1:
            message = "1 post have been updated"
        else:
            message = f"{row_update} posts have been updated"
        self.message_user(request, message)

    unpublish.short_descriptions = "Unpublish"
    unpublish.allowed_permissions = ('change', )

    publish.short_descriptions = "Publish"
    publish.allowed_permissions = ('change', )


@admin.register(BlogCategory)
class CategoryBlogAdmin(admin.ModelAdmin):
    """Customize categories"""
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(BlogTags)
class TagsBlogAdmin(admin.ModelAdmin):
    """Customize tags"""
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}
