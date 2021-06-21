from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Szymon Fraszak',
        'title': 'Post number one',
        'content': 'First post content',
        'date_posted': 'June 16, 2021'
    },
    {
        'author': 'Cristiano Ronaldo',
        'title': 'Post number two',
        'content': 'Second post content',
        'date_posted': 'June 29, 2021'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home Page'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})