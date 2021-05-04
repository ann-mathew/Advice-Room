from django.db import models
import secrets

def get_code():
  return secrets.token_hex(3).upper()

#Create your models here.

class Advisor(models.Model):
    advisor_id = models.CharField(max_length=6, primary_key=True, default=get_code, editable=False)
    name = models.CharField(max_length=32)
    photo_url =  models.URLField(max_length=1000)

    def __str__(self):
        return self.advisor_id



  