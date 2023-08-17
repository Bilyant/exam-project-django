from django.contrib import admin

from MOTIVE_project.common.models import Comments


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    search_fields = ('user', 'forum')
    list_display = ('content', 'user', 'forum', 'created', 'updated')
    list_filter = ('user', 'forum')
