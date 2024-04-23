from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm, UserCreationForm,)
from django.contrib.auth import get_user_model


from users.models import Users, RentData, PaymentData



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
    




class RentDataForm(forms.ModelForm):   
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    pick_up_location = forms.ChoiceField(
        choices=[('tbilisi', 'Tbilisi'), ('batumi', 'Batumi'), ('kutaisi', 'Kutaisi')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    leave_car_location = forms.ChoiceField(
        choices=[('tbilisi', 'Tbilisi'), ('batumi', 'Batumi'), ('kutaisi', 'Kutaisi')],
        widget=forms.Select(attrs={'class': 'form-control'})           
    )

    pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
        'id': 'pick_up_time',
        'name': 'pick_up_time',
    }))

    return_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
        'id': 'return_time',
        'name': 'return_time',     
    }))
    
    pick_up_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'id': 'date',
        'name': 'date',
        'style': 'width: 200px; height: 25px; padding: 5px;'
    }))

    car_return_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'id': 'date',
        'name': 'date',
        'style': 'width: 200px; height: 25px; padding: 5px;'
    }))


    class Meta:
        model = RentData
        fields = [
            'username', 'email', 'first_name', 'last_name', 'phone', 'pick_up_location', 
            'leave_car_location', 'pick_up_time', 'return_time', 'pick_up_date', 'car_return_date', 
        ]



class PaymentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'placeholder': 'Name',
        'size': '15'
    }))

    card_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'text',
        'name': 'card-num',
        'placeholder': '0000 0000 0000 0000',
        'size': '18', 
        'id': 'cr_no',
        'minlength': '19', 
        'maxlength': '19'
    }))

    expiry_date = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'text',
        'name': 'exp',
        'placeholder': 'MM/YY', 
        'size': '6',
        'id': 'exp',
        'minlength': '5', 
        'maxlength': '5'
    }))

    cvv_cvc = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'password',
        'name': 'cvv', 
        'placeholder': '000',
        'size': '1', 
        'minlength': '3',
        'maxlength': '3'
    }))

    class Meta:
        model = PaymentData
        fields = ['name', 'card_number', 'expry_date', 'cvv_cvc']