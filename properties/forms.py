from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'title',
            'description',
            'location',
            'price',
            'rooms',
            'property_type',
        )

        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'location': 'Местоположение',
            'price': 'Цена',
            'rooms': 'Количество комнат',
            'property_type': 'Тип жилья',
        }
