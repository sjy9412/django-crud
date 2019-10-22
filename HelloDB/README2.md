# SQL과 django ORM

## 기본 준비 사항

* https://bit.do/djangoorm에서 csv 파일 다운로드

* django app

  * `django_extensions` 설치

  * `users` app 생성

  * csv 파일에 맞춰 `models.py` 작성 및 migrate

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```

    

## 문제

> 아래의 문제들을 sql문과 대응되는 orm을 작성 하세요.

### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   print(User.objects.all().query)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm1
   User.objects.creat(first_name='이름', last_name='성', age='20', country='대전광역시', phone='010-1234-5678', balance='1234')
   
   # orm2
   user = User()
   user.first_name = '길동'
   ...
   user.save() # 반드시 저장!
   ```

   ```sql
   -- sql
   INSERT INTO users_user (first_name, last_name, age, country, phone, balance)
   VALUES ('길동', '홍', 20, '대전광역시', '010-9876-5432', '6789');
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

     ```python
     # orm 오류
     IntegrityError: NOT NULL constraint failed: users_user.age
     ```

     ```sql
     -- sql 오류
     NOT NULL constraint failed: users_user.age
     ```

     

3. 해당 user 레코드 조회

   ```python
   # orm
   user = User.objects.get(pk=1)
   user.phone # 값 불러오기
   ```

      ```sql
   -- sql
   SELECT * FROM users_user WHERE id=1;
      ```

4. 해당 user 레코드 수정

   ```python
   # orm
   user = User.objects.get(pk=1)
   user.phone = '010-5555-6666'
   user.save()
   ```

      ```sql
   -- sql
   UPDATE users_user SET age=25 WHERE id=1;
      ```

5. 해당 user 레코드 삭제

   ```python
   # orm1
   user.objects.get(pk=1).delete()
   # orm2
   user = User.objects.get(pk=1)
   user.delete() # delete에서는 save하지 않음!
   ```
   
      ```sql
   -- sql
   DELETE FROM users_user WHERE id=1;
      ```

### 조건에 따른 쿼리문

1. 전체 인원 수 

   ```python
   # orm
   User.objects.count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   # 결과
   # <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   print(User.objects.filter(age=30).values('first_name').query)
   # 결과
   # SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE age = 30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   > __gte : 이상
   >
   > __gt : 초과
   >
   > __lte : 이하
   >
   > __lt : 미만

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   # query는 queryset의 인스턴스 변수로 존재 (따라서 count().query 하면 오류남! -> count()는 값만 반환하므로)
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age >= 30;
   ```

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm1
   User.objects.filter(age__gte=30, last_name='김').count()
   # orm2
   User.objects.filter(age=30).filter(last_name='김').count() 
   # user = User.objects.filter(age=30)
   # user.filter(last_name='김') 
   # 이런 식으로 사용하지 말기! 한 번에 이어서!!
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age >= 30 AND last_name='김';
      ```

5. 지역번호가 02인 사람의 인원 수

   > sqlite에서 LIKE와 같은 역할
   >
   > exact, contains, startswith, endwith
   >
   > i -> case insensitive (대소문자 무시)
   >
   > iexact, icontains, istartswith, iendwith

   ```python
   # orm
   User.objects.filter(phone__startswiths='02-').count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   ```

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country='강원도', last_name='황').values('first_name')
   ```

      ```sql 
   -- sql
   SELECT first_name FROM users_user 
   WHERE country='강원도' AND last_name='황';
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명

   ```python
   # orm
   # 내림차순
   User.objects.order_by('-age').values('age')[:10]
   ```
   
   ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY age DESC LIMIT 10;
   ```


2. 잔액이 적은 사람 10명

   ```python
   # orm
   User.objects.order_by('balance').values('balance')[:10]
   ```

   ```sql
   -- sql
   SELECT balance FROM users_user 
   ORDER BY balance ASC LIMIT 10;
   ```


3. 성, 이름 내림차순 순으로 5번째 있는 사람

      ```python
   # orm
   User.objects.order_by('-last_name').order_by('-first_name').values()[4]
   ```

   ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
   ```



### 표현식

​	[django 참고 자료]( https://docs.djangoproject.com/en/2.2/topics/db/aggregation/ )

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   # {'age__avg': 28.23}
   ```

   ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
   ```

2. 김씨의 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

4. 계좌 잔액 총액

   ```python
   # orm
   from django.db.models import Sum
   User.objects.aggregate(Sum('balance'))
   ```

      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```
