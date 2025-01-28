from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game, News
from .forms import UserRegister


def news(request):
    contents = News.objects.all()
    paginator = Paginator(contents, 2)
    page_number = request.GET.get('page')
    try:
        page_contents = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_contents = paginator.page(1)
    except EmptyPage:
        page_contents = paginator.page(paginator.num_pages)
    return render(request, 'first_task/news.html', {'page_contents': page_contents})


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
