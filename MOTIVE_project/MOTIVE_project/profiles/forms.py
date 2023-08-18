from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.regex_helper import _lazy_re_compile
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from MOTIVE_project.profiles.models import CustomUser


class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={
            'id': 'id_username',
            'name': 'username',
            'type': 'text',
            'placeholder': 'example@gmail.com',
            'autofocus': '',
            'autocapitalize': 'none',
            'autocomplete': 'username',
            'maxlength': '254',
            'required': ''
        })

        self.fields['username'].widget = forms.TextInput(attrs={
            'id': 'id_username',
            'name': 'username',
            'type': 'text',
            'placeholder': 'Потребител',
            'autofocus': '',
            'autocapitalize': 'none',
            'autocomplete': 'username',
            'maxlength': '254',
            'required': ''
        })

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'id': 'id_password1',
            'name': 'password',
            'type': 'password',
            'autocomplete': 'current-password',
            'required': '',
            'placeholder': '••••••••',
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'id': 'id_password2',
            'name': 'password',
            'type': 'password',
            'autocomplete': 'current-password',
            'required': '',
            'placeholder': '••••••••',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email.strip == "":
            raise forms.ValidationError('Имейлът е задължителна')

        try:
            validate_email(email)
        except ValidationError as e:
            raise forms.ValidationError('Моля въведете валиден имейл')

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 3:
            raise forms.ValidationError('Потребителското име трябва да съдържа поне 3 символа')
        if username.strip == "":
            raise forms.ValidationError('Потребителското поле е задължително')

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError('Паролата трябва да съдържа поне 4 символа')
        if password1.strip == "":
            raise forms.ValidationError('Паролата е задължителна')
        if password1.isdigit():
            raise forms.ValidationError('Паролата е задължителна')
        if password1.isalpha():
            raise forms.ValidationError('Паролата не може да съдържа само букви')

        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')

        if len(password2) < 6:
            raise forms.ValidationError('Паролата трябва да съдържа поне 4 символа')
        if password2.strip == "":
            raise forms.ValidationError('Паролата е задължителна')
        if password2.isdigit():
            raise forms.ValidationError('Паролата е задължителна')
        if password2.isalpha():
            raise forms.ValidationError('Паролата не може да съдържа само букви')
        if password1 != password2:
            raise forms.ValidationError('Двете пароли трябва да са идентични')

        return password2


class LoginProfileForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'id': 'id_username',
            'name': 'username',
            # 'type': 'email',
            'placeholder': 'example@gmail.com',
            'autofocus': '',
            'autocapitalize': 'none',
            'autocomplete': 'email',
            'maxlength': '254',
            'required': '',
            # 'oninvalid': "this.setCustomValidity('Моля въведете валиден имейл')"
        })

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'id': 'id_password',
            'name': 'password',
            'type': 'password',
            'autocomplete': 'current-password',
            'required': '',
            'placeholder': '••••••••',
            # 'oninvalid': "this.setCustomValidity('Моля въведете валидна парола')"
        })

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #
    #     user = CustomUser.objects.get(email=username, password=password)
    #     if user is None:
    #         raise forms.ValidationError('Невалиден имейл или парола')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'description', 'profile_image', 'date_of_birth', 'residency')
        # fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                'type': 'text',
                'id': 'id_username',
                'class': 'form-control form-control-alternative',
                'value': '',
                'maxlength': '40',
            }),

            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-alternative',

            }),

            'residency': forms.TextInput(attrs={
                'placeholder': 'Държава, град',
                'type': 'text',
                'id': 'id_residency',
                'class': 'form-control form-control-alternative',
                # 'value': '',
                'maxlength': '40',
                'name': 'residency',
            }),

            'first_name': forms.TextInput(attrs={
                'placeholder': 'Име',
                'type': 'text',
                'id': 'id_first_name',
                'class': 'form-control form-control-alternative',
                'value': '',
                'maxlength': '40',
                'name': 'first_name',
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Фамилия',
                'type': 'text',
                'id': 'id_last_name',
                'class': 'form-control form-control-alternative',
                'value': '',
                'maxlength': '40',
                'name': 'last_name',
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Няколко думи за мен...',
                'type': 'text',
                'id': 'id_description',
                'class': 'form-control form-control-alternative',
                'value': '',
                'maxlength': '400',
                'name': 'description',
                'rows': '4',
                'cols': '40',
            }),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
