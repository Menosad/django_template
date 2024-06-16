from django.db import models


NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="категория",)
    avatar = models.ImageField(upload_to='investments', **NULLABLE, width_field=100, height_field=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Investment(models.Model):
    name = models.CharField(max_length=100, verbose_name="бумага")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="категория"
    )
    price = models.PositiveIntegerField(verbose_name="цена")
    quantity = models.PositiveIntegerField(verbose_name="количество")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'инвестиция'
        verbose_name_plural = 'инвестиции'
        ordering = ('price',)
