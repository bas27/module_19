from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Баланс: {self.balance}\n'
                f'Возраст: {self.age}')


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return (f'Название: {self.title}\n'
                f'Цена: {self.cost}\n'
                f'Размер: {self.size}\n'
                f'Описание: {self.description}\n'
                f'Возрастной рейтинг: {self.age_limited}')