from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password=None):
        """
        Creates and saves a User with the given email,phone_number and full_name and password.
     """

        user = self.model(


            phone_number=phone_number,
            full_name=full_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password=None):
        """
        Creates and saves a superuser with the given email, phone_number and full_name and password.
        """
        user = self.create_user(

            password=password,
            phone_number=phone_number,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Otp(models.Model):
    token = models.CharField(max_length=20, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11)
    randomcode = models.IntegerField()
    expertion_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone







