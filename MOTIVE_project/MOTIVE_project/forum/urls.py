from django.urls import path

from MOTIVE_project.forum.views import ViewForumView, forum_create_page, forum_create, forum_details, forum_edit, \
    forum_delete, forum_rate, forum_show_specific_topic

urlpatterns = (
    path('', ViewForumView.as_view(), name='forum show all'),
    path('topic/<int:pk>/', forum_show_specific_topic, name='forum show specific topic'),
    path('create-form/', forum_create_page, name='forum create page'),
    path('create/', forum_create, name='forum create'),
    path('details/<int:pk>/', forum_details, name='forum details'),
    path('edit/<int:pk>/', forum_edit, name='forum edit'),
    path('delete/<int:pk>/', forum_delete, name='forum delete'),
    path('rate/<int:pk>/', forum_rate, name='forum rate'),

)
