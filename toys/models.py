from django.conf import settings
from django.db import models


class Brend(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Toy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Игрушка')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.PositiveIntegerField()
    # у бренда может быть много игрушек
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE, null=True, related_name='toys_by_brend')
    # Связь будет описана через вспомогательную модель ToyBYCategory
    categories = models.ManyToManyField(Category, related_name='toys_by_category')
    # categories = models.ManyToManyField(Category, on_delete=models.CASCADE)

    gender = models.CharField(max_length=50)
    discription = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Игрушки'

    def __str__(self):
        return self.name


# В этой модели будут связаны id игрушки и id его категории
class ToyCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    date = models.DateField()  # дата поступления игрушки в магазин

    def __str__(self):
        return f'{self.toy}, {self.category}'


class Order(models.Model):
    """Заказ."""
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

