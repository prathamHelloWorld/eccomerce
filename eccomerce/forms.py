from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class AboutForm(forms.Form):
    name=forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(widget=forms.EmailInput, required=True)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        emailCheck=User.objects.filter(email=email)
        if emailCheck:
            raise forms.ValidationError('email already taken')
        else:
            return email
            
    def clean_username(self):
        username=self.cleaned_data.get('username')
        userCheck=User.objects.filter(username=username)
        if userCheck:
            raise forms.ValidationError('username already taken')
        else:
            return username
