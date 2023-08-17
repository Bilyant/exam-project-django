from django.contrib.auth import get_user_model
from django.db import models

from MOTIVE_project.profiles.models import CustomUser


class Topics(models.Model):
    TOPIC_MAX_LENGTH = 60

    name = models.CharField(
        max_length=TOPIC_MAX_LENGTH, unique=True)

    def __str__(self):
        return f'Topic name: {self.name}'

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Topic'


class Forum(models.Model):
    NAME_MAX_LENGTH = 60
    TOPIC_MAX_LENGTH = 60
    DESCRIPTION_MAX_LENGTH = 600
    CHOICES_MAX_LENGTH = 20

    host = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    members = models.ManyToManyField(CustomUser, related_name='members', blank=True)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_image = models.FileField(null=True, blank=True, upload_to='forum_main_images')
    side_image = models.FileField(null=True, blank=True, upload_to='forum_side_images')
    average_rating = models.FloatField(null=True, blank=True, default=0)
    ratings_count = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f'Forum name: {self.name}, topic: {self.topic.name}'

    @property
    def get_ratings_round(self):
        iterations_needed = 0
        iterations = {
            0: '',
            1: '1',
            2: '12',
            3: '123',
            4: '1234',
            5: '12345',
        }
        if self.average_rating:
            iterations_needed = int(self.average_rating)
        return iterations.get(iterations_needed)


class ForumRatings(models.Model):
    RATINGS_MAX_LENGTH = 20

    ratings = models.CharField(
        choices=(
            ('1', '1'),
            ('1', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ),
        max_length=RATINGS_MAX_LENGTH,
        null=True,
        blank=True,
    )

    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'ForumRating'
