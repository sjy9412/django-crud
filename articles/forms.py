from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=10, 
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력바랍니다.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        # Django form에서 HTML 속성 지정 -> widget
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력바랍니다.', 
                'rows': 5, 
                'cols': 60
            }
        )
    )