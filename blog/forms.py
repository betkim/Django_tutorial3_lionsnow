from django import forms
from .models import Post , Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields=['name']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form=control',
                'placeholder':'카테고리명을 입력하세요'          #gpt 검색창에 입력하라고 적힌표시 우리가 글씨쓰면사라짐
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','category','content']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form=control',
                'placeholder':'카테고리명을 입력하세요' 
            }),
            # 'category':forms.Select(attrs={
            #     'class':'form-control',
            #     'row':10,
            #     'placeholder':'내용을 입력하세요'
            # }) ,
            'content':forms.TextInput(attrs={
                'class':'form-control',
                'rows':10,
                'placeholder':'내용을 입력하세요'
            })
        }