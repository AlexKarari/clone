from django.db import models
from django.conf import settings #Setting foreign key with specific user
from django.core.exceptions import ValidationError
from .validators import validate_content

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey('self', default=1)
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated     = models.DateTimeField(auto_now =True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)


# Setting Validations to models
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)
 
