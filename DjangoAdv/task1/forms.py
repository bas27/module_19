from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30,)
    age = forms.IntegerField(label='Введите свой возраст', min_value=0, max_value=120)
    balance = forms.IntegerField(label='Введите свой баланс', min_value=0)
