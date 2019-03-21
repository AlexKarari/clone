from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView, ListView

# Create your views here.

#Function below GETS the template index.
def index (request):
    return render(request, 'all/index.html')

# C.R.U.D (Create, Retrieve, Update, Delete. List & Search also apply here) tweets

#Funtion based views below
# Function below RETREIEVES a tweet with a function based view
# def view_tweet(request, tweet_id):
#     tweet = Tweet.objects.get(id=tweet_id) # Get tweet from Database
#     context = {
#         "object": tweet
#     }
#     return render(request, 'all/individual_tweet.html', context)

# # Function below displays a list of tweets with a function based view
# def tweet_list(request):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, 'all/tweet_list.html', context)

#Class based views below
# C.R.U.D (Create, Retrieve, Update, Delete. List & Search also apply here) tweets
#class based view to retrieve a tweet 
 
class TweetDetailView(DetailView):
    template_name = "all/individual_tweet.html."
    queryset = Tweet.objects.all()
    
    def get_object(self, tweet_id):
        return Tweet.objects.get(id=tweet_id)

class TweetListView(ListView):
    template_name = 'all/tweet_list.html'
    queryset = Tweet.objects.all()

