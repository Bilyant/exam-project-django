from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from MOTIVE_project.common.models import Comments
from MOTIVE_project.forum.forms import ForumCreateForm, ForumEditForm, ForumDeleteForm, RatingForumForm
from MOTIVE_project.forum.models import Topics, Forum, ForumRatings
from MOTIVE_project.profiles.models import CustomUser


def forum_show_all(request):
    context = {
        'forums': Forum.objects.all().order_by('-average_rating'),
        'forums_unique_topic': Forum.objects.all().distinct('topic_id'),
        'topics': Topics.objects.all(),
        'topics_count': Topics.objects.count(),
        'comments': Comments.objects.all()
    }

    return render(request, 'forum/forum-show-all.html', context)


def forum_show_specific_topic(request, pk):
    context = {
        'forums': Forum.objects.filter(topic_id=pk).all().order_by('-average_rating'),
        'topics': Topics.objects.filter(id=pk).get(),
        'topics_count': Topics.objects.count(),
        'comments': Comments.objects.all()
    }
    return render(request, 'forum/forum-specific-topic.html', context)


@login_required
def forum_create_page(request):
    context = {
        'form': ForumCreateForm(),
    }
    return render(request, 'forum/forum-create.html', context)


@login_required
def forum_edit(request, pk):
    forum = Forum.objects.filter(pk=pk).get()
    topics = Topics.objects.all()
    current_topic = Topics.objects.filter(id=forum.topic_id).get()

    if request.method == "GET":
        form = ForumEditForm(instance=forum)
    else:
        topic_name = request.POST.get('topic')
        topic, created = Topics.objects.get_or_create(name=topic_name)
        forum.topic = topic
        forum.name = request.POST.get('name')
        forum.description = request.POST.get('description')
        forum.host = request.user
        main_image = request.FILES.get('main_image')
        if main_image:
            forum.main_image = main_image
        side_image = request.FILES.get('side_image')
        if side_image:
            forum.side_image = side_image

        forum.save()
        return redirect('forum details', pk=forum.id)

    context = {
        'form': form,
        'forum': forum,
        'topics': topics,
        'current_topic': current_topic,
    }
    return render(request, 'forum/forum-edit.html', context)


@login_required
def forum_create(request):
    topics = Topics.objects.all()
    form = ForumCreateForm()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topics.objects.get_or_create(name=topic_name)
        new_forum_data = {
            'name': request.POST.get('name'),
            'topic': topic,
            'description': request.POST.get('description'),
            'host': request.user,
            'main_image': request.FILES.get('main_image'),
            'side_image': request.FILES.get('side_image'),
        }
        Forum.objects.create(**new_forum_data)
        # form = ForumCreateForm(request.POST, request.FILES)
        return redirect('forum show all')

    context = {
        'form': form,
        'topics': topics,
    }
    return render(request, 'forum/forum-create.html', context)


def get_average_ratings(forum_ratings, pk):
    average_forum_rating = 0
    total_forum_ratings = 0
    if forum_ratings:
        for rating in forum_ratings:
            total_forum_ratings += int(rating.ratings)
        average_forum_rating = f'{(total_forum_ratings / len(forum_ratings)):.1f}'

    return average_forum_rating


def create_comment(profile, current_forum, request):
    new_comment_data = {
        'user': profile,
        'forum': current_forum,
        'content': request.POST.get('Message'),
    }
    Comments.objects.create(**new_comment_data)
    current_forum.members.add(request.user)


def add_rating(current_forum, request, profile):
    current_forum.members.add(request.user)
    new_rating_data = {
        'ratings': request.POST.get('ratings'),
        'forum_id': current_forum.id,
        'voter_id': profile.id,
    }
    ForumRatings.objects.create(**new_rating_data)


@login_required
def forum_details(request, pk):
    profile = CustomUser.objects.filter(id=request.user.pk).get()
    current_forum = Forum.objects.filter(pk=pk).get()
    current_forum_comments = current_forum.comments_set.all()
    current_forum_members = current_forum.members.all()
    has_user_rated = ForumRatings.objects.filter(voter_id=profile.id, forum_id=pk).all()
    forum_ratings = ForumRatings.objects.filter(forum_id=pk).all()
    average_forum_rating = get_average_ratings(forum_ratings, pk)

    current_forum.average_rating = average_forum_rating
    current_forum.ratings_count = len(forum_ratings)
    current_forum.save()

    if request.method == 'POST':

        if request.POST.get('Message'):
            create_comment(profile, current_forum, request)

        elif request.POST.get('ratings'):
            add_rating(current_forum, request, profile)

        return redirect('forum details', pk=current_forum.id)

    context = {
        'current_forum': current_forum,
        'current_forum_comments': current_forum_comments,
        'current_forum_members': current_forum_members,
        'rating_form': RatingForumForm(request.POST),
        'forum_id': pk,
        'has_user_rated': has_user_rated,
    }
    return render(request, 'forum/forum-details.html', context)


@login_required
def forum_rate(request, pk):
    form = RatingForumForm(request.POST)
    if request == "POST":
        forum = Forum.objects.filter(pk=pk).get()
        forum.rating = request.POST.get('rating')
        if form.is_valid():
            form.save()
        return redirect('forum details', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'forum/forum-rate.html', context)


@login_required
def forum_delete(request, pk):
    forum = Forum.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = ForumDeleteForm(instance=forum)
    else:
        form = ForumDeleteForm(request.POST, instance=forum)
        if form.is_valid():
            forum.delete()
            return redirect('forum show all')

    context = {
        'form': form,
        'forum': forum,
    }

    return render(request, 'forum/forum-delete.html', context)
