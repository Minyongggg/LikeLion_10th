from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)	
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

