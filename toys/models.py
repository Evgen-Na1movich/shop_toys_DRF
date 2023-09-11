from django.db import models


class Brend(models.Model):
    brend = models.CharField(max_length=30, )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brend


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class Toy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Игрушка')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.PositiveIntegerField()
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True, related_name='toys_by_brend')
    # у бренда может быть много игрушек
    # устанавливает NULL при удалении связоной строки в главной таблице. Удалив бренд, у игрушки будет Null
    categories = models.ManyToManyField(Category, null=True, blank=True, related_name='cats')
    gender = models.CharField(max_length=50)
    discription = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Игрушки'


    def __str__(self):
        return self.name
