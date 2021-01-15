# AbstractUser vs AbstractBaseUser
---

The default User model in Django uses a username to uniquely identify a user during authentication. If you'd rather use an email address, you'll need to create a custom User model by either subclassing __AbstractUser__ or __AbstractBaseUser__.

Options:
* __AbstractUser__: Use this option if you are happy with the existing fields on the User model and just want to remove the username field..
* __AbstractBaseUser__: Use this option if you want to start from scratch by creating your own, completely new User model.

[click Here To Learn More](https://testdriven.io/blog/django-custom-user-model/)