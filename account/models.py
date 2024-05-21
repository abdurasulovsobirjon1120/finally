from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.app import AppConfig
#
#
# class AccountConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'account'
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='customuser_set',  # Unique related_name
    #     blank=True,
    #     help_text=('The groups this user belongs to. A user will get all permissions '
    #                'granted to each of their groups.'),
    #     related_query_name='customuser',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='customuser_set',  # Unique related_name
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_query_name='customuser',
    # )
    email = models.CharField(max_length = 100 , unique = True)
    username = None
    first_name = models.CharField(max_length = 100 , null = True , blank=True)
    last_name = models.CharField(max_length=100, null=True , blank= True)
    password = models.CharField(max_length =100)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default= False )
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



# class CodeConfirmation(models.Model):
#     user = models.ForeignKey(    #ForeignKey 1 ga ko'p bog'lanishda ishlatiladi .
#         CustomUser,
#         on_delete = models.CASCADE,   # CASCADE methodi - user databasedan chiqib ketsa birdan uning barcha unga tegishli ma'lumotlar o'chib ketadi .
#         related_name='user_code', ) # related name 2 ta bo'g'langan table ga yangi nom berishda ishlatiladi . SQL dagi AS ga o'xshaydi)       # CASCADE ga o'xshagan SET_NULL degan qiymat bor ikkalasining farqi set null da user o'chiriladi lekin unga tegishli ma'lumotlar o'chib ketmaydi
#     code = models.CharField(max_length=4)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user} ---- {self.code}"