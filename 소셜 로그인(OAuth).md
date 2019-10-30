# 소셜 로그인(OAuth)

* 인증 체계
* OAuth 2.0 사용
* authentication(인증 - 로그인)
* authentizagion(인증 후)



### 카카오 등록하기

1. django-allauth 설치
2. settings.py 필요한 내용 추가
3. kakao에서 앱 등록 후 비밀 키 발급(고급 설정)
4. django/admin에서 소셜 어플리케이션 추가
   * REST API -> 클라이언트 아이디
   * Client Secret -> 비밀 키



### OAuth 처리 과정

> 토큰(access token)은 보통 유효기간이 있는데, refresh token을 통해서 토큰 재발급을 받을 수 있다.

1. 사용자가 카카오링크(/accounts/kakao/login/)

2. 사용자는 카카오 사이트 로그인 페이지를 확인

3. 사용자는 로그인 정보를 카카오로 보냄

4. 카카오는 redirect url로 django 서버로 사용자 토큰을 보냄

5. 해당 토큰을 이용하여 카카오에 인증 요청

6. 카카오에서 확인

7. 로그인

   ```
   카카오 - 리소스 서버/인증 서버
   사용자(리소스 owner) - 유저
   django - 클라이언트
   ```

   

   

