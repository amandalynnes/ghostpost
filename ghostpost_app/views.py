from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from ghostpost_app.models import PostItem
from ghostpost_app.forms import AddPostForm


# Create your views here.


def index_view(request):
    posts = PostItem.objects.all().order_by('time_created').reverse()

    return render(request, 'index.html', {
        'heading': 'Roasts & Boasts',
        'posts': posts
    })


def post_view(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PostItem.objects.create(
                text=data['text'],
                toast_roast=data['toast_roast'],
            )
            return redirect(reverse('submit_post'))

    form = AddPostForm()
    return render(
        request,
        'post_view.html',{
        'heading': 'Post a Boast or a Roast',
        'form': form},
    )


def like_view(request, post_id):
    post = PostItem.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return redirect('/')


def dislike_view(request, post_id):
    post = PostItem.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return redirect('/')

def score_view(request, post_id):
    post = PostItem.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return redirect(reverse('homepage', args=['score']))