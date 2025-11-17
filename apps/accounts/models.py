from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) :
    USER_TYPE_CHOICES = {
        ('student', 'Student'),
        ('company', 'Company'),
    }

    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
