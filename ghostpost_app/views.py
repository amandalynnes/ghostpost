from django.shortcuts import render, redirect, reverse
from ghostpost_app.models import PostItem
from ghostpost_app.forms import AddPostForm


# Create your views here.


def index_view(request):
    posts = PostItem.objects.all().order_by('time_created')

    return render(request, 'index.html', {
        'heading': 'Roasts & Boasts',
        'posts': posts
    })


def post_view(request):
    
    form = AddPostForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        PostItem.objects.create(
            text=data['text'],
            likes=data['likes'],
            dislikes=data['dislikes'],
            time_created=data['time_created'],
            toast_roast=data['toast_roast']
        )
        return redirect(reverse('submit_post'))

    form = AddPostForm()
    return render(
        request,
        'post_view.html',{
        'heading': 'Post a Boast or a Roast',
        'form': form},
    )

    # return render(request, 'post_view.html', {
    #     'heading': 'Post a Boast...or a Roast',
    #     'text': text, 
    #     'likes': likes,
    #     'dislikes': dislikes,
    #     'time_created': time_created,
    #     'toast': toast,
    #     'roast': roast,
    #     })