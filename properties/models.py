from django.conf import settings
from django.db import models


class Property(models.Model):
    class PropertyType(models.TextChoices):
        APARTMENT = 'apartment', 'Квартира'
        HOUSE = 'house', 'Дом'
        STUDIO = 'studio', 'Студия'
        ROOM = 'room', 'Комната'

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    location = models.CharField(
        max_length=200,
        verbose_name='Местоположение'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )

    rooms = models.PositiveIntegerField(
        verbose_name='Количество комнат'
    )

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        verbose_name='Тип жилья'
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Арендодатель'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return self.title
