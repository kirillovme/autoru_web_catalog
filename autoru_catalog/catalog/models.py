from django.db import models


class Mark(models.Model):
    """Модель марки автомобиля."""

    name = models.CharField(max_length=128, verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'

    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    """Модель модели автомобиля."""

    name = models.CharField(max_length=128, verbose_name='Название')
    mark_id = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='models', verbose_name='Марка')

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'

    def __str__(self) -> str:
        return self.name
