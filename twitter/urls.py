from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Function based views
# urlpatterns = [
#     url('^$', views.index, name='homepage'),
#     url('^posted_tweet/', views.view_tweet, name='singleTweet'),
#     url('^users_tweets/', views.tweet_list, name='usersTweets'),

# ]


#Class based views url
urlpatterns = [
    url('^$', views.index, name='homepage'),
    url('^posted_tweet/', views.TweetDetailView, name='singleTweet'),
    url('^users_tweets/', views.TweetListView, name='usersTweets'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
