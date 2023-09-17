from django.shortcuts import render
from django.http import HttpResponse

posts = [
   {
        'author': 'Charmoni Pi',
        'title': 'The Good Gil',
        'content': 'This is Alot',
        'date_posted': 'August 27, 2023',
   }, 
      {
        'author': 'Charmoni Pi2',
        'title': 'The Good Gil22',
        'content': 'This is Alo2222t',
        'date_posted': 'August 27, 2023',
   } 
]

# Create your views here.
def home(request):
    context ={
        'posts': posts    
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html') 