from django.contrib import admin
from .models import Tweet
from .forms import TweetForm

# Register your models here.
# admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    form = TweetForm
    # class Meta:
    #     model = Tweet
    #     form = TweetForm

admin.site.register(Tweet, TweetModelAdmin)


