from django.test import TestCase

# Imports the user model or the database table for storing the users
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """
        Tests the user creation with email
        """
        email = "someName@gmaal.com"
        password = "testPass12@A1"

        # Create a dummy user to test if the user is created or not
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        """
        Now we check for the user email has been set
        properply by calling the assertEqual()
        Since the password is incrypted we can not
        access the password so we call the assertTrue()
        for password.
        """
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        This function will test if the
        user email is normalized or not.
        Normalization of email is just
        converting the domain name to
        lower case.
        """
        email = "test@SOME_DOMAIN.COM"
        user = get_user_model().objects.create_user(email, "somePassWord!a")

        self.assertEqual(user.email, email.lower())

    """
    This function will check if
    the empty email is passed
    then an error is raised or not
    """

    def test_new_user_email_invalid(self):
        """
        This function comes with the
        TestCase. Whatever is passed
        in this fuction that gives the
        error is passed as assertions
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "somePassWord!a")

    """
    This function will check if a new
    super user created using the CLI
    (Command Line Interface)
    """

    def test_create_new_superuer(self):
        user = get_user_model().objects.create_superuser(
            "test@somedomain.com", "testPassword!A1"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
