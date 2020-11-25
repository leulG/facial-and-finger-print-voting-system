
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key=True)
    profile_pic = models.ImageField(upload_to="profile/Image" , null=False , blank=False)
    adress = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Account.objects.get_or_create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


# Create your models here.
