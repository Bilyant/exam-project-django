from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from MOTIVE_project.common.forms import EditCommentForm, DeleteCommentForm
from MOTIVE_project.common.models import Comments
from MOTIVE_project.forum.models import Forum
from MOTIVE_project.profiles.models import CustomUser


def index(request):
    login_or_profile = 'Профил' if request.user.is_authenticated else 'Вход'
    register_or_exit = 'Изход' if request.user.is_authenticated else 'Регистриране'

    context = {
        'login_or_profile': login_or_profile,
        'register_or_exit': register_or_exit,
    }

    return render(request, 'common/index.html', context)


class ForumRulesView(generic.TemplateView):
    template_name = 'forum/forum-rules.html'


@login_required
def edit_comment(request, pk):
    profile = CustomUser.objects.filter(id=request.user.pk).get()
    comment = Comments.objects.filter(id=pk).get()
    current_forum = Forum.objects.filter(pk=comment.forum_id).get()
    form = EditCommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_comment_data = {
                'user': profile,
                'forum': current_forum,
                'content': request.POST.get('Message'),
            }
            Comments.objects.filter(id=pk).update(**new_comment_data)
            return redirect('forum details', pk=comment.forum_id)

    context = {
        'profile': profile,
        'comment': comment,
        'form': form,
    }
    return render(request, 'common/comment-edit.html', context)


@login_required()
def delete_comment(request, pk):
    comment = Comments.objects.filter(id=pk).get()
    form = DeleteCommentForm()

    if request.method == 'POST':
        form = DeleteCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.delete()
            return redirect('forum details', pk=comment.forum_id)

    context = {
        'form': form,
        'comment': comment,
        'pk': pk,
    }
    return render(request, 'common/comment-delete.html', context)
