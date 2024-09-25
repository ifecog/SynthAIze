import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Synthesist', 'Synthesist'),
        ('Observer', 'Observer')
    ]
    
    username = None    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
    def save(self, *args, **kwargs):
        if self.role == 'Synthesist' and not self.bio:
            raise ValueError('A bio is required for Synthesists.')
        
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f'{self.email}'
