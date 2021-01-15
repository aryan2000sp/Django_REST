from django.db import models

# These import will help us to extend the user model
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

"""
This class will provide the
helper function for creating
and maintaining the user and
superuser.
"""


class UserManager(BaseUserManager):
    """
    If in the future we want to extend the
    model then we can add them as
    extra_fields.
    This function will create a
    a new user and saves(commit) it
    to the database.
    """

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("User Should Have Email")

        # Now we add the user's email to models
        user = self.model(email=self.normalize_email(email), **extra_fields)

        """
        Now we add the user's password to models.
        We want the user password to be not
        exposed so we use set_password() which comes
        in build with BaseUserManager class
        """
        user.set_password(password)

        # Now we save the user. If in case we use a different database.
        user.save(using=self._db)

        return user

    """
    This function create a new
    super user.
    """

    def create_superuser(self, email, password):
        # We create a normal user first.
        user = self.create_user(email, password)

        # Now we give the user some spacial permissions
        user.is_staff = True
        user.is_superuser = True

        # Now we save the user
        user.save(using=self._db)

        return user


"""
Since we are writing the user model from
sratch we are extending the AbstractBaseUser.
AbstractBaseUser allows us to customize the
user model.
This will also define the structure of
the user model. In this class we will
define the fields in user model.
"""


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=250)

    """
    Allows us to know if the user is active in the system
    """
    is_active = models.BooleanField(default=True)

    """
    Now set the staff user activation to false
    This restricts the user accesing the
    admin page.
    """
    is_staff = models.BooleanField(default=False)

    """
    Since we customise the user model we
    need the customized user manager to
    handle the backend management of data.
    Hence we set the object to UserManager() class.
    NOTE:-
    Ojects are Model managers.
    """
    objects = UserManager()
    USERNAME_FIELD = "email"
