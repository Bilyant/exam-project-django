from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from MOTIVE_project.forum.models import Forum
from MOTIVE_project.profiles.models import CustomUser


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Comment'

    def __str__(self):
        return f'Comment from forum "{self.forum.name}" ; user: "{self.user.username}"'
