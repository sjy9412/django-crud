# ForeignKey

```python
# Reporter(1) - Article(N)
# reporter - name

class Reporter(models.Model):
    name = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
# Article(1) - Comment(N)
# comment - content
class Comment(models.Model):
    content = models.CharField(max_length=10)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



1. '홍길동' 이름 가진 reporter1 생성 (방법1)

   ```python
   reporter1 = Reporter()
   reporter1.name = '홍길동'
   reporter1.save()
   ```
   
2. '철수' 이름을 가진 reporter2 생성(방법2)

   ```python
reporter2 = REpoter.objects.create(name='철수')
   ```

3. reporter1의 article1 추가 (오브젝트를 통해서)

   ```python
   article.reporter = reporter1
   article.save()
   ```

5. reporter2의 article3 추가(id값을 통해서)

   ```python
   article3 = Article.objects.create(title='제목', content= '내용', reporter_id = 2)
   ```

   ```python
   article3 = Article.objects.create(title='제목', content= '내용', reporter_id = reporter2)
   ```

5. 각 reporter의 article들 조회

   ```python
   Article.objects.fillter(reporter_id=1)
   # fillter보다 set all을 사용하는게 나음
   reporter1.article_set.all()
   article3
   article3.reporter
   article3.reporter_id
   ```

6. article1에 댓글 두 개 추가

    ```python
    comment1 = Comment()
    comment1.content = '댓글1'
    comment1.article_id = 1
    # 또는 comment1.article = article
    comment1.save()
    ```

    ```python
    comment2 = Comment.objects.create(contetn='댓글2', article_id = 1)
    ```

7. comment2의 기사를 작성한 기자

    ```python
    comment2.article.reporter
    ```

8. 기사별 댓글 내용 출력

    ```python
    articles = Article.objects.all()
    for article in articles:
        for comment in article.comment_set.all():
            print(comment.content)
    ```

9. 기자별 기사 내용 출력

    ```python
    reporters = Reporter.objects.all()
    for reporter in reporters:
        print(reporter.name)
        for article in reporter.article_set.all():
            print(article.content) 
    ```

10. reporter1의 기사 갯수

    ```python
    reporter1.article_set.count()
    ```

    