from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    # creates a filter box so that you can filter the posts in the admin center
    list_display = ('title', 'slug', 'status', 'created_on')
    # can search post by listing
    search_fields = ('title', 'content')
    # can find post via search bar
    prepopulated_fields = {'slug': ('title',)}
    # pre-populates the slug field with text typed in the title field
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
