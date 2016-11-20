from django import forms
from django.contrib.auth.models import User
from .models import Blog

class Blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[
            "标题",
            "内容",
            "图片"
        ]


class User_form(forms.ModelForm):

    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password"
        ]


class User_login_form(forms.ModelForm):

    class Meta:
        model=User
        fields=[
            "username",
            "password"
        ]