from django.contrib import admin
from MOTIVE_project.forum.models import Topics, Forum, ForumRatings


@admin.register(Topics)
class AdminTopics(admin.ModelAdmin):
    search_fields = ('id', 'name')
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Forum)
class AdminForum(admin.ModelAdmin):
    search_fields = ('name', 'description', 'average_rating')
    list_display = ('name', 'average_rating', 'created', 'updated')
    list_filter = ('name', 'average_rating', 'created', 'updated')

