from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def portfoylo(request):
    if request.user.is_authenticated == False:
        return redirect("portfoylo2")
        messages.error(request,"Projelere Erişmek İçin Lütfen Giriş Yapınız")
        
    else:

        articles = Article.objects.filter(author=request.user)
        context = {
            "articles":articles,
        }
    
    return render(request,"portfoylo.html",context)
    

def contact(request):
    return render(request,"contact.html")

def portfoylo2(request):
    return render(request,"portfoylo2.html")