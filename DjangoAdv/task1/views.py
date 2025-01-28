from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game
from .forms import UserRegister

# Create your views here.

data = {
    'games':
        ['The Witcher 3: Wild Hunt', 'Grand Theft Auto V', 'The Elder Scrolls V: Skyrim']
        }


def get_buyers(request):
    buyers = Buyer.objects.all()
    return render(request, 'first_task/buyers.html', {'buyers': buyers})


def shop(request):
    data = Game.objects.all()
    return render(request, 'first_task/shop.html', {'data': data})


def sign_up_by_django(request):
    info = {}
    users = [user.name for user in Buyer.objects.all()]
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            balance = form.cleaned_data['balance']

            if username in users:
                info['error'] = 'Пользователь с таким логином уже существует'
                print('Пользователь с таким логином уже существует')
            else:
                Buyer.objects.create(name=username, age=age, balance=balance)
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['form'] = form
    else:
        info['form'] = UserRegister()

    return render(request, 'first_task/registration_page.html', info)
