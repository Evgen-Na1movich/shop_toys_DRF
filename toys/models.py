from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Brend(models.Model):
    """Бренд."""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория."""
    name = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class GenderChoices(models.TextChoices):
    M = 'Для мальчиков'
    W = 'Для девочек'
    MW = 'Для мальчиков и девочек'


class Toy(models.Model):
    """Игрушка."""
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    count = models.PositiveIntegerField(verbose_name='Количество')
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE, related_name='toys_by_brend', verbose_name='Бренд')
    categories = models.ManyToManyField(Category, related_name='toys_by_category', verbose_name='Катерогия')
    gender = models.TextField(
        choices=GenderChoices.choices,
        default=GenderChoices.MW,
        verbose_name='Для кого',
    )
    discription = models.TextField(blank=True, null=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Игрушки'

    def __str__(self):
        return self.name


class OrderStatusChoices(models.TextChoices):
    """Статусы заказа."""

    NEW = "Новый"
    IN_PROGRESS = "В процессе"
    DONE = "Закрыт"


class Order(models.Model):
    """Заказ."""
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(Toy, through='Item')
    status = models.TextField(
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NEW
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    total_items = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = sum(item.get_cost() for item in self.positions.all())
        self.total_items = sum(item.quantity for item in self.positions.all())
        super(Order, self).save(*args, **kwargs)


class Item(models.Model):
    """Позиция."""
    product = models.ForeignKey(Toy, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.product.name

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.product.price
        super(Item, self).save(*args, **kwargs)


