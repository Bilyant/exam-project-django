import datetime

from django import forms
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth import views as auth_view
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from MOTIVE_project.common.models import Comments
from MOTIVE_project.forum.models import Forum
from MOTIVE_project.profiles.forms import EditProfileForm, DeleteProfileForm, LoginProfileForm, RegisterUserForm
from MOTIVE_project.profiles.models import CustomUser


class RegisterUserView(views.CreateView):
    template_name = "common/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# def user_register(request):
#     if request.method == 'GET':
#         form = RegisterUserForm()
#     else:
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'common/register.html', context)

#
class LoginUserView(auth_view.LoginView):
    template_name = 'common/login.html'
    form_class = LoginProfileForm


# def login_user(request):
#     if request.method == 'GET':
#         form = LoginProfileForm()
#     else:
#         form = LoginProfileForm(request.POST)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         try:
#             user = CustomUser.objects.get(email=email, password=password)
#         except:
#             forms.ValidationError('Невалиден имейл или парола')
#
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#     context = {
#         'form': form,
#     }
#     return render(request, 'common/login.html', context)


#
#
# def login_user(request):
#     if request.method == 'GET':
#         form = LoginProfileForm()
#     else:
#         form = LoginProfileForm(request.POST)
#         if form.is_valid():
#             form.save()


class LogoutUserView(auth_mixins.LoginRequiredMixin, auth_view.LogoutView):
    template_name = 'common/logout.html'


@login_required
def show_profile(request, pk):
    profile = CustomUser.objects.get(pk=pk)
    user_age = None
    if profile.date_of_birth:
        user_age = datetime.date.today().year - profile.date_of_birth.year
    context = {
        "pk": pk,
        'profile': profile,
        'user_age': user_age,
        'forums_participated': Comments.objects.filter(user_id=pk).all(),
        'forums_participated_count': Forum.members.through.objects.filter(customuser_id=pk).count(),
        'user_comments': Comments.objects.filter(user_id=pk).count(),
        'user_forums_created': Forum.objects.filter(host_id=pk).all(),
        'user_forums_created_count': Forum.objects.filter(host_id=pk).count(),
    }

    return render(request, 'profile/profile_show.html', context)


@login_required
def profile_edit(request, pk):
    profile = CustomUser.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


@login_required
def delete_profile(request, pk):
    profile = CustomUser.objects.get(pk=pk)
    form = DeleteProfileForm(request.POST, instance=profile)
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()  # == delete
            return redirect('index')

    context = {
        'from': form,
    }
    return render(request, 'profile/profile_delete.html', context)


@login_required
def show_profile_forums(request, pk):
    profile = CustomUser.objects.get(pk=pk)

    context = {
        'profile': profile,
        'forums_participated': Forum.members.through.objects.filter(customuser_id=pk),
        'user_forums_created': Forum.objects.filter(host_id=pk).all(),
    }

    return render(request, 'profile/profile-forums.html', context)
