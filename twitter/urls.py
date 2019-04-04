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
    url(r'^(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name='singleTweet'),
    url('^users_tweets/', views.TweetListView.as_view(), name='usersTweets'),
    url('^create_tweet/', views.TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', views.TweetUpdateView.as_view(), name='editTweet'),
    url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name='deleteTweet'),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
