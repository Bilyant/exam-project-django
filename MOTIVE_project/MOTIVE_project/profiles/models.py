from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 40
    USERNAME_MIN_LENGTH = 3
    EMAIL_MAX_LENGTH = 254
    FIRST_NAME_MAX_LENGTH = 40
    LAST_NAME_MAX_LENGTH = 40
    DESCRIPTION_MAX_LENGTH = 400
    MAX_LENGTH_RESIDENCY = 40

    email = models.CharField(unique=True, max_length=EMAIL_MAX_LENGTH,)
    USERNAME_FIELD = "email"
    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True)

    profile_image = models.FileField(null=True, blank=True, upload_to='images')
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, null=True, blank=True)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)
    residency = models.CharField(null=True, blank=True, max_length=MAX_LENGTH_RESIDENCY, default=None)

    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

