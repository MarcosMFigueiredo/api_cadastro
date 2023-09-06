from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 11)

    def __str__(self):
        return self.username
    
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users'  
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users'  
    )
