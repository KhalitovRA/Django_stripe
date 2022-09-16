from django.db import models


class Item(models.Model):

    name = models.CharField('Название', max_length=300, help_text='Название Вашего товара')
    description = models.TextField('Описание', help_text='Описание Вашего товара')
    price = models.PositiveIntegerField('Цена', help_text='Указать сумму в центах')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
