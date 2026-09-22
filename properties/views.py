from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PropertyForm
from .models import Property



@login_required
def create_property(request):
    if request.user.role != 'landlord':
        return redirect('home')

    if request.method == 'POST':
        form = PropertyForm(request.POST)

        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()

            return redirect('property_list')
    else:
        form = PropertyForm()

    return render(
        request,
        'properties/create_property.html',
        {'form': form}
    )

def property_list(request):
    properties = Property.objects.filter(is_active=True)

    # Поиск по заголовку и описанию
    query = request.GET.get('q', '')

    if query:
        properties = properties.filter(
            title__icontains=query
        ) | properties.filter(
            description__icontains=query
        )

    # Минимальная цена
    min_price = request.GET.get('min_price', '')

    if min_price:
        properties = properties.filter(price__gte=min_price)

    # Максимальная цена
    max_price = request.GET.get('max_price', '')

    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Местоположение
    location = request.GET.get('location', '')

    if location:
        properties = properties.filter(
            location__icontains=location
        )

    # Минимальное количество комнат
    min_rooms = request.GET.get('min_rooms', '')

    if min_rooms:
        properties = properties.filter(rooms__gte=min_rooms)

    # Максимальное количество комнат
    max_rooms = request.GET.get('max_rooms', '')

    if max_rooms:
        properties = properties.filter(rooms__lte=max_rooms)

    # Тип жилья
    property_type = request.GET.get('property_type', '')

    if property_type:
        properties = properties.filter(
            property_type=property_type
        )

    # Сортировка
    sort = request.GET.get('sort', 'newest')

    if sort == 'price_asc':
        properties = properties.order_by('price')

    elif sort == 'price_desc':
        properties = properties.order_by('-price')

    elif sort == 'oldest':
        properties = properties.order_by('created_at')

    else:
        properties = properties.order_by('-created_at')

    return render(
        request,
        'properties/property_list.html',
        {
            'properties': properties,
            'query': query,
            'min_price': min_price,
            'max_price': max_price,
            'location': location,
            'min_rooms': min_rooms,
            'max_rooms': max_rooms,
            'property_type': property_type,
            'sort': sort,
        }
    )


@login_required
def edit_property(request, property_id):
    property_obj = Property.objects.get(
        id=property_id,
        owner=request.user
    )

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_obj)

        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property_obj)

    return render(
        request,
        'properties/edit_property.html',
        {'form': form, 'property': property_obj}
    )


@login_required
def delete_property(request, property_id):
    property_obj = Property.objects.get(
        id=property_id,
        owner=request.user
    )

    if request.method == 'POST':
        property_obj.delete()
        return redirect('property_list')

    return render(
        request,
        'properties/delete_property.html',
        {'property': property_obj}
    )


@login_required
def toggle_property(request, property_id):
    property_obj = Property.objects.get(
        id=property_id,
        owner=request.user
    )

    property_obj.is_active = not property_obj.is_active
    property_obj.save()

    return redirect('property_list')
