- **_ДЗ. QuerySet запросы в базу данных (app task1)_**

При помощи QuerySet запросов необходимо создать 3 записи Buyer и 3 записи Game в вашу базу данных.
Все значения для полей этих записей выберите самостоятельно со следующими условиями:
Только один Buyer должен быть младше 18. (age)
Только одна Game должна быть без ограничения возраста. (age_limited)

После создания всех объектов свяжите их полем buyer у записей Game. 
Просто присвоить значение при создании объектов не получится. 
Для присвоения используйте метод set(objects), который принимает коллекцию объектов, например:
Game.objects.get(id=1).buyer.set((first_buyer, second_buyer)) - здесь игра c id=1 приобретается покупателями first_buyer и second_buyer.
При назначении покупателей для игр соблюсти следующие правила:
Только один из Buyer должен обладать всеми Game.
Buyer с возрастом меньше 18 не выдавать игры с ограничением по возрасту.

создание записи
```python
from task1.models import Buyer
from task1.models import Game
 
Buyer.objects.create(name="Maloi", balance='100.00', age=15)

Game.objects.create(title='Terminator', cost=50, size=25, description='Action', age_limited='True')
```

свяжите их полем buyer у записей Game
```python
first = Buyer.objects.get(age=22)
second = Buyer.objects.get(age=25)
third = Buyer.objects.get(age=15)
Buyer.objects.all()

Game.objects.all()
Game.objects.get(id=1).buyer.set((first, second))
Game.objects.get(id=2).buyer.set((first,))
Game.objects.get(id=3).buyer.set((first, second, third))

```

После создания и подключения БД в Postgresql делаю запросы:

python manage.py shell

from .models import Postcode
```python
from task1.models import Postcode
Postcode.objects.create(id=2, postcode=600302, city='Nnovgorod', street='rai', house=3, flat=5)
Postcode.objects.create(id=1, postcode=600300, city='Ganduras', street='Oboima', house=3, flat=5)
 
alls_post = Postcode.objects.all()
print(alls_post)

from task1.models import News      
news = News.objects.all()
print(news)

>>> news1 = News.objects.get(id=1)       
>>> print(news1)

>>> b1 = Buyer.objects.filter(age=25) 
>>> print(b1)

Агрегатные функции
print(len(news))

```