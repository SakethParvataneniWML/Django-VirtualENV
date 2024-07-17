from django.shortcuts import render
from .models import Author, Post

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})

# New root view
def home(request):
    return render(request, 'home.html')
