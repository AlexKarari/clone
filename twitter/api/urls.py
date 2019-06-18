from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

#Class based views url
urlpatterns = [
    # url('^$', RedirectView.as_view(url="/")),
    url('^$', views.TweetListAPIView.as_view(), name='APItweetList'),
    # url(r'^(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name='singleTweet'),
    # url('^create_tweet/', views.TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update/$', views.TweetUpdateView.as_view(), name='editTweet'),
    # url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name='deleteTweet'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
