from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Tweet

from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='users/accounts/login/')
def tweet_list(request):
    return render(request, 'home.html', {'object_list': Tweet.objects.all()})

def tweet_new(request):
    user=None
    if request.user:
        user=request.user 
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TweetForm

    return render(request, 'tweet_new.html', {'form': form, 'user':user})

    
class TweetListView(ListView):
    model = Tweet
    template_name = 'home.html'

class TweetCreateView(CreateView):
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')
