from django.urls import path

from MOTIVE_project.profiles.views import RegisterUserView, LogoutUserView, show_profile, profile_edit, \
    delete_profile, LoginUserView, show_profile_forums

urlpatterns = (
    path('<int:pk>/', show_profile, name='profile'),
    path('edit/<int:pk>/', profile_edit, name='profile edit'),
    path('forums/<int:pk>/', show_profile_forums, name='profile show forums'),
    # path('forums/topic/<int:pk>/', show_profile_forums, name='profile show forums'),
    path('register/', RegisterUserView.as_view(), name='user register'),
    path('login/', LoginUserView.as_view(), name='user login'),
    path('logout/', LogoutUserView.as_view(), name='user logout'),
    path('delete/<int:pk>', delete_profile, name='user delete'),
)

