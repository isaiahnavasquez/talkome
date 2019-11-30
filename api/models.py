from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sender.username + '>' + self.recipient.username + ' : "' + self.content + '"'