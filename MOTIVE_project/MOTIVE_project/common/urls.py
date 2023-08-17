from django.urls import path

from MOTIVE_project.common.views import index, edit_comment, delete_comment, ForumRulesView

urlpatterns = (
    path('', index, name='index'),
    path('rules/', ForumRulesView.as_view(), name='forum rules'),
    path('comment/edit/<int:pk>', edit_comment, name='comment edit'),
    path('comment/edlete/<int:pk>', delete_comment, name='comment delete'),
)
