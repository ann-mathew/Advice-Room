from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets

def get_code():
  return secrets.token_hex(3).upper()

#Create your models here.

class User(AbstractUser):
    user_id = models.CharField(max_length=6, primary_key=True, default=get_code, editable=False)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_id


  
