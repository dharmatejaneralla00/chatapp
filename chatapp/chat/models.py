from django.db import models

# Create your models here.
class roomid(models.Model):
    roomid = models.CharField(max_length=255)
    user1 = models.CharField(max_length=255)
    user2 = models.CharField(max_length=255)
    def __str__(self):
        return self.roomid

class message(models.Model):
    roomid = models.CharField(max_length=255)
    msg = models.TextField()
    user = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.roomid