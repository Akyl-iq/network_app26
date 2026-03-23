from django.contrib import admin
from .models import *


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class SavePostItemInline(admin.TabularInline):
    model = SavePostItem
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "created_date")
    search_fields = ("description",)
    list_filter = ("created_date",)
    inlines = [ContentInline, CommentInline]


@admin.register(SavePost)
class SavePostAdmin(admin.ModelAdmin):
    inlines = [SavePostItemInline]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_fields = ("username", "phone_number")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_date")
    search_fields = ("text",)


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "like")


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "like")


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("user", "created_date")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "following")


admin.site.register(Hashtag)
admin.site.register(Content)
admin.site.register(SavePostItem)
admin.site.register(Chat)
admin.site.register(Messages)