from django.test import TestCase, Client
from django.contrib.auth import get_user_model

"""
This import will allow us
to generate the urls to
test the admin page.
"""
from django.urls import reverse


class AdminSiteTests(TestCase):
    """
    This will create a setup
    for testing the admin page.
    This function will called
    everytime the a test function
    runs.
    """
    def setUp(self):
        # We variable will hold the Client() object
        self.client = Client()

        # Now we create a dummy superUser for testing
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@somedomain.com',
            password='somePassword!A'
        )

        # Now we forcefully login the superuser for testing
        self.client.force_login(self.admin_user)

        # Now we create a normal user
        self.user = get_user_model().objects.create_user(
            email='user@somedomain.com',
            password='somePassword!A',
            name='SomeName'
        )

    """
    This function will test if
    the user was created and stored
    in the admin list.
    """
    def test_users_listed(self):
        # First we get the urls where the users lists are loacted
        url = reverse('admin:core_user_changelist')

        # Now we create a response object which store repose recieved from url
        response = self.client.get(url)

        # Now we check if the reponse contains the user object
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    """
    This test will check if the
    user change page is redered
    correctly
    """
    def test_change_user_page(self):
        """
        First we get the url for the user change
        page. The args in reverse will assign a
        endpoint to the url and will produce a
        url like: admin/core/user/1
        where 1 is the args
        For informantion:-
        https://www.youtube.com/watch?v=JqbBGxDLQeU
        also use the following link
        to know the conventions for url names
        in django for admin:
        https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#reversing-admin-urls
        """
        url = reverse(
            'admin:core_user_change',
            args=[self.user.id]
        )

        """
        Now we will get pass the url
        as request to get user change
        page render information in
        the form of response object
        """
        response = self.client.get(url)

        """
        Now we check if the status code
        is 200 or not.
        """
        self.assertEqual(response.status_code, 200)

    """
    This function will test
    if the create user in
    admin page is rendered
    properly or not.
    """
    def test_create_user_page(self):
        url = reverse(
            'admin:core_user_add'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
