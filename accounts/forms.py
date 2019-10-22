from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name') 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')


# 장고는 User 관련 기능이 내부적으로 있어서 가져다 쓰면 됌
# django.contrib.auth.models.User 변경할 상황이 있으면
    # 상속을 받아 내가 만들 수 있음
    # DB와 연결되어 있어 나중에 다 바꿔줘야함
    # 프로젝트 만들면서 미리하는 게 좋음
    # 바꿨을 때 장고 내부에서 바뀐것을 확인하기 위해 -> settings 설정의 AUTH_USER_MODEL
    # User 클래스를 어떻게 가져다 쓰는지 확인하기 위히 -> get_user_model() :settings 설정 확인

# models.py에서도 get_user_model() 사용 할 수 있을까?
    # 아닐 수 있다. 장고가 명령어를 수행할 때, INSTALLED_APPS -> models /apps
    # User 클래스가 아직 없을 수 있음 (이름)
    # 그 땐 그냥 settings.AUTH_USER_MODEL로 문자열을 찍어놓으면 알아서 바꿔줌
    
# 근데 왜 갑자기 UserCreationForm 사용 못함?
    # User를 그대로 import해서 써서 안됌! (from django.contrib.auth.models import User)
    # get_user_model()로 써야함!
    # 상속을 받아서 덮어써야한다!

# 정리 
    # 프로젝트 시작하면 User 모델 빼자
    # User 클래스가 필요하면, get_user_model() 호출해서 쓰자
    # models.py에서만 settings.AUTH_USER_MODEL 쓰자