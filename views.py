from django.shortcuts import render
posts=[
    {
     'author':'Ronglin',
      'title': 'blog post 1',
      'content':'First post content',
      'date_posted':'5/18/2022'

    },
]

# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html')
