# Generated by Django 4.1.1 on 2022-09-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
        ),
    ]
