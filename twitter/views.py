from django.shortcuts import render
from .models import Tweet

# Create your views here.

#Function below GETS the template index.
def index (request):
    return render(request, 'all/index.html')

# C.R.U.D (Create, Retrieve, Update, Delete. List & Search also apply here) tweets

# Function below RETREIEVES a tweet with a function based view
def view_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id) # Get tweet from Database
    context = {
        "object": tweet
    }
    return render(request, 'all/individual_tweet.html', context)

# Function below displays a list of tweets with a function based view
def tweet_list(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'all/tweet_list.html', context)
