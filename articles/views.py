from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
# 중간에 embed를 사용하면 ipython을 이용하여 중간 값을 확인할 수 있다.
# from IPython import embed

from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    # embed()
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        # context = {
        #     'article': article
        # }
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {
        'article': article, 
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
# require_POST를 사용하면 if문을 사용하지 않아도 됌
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)


# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
        'article': article
        }
        return render(request, 'articles/edit.html', context)

@require_POST
def comment_create(request, article_pk):
    comment = Comment.objects.create(content=request.POST.get('comment'), article_id = article_pk)
    messages.success(request, '댓글이 생성되었습니다.')
    return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('articles:detail', article_pk)