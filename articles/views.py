# from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
# from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
# 중간에 embed를 사용하면 ipython을 이용하여 중간 값을 확인할 수 있다.
# from IPython import embed

from django.contrib.auth import get_user_model
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

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

@login_required
def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        article_form = ArticleForm(request.POST, request.FILES)
        # embed()
        # 검증에 성공하면 저장하고, (검사에서 max_length를 바꾸고 입력할 수 있어서)
        if article_form.is_valid():
            # title = article_form.cleaned_data.get('title')
            # content = article_form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            # context = {
            #     'article': article
            # }
            # redirect
            return redirect('articles:detail', article.pk)
        # else:
            # 다시 폼으로 돌아가 -> 중복되서 제거
    else:
    # GET 요청 -> Form
        article_form = ArticleForm()
    # GET -> 비어있는 Form context
    # POST -> 검증 실패시 에러메시지와 입력값 채워진 Form context
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # 해당 url이 없을 때 500 error가 아닌 404  error가 뜨도록
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    commnet_form = CommentForm()
    context = {
        'article': article, 
        'comments': comments,
        'comment_form': commnet_form
    }
    return render(request, 'articles/detail.html', context)

@require_POST
# require_POST를 사용하면 if문을 사용하지 않아도 됌
def delete(request, article_pk):
    if article.user == request.user:
        article = Article.objects.get(pk=article_pk)
        # if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
        # else:
        #     return redirect('articles:detail', article.pk)
    else:
        raise PermissionDenied


# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.user == request.user:
        if request.method == 'POST':
            # instance값을 줘서 수정가능하도록
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                # content = article_form.cleaned_data.get('content')
                # article.content = content
                # article.save()
                article.image = request.FILES.get('image')
                article = article_form.save()
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/form.html', context)
    else:
        raise PermissionDenied

@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 1. modelform에 사용자 입력값 넣고
    comment_form = CommentForm(request.POST)
    # 2. 검증하고, 
    if comment_form.is_valid():
        # 3. 맞으면 저장
        # 3-1. 사용자 입력값으로 comment instance 생성(저장은 X)
        # 그냥 저장하면 Not null constraint 오류 발생 (FK가 없어서)
        comment = comment_form.save(commit=False)
        # 3-2. FK 넣고 저장
        comment.article = article
        comment.user = request.user
        comment.save()
        messages.success(request, '댓글이 생성되었습니다.')
    else:
        messages.success(request, '댓글 형식이 맞지 않습니다.')
    # 4. return redirect
    return redirect('articles:detail', article_pk)
    # comment = Comment.objects.create(content=request.POST.get('comment'), article_id = article_pk)
    # messages.success(request, '댓글이 생성되었습니다.')
    # return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, '댓글이 삭제되었습니다.')
        return redirect('articles:detail', article_pk)
    else:
        # raise PermissionDenied 
        return HttpResponseForbidden()