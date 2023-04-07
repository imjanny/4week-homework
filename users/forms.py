from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        print("폼데이터", cleaned_data)
        return cleaned_data
            
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']