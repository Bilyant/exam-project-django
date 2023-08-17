from django import forms

from MOTIVE_project.forum.models import Forum, ForumRatings


class ForumCreateForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('topic', 'name', 'description', 'main_image', 'side_image')

        widgets = {
            'description': forms.Textarea(),
        }

        labels = {
            'topic': 'Тема',
            'name': 'Име',
            'description': 'Описание',
            'main_image': 'Основна снимка',
            'side_image': 'Странична снимка',
        }


class ForumEditForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('topic', 'name', 'description', 'main_image', 'side_image')

        widgets = {
            'description': forms.Textarea(),
        }


class ForumDeleteForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ()


class RatingForumForm(forms.ModelForm):
    class Meta:
        model = ForumRatings
        fields = ('ratings',)

    widgets = {
        'ratings': forms.ChoiceField(),
    }
