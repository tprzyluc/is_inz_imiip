from django.db import models
from django.contrib.auth.models import UserManager
from django.utils import timezone
# Create your models here.


class Localization(models.Model):
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posX = models.FloatField()
    posY = models.FloatField()
    created_date = models.DateTimeField(default = timezone.now)


    def _init_(self, posX, posY):
        self.posX = posX
        self.posY = posY

    # def __str__(self):
    #     return u'%s %s %s %d' % (self.client, self.posX, self.posY, self.created_date)
