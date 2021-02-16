from django.shortcuts import render, redirect
from ghostpost_app.models import PostItem
from ghostpost_app.forms import AddPostForm


# Create your views here.


def index_view(request):
    posts = PostItem.objects.all().order_by('time_created')

    return render(request, 'index.html', {
        'heading': 'Roast & Boasts',
        'posts': posts
    })


def post_view(request):
    
    form  = AddPostForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        PostItem.objects.create(
            text=data['text'],
            likes=data['likes'],
            dislikes=data['dislikes'],
            time_created=data['time_created'],
            toast_roast=data['toast_roast']
        )
        form = AddPostForm()
        return render(request, 'post_view.html', {'text': text, 
            'likes': likes,
            'dislikes': dislikes,
            'time_created': time_created,
            'toast': toast,
            'roast': roast,

            })


    return redirect(request, 'post/', {'form': form})
