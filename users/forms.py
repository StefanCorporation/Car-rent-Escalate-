from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm, UserCreationForm)
from django.contrib.auth import get_user_model


from users.models import Users



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model() # base user model
        fields = ['username', 'password']



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model() # base user model
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'first name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'last name'
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'choose a new image'
    }), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'        
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'email', 
        'readonly': True
    }))
 

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'image', 'username', 'email']
    