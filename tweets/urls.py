from django.urls import path
#from .views import TweetListView, TweetCreateView
from tweets import views as tweets_views

urlpatterns = [
    #path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
    #path('', TweetListView.as_view(), name='home'),
    path('tweets/new/', tweets_views.tweet_new, name='tweet_new'),
    path('', tweets_views.tweet_list, name='home'),
]