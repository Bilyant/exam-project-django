from django import forms

from MOTIVE_project.common.models import Comments


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ()


class DeleteCommentForm(EditCommentForm):
    pass
