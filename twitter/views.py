from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from .mixins import FormUserNeededMixin
from django.views.generic import DetailView, ListView, CreateView

# Create your views here.

#Function below GETS the template index.
def index (request):
    return render(request, 'all/index.html')

# C.R.U.D (Create, Retrieve, Update, Delete. List & Search also apply here) tweets

# _____________________Funtion based views below_____________________________
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

# Function below creates a Tweet
# def tweet_create_view(request):
#     form = TweetForm(request.POST or None):
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#         context = {
#             "form":form
#         }
#         return render(request, 'all/index.html', context)


# ___________________________Class based views below________________________________
# C.R.U.D (Create, Retrieve, Update, Delete. List & Search also apply here) tweets
#class based view to retrieve a tweet 
 
class TweetDetailView(DetailView):
    template_name = "all/individual_tweet.html"
    queryset = Tweet.objects.all()
    
    def get_object(self):
        # print = (self.kwargs)
        pk = self.kwargs.get("pk")
        print = (pk)
        return Tweet.objects.get(id=pk) 

class TweetListView(ListView):
    template_name = 'all/tweet_list.html'
    queryset = Tweet.objects.all()


class TweetCreateView(FormUserNeededMixin, CreateView):
    template_name = 'all/create_tweet.html'
    form_class = TweetForm
    success_url = "/create_tweet/"
    
