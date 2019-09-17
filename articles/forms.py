from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 첫번째 방법
    # title = forms.CharField(
    #     max_length=10, 
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '제목을 입력바랍니다.'
    #         }
    #     )
    # )
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title')
        # exclude = ('title')
        # 두번째 방법
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목을 입력바랍니다.'
                }
            )
        }

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '제목을 입력바랍니다.'
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         # Django form에서 HTML 속성 지정 -> widget
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': '내용을 입력바랍니다.', 
#                 'rows': 5, 
#                 'cols': 60
#             }
#         )
#     )