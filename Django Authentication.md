# Django Authentication

## 1. `User` Class

> django에서는 프로젝트를 시작할 때, 항상 `User` Class를 직접 만드는 것을 추천함. [링크]()
>
> django의 기본 Authentication과 관련된 설정 값들은 `accounts` url로 설정되어 있음 (ex. LOGIN_URL = '/accounts/login')

1. models.py

   ```python
   # accounts/models.py
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstactUser):
       pass
   ```

   * django 내부에서 `User`를 기본적으로 사용한다. ex) `python manage.py createsuperuser`
   * 확장 가능성(변경)을 위해 내가 원하는 앱에 class를 정의
   * `User` 상속 관계 [Github 링크]() [공식문서 링크]()
     * `AbstactUser` : `Username`, `last_name`, `first_name`, `email`, ...
     * `AbstractBaseUser` : `password`, `last_login` 
     * `models.Model`

2. `settings.py`

   ```python
   # project/settings.py
   
   AUTH_USER_MODEL = 'accounts.User'
   ```

   * `User` 클래스를 활요하는 경우에는 `get_user_model()`을 함수를 호출하여 사용

     ```python
     # accounts/forms.py
     from django.contrib.auth import get_user_model
     
     class CustomUserCreationFrom(UserCreationForm):
         class Meta:
             model = get_user_model()
     ```

   * 단, `models.py`에서 사요하는 경우에는 `settings.AUTH_USER_MODEL`을 활용

     ```python
     # articles/models.py
     from django.conf import settings
     class Article(modes.Model):
         user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
     ```

3.  `admin.py`

   * admin 페이지를 활용하기 위해서는 직접 자성을 해야한다.

   * `UserAdmin` 설정을 그대로 활요할 수 있다.

     ```python
     # accounts/admin.py
     from django.contrib.auth.admin import UserAdmin
     from .models import User
     
     admin.site.register(User, UserAdmin)
     ```

     

## 2. Authentication Forms

### 1. `UserCreationForm` (ModelForm)

* custom user를 사용하는 경우 직접 사용할 수 없음
  * 실제 코드 상에 `User`가 직접 import되어 있기 때문

```python
# accounts/forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields =  ('username',)
```

* `ModelForm`이므로 활용 방법은 동일

### 2. `UserChangeForm`(ModelForm)

* custom user를 사용하는 경우 직접 사용할 수 없음
* 그대로 활요하는 경우 `User`와 관련된 모든 내용을 수정
  * 실제 코드 상에 필드가 `__all__`로 설정되어 있음 [Github 링크]()()

```python
# accounts/form
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields =  ('username', 'first_name', ///)
```

### 3. `AuthenticationForm`

* `ModelForm`이 아님!!  **인자 순서를 반드시 기억하자!!!**
* `AuthenticationForm(request, data, ...)`

```python
if request.method == 'POST':
    form = AuthenticationForm(request, request.POST) # 모델 form이 아님
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect(request.GET.get('next') or 'articles:index')
```

* 로그인에 성공한 `user`의 인스턴스는 `get_user` 메소드를 호출하여 사용한다.

* 실제 로그인은 아래의 함수를 호출해야 한다.

  ```python
  from django.contrib.auth import login as auth_login
  auth_login(request, user)
  ```

### 4. `PasswordChangeForm`

* `ModelForm`이 아님!!  **인자 순서를 반드시 기억하자!!!**

* `PasswordChangeForm(user, data)` ***model이 아니기 때문에 instance를 받을 수 없음***

  ```python
  if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.date)
  else:
      form = PasswordChangeForm(request.user)
  ```

* 비밀번호가 변경 완료된 이후에는 기존 세션 인증 내역이 바뀌어서 자동으로 로그아웃된다. 아래의 함수를 호출하면, 변경된 비밀번호로 세션 내역을 업데이트 한다.

  ```python
  from django.contrib.auth import update_session_auth_hash
  update_session_auth_hash(request, form.user)
  ```



# Appendix.import

```python
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstactUser
from django.contrib.auth.models import AbstactBaseUSer
from django.contrib.auth.decorators import login_required
```

```python
from django.conf import settings
```

```python
from django.db import models # models.Model, models.CharField() ...
from django import forms # forms.ModelForm, forms.Form
```

```python
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
```

