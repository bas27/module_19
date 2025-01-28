from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Логин")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс")
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Баланс: {self.balance}\n'
                f'Возраст: {self.age}')

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер")
    description = models.TextField(verbose_name="Описание")
    age_limited = models.BooleanField(default=False, verbose_name="Возрастное ограничение")
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return (f'Название: {self.title}\n'
                f'Цена: {self.cost}\n'
                f'Размер: {self.size}\n'
                f'Описание: {self.description}\n'
                f'Возрастной рейтинг: {self.age_limited}')

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Статья")
    date = models.DateField(auto_now_add=True, verbose_name="Дата статьи")

    def __str__(self):
        return (f'Заголовок: {self.title}\n'
                f'Дата: {self.date}')

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"