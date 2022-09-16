from django.db import models


class Item(models.Model):

    name = models.CharField('Название', max_length=300)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.name

