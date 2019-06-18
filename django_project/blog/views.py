from django.shortcuts import render

posts = [
        {'title':"Don't forget, a person's greatest emotional need is to feel appreciated.",
        'date_posted': 'August 27, 2018',
        'author': 'user#2018'
        }
    ,
    
       {'title':"Our core emotional need is to feel valued.",
        'date_posted': 'August 27, 2017',
        'author':'user#2017'
       }
]


def home(request):
    context = {
        'posts': posts 
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def register(request):
    return render(request, 'blog/register.html', {'title': 'Register'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

