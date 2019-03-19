from django.db import models
from django.conf import settings #Setting foreign key with specific user

# Create your models here.

class Tweet(models.Model):
    User = models.ForeignKey('self', default=1)
    content     = models.CharField(max_length=140)
    updated     = models.DateTimeField(auto_now =True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
 
