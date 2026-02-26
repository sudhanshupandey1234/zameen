from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="username")
    phone=forms.IntegerField(label="phone")
    password=forms.CharField(widget=forms.PasswordInput)

class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

