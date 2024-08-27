from django.db import models
import datetime


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatars/')
    created_at = models.DateTimeField(auto_now=True)
    token = models.TextField(default='')
    suc = models.IntegerField(default=0)
    update_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    avatar = models.ImageField(upload_to='chat_avatar/',default=None)
    users = models.ManyToManyField(User, related_name='Users')
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
