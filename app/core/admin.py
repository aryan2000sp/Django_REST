from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _

"""
This class we have extend
the default UserAdmin class
by ordering the users according
to their ids
"""


class UserAdmin(BaseUserAdmin):
    """
    This will order the users
    according to their ids
    """
    ordering = ['id']

    """
    This will display the users
    name and email
    """
    list_display = ['name', 'email']

    """
    Now we customize the admin
    page for user change page.
    This will include the changing
    the fields. _ will mark
    which fields are translated
    into language prefered by the
    user. We basically add field
    sets which will contain fields.
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal_Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important_Dates'), {'fields': ('last_login',)}),
    )

    """
    You need to add your
    custom fields to fieldsets
    for fields to be used in
    editing users and to
    add_fieldsets for fields
    to be used when creating a user.
    The classes key sets any
    custom CSS classes we want
    to apply to the form section.
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        }),
    )


"""
Finally we want to
register the user
model to admin site
in order to show the
table admin users.
"""
admin.site.register(models.User, UserAdmin)
