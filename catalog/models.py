from django.db import models


# Объявление словаря NULLABLE
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='цена за единицу товара')
    date_of_creation = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
