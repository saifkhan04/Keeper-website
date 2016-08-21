from django.contrib.auth.models import Permission, User
from django.db import models

ACCOUNT_CHOICES = (
    ('SKYPE', 'SKYPE'),
    ('FACEBOOK', 'FACEBOOK'),
    ('GMAIL','GMAIL')
)


class Album(models.Model):


    user = models.ForeignKey(User, default=1)
    account_type = models.CharField(max_length=250,choices=ACCOUNT_CHOICES,default='--choose--')
    account_name = models.CharField(max_length=250)
    account_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.account_type + ' - ' + self.account_name


class Song(models.Model):
    account = models.ForeignKey(Album, on_delete=models.CASCADE)
    username = models.CharField(max_length=15,default='username')
    password = models.CharField(max_length=50,default='pass')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.username
