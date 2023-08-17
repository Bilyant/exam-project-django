from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AdminCustomUserModel(admin.ModelAdmin):
    search_fields = ('email', 'username', 'date_of_birth', 'residency')
    list_display = ('email', 'username', 'date_of_birth', 'residency')
    list_filter = ('email', 'username', 'date_of_birth', 'residency')
