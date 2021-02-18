from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
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
                choose=data['choose'],
            )
            return redirect(reverse('submit_post'))

    form = AddPostForm()
    return render(
        request,
        'post_view.html',{
        'heading': 'Post a Boast or a Roast',
        'form': form},
    )


def like(request, post_id):
    post = PostItem.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return redirect('/')


def dislike(request, post_id):
    post = PostItem.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()

    return redirect('/')


def score_view(request):
    posts = sorted(PostItem.objects.all(), key= lambda x: x.score())[::-1]

    return render(request, 'score_view.html', {
        'heading': 'Four Score.....',
        'posts': posts
    })


def boast_view(request):
    posts = PostItem.objects.filter(choose=True).order_by('time_created').reverse()

    return render(request, 'boast_view.html', {
        'heading': 'Four Score.....',
        'posts': posts
    })


def roast_view(request):
    posts = PostItem.objects.filter(choose=False).order_by('time_created').reverse()

    return render(request, 'roast_view.html', {
        'heading': 'Four Score.....',
        'posts': posts
    })