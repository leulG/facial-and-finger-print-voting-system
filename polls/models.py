from django.db import models

# Create your models here.
from acount.models import Account


class Polle(models.Model):
    thumb = models.ImageField(upload_to = 'thumbnail/image' , null = True , blank =True)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    voters = models.ManyToManyField(Account, default = None)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name

class Party(models.Model):
    polle = models.ForeignKey(Polle , on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/image' , null = False , blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name




        