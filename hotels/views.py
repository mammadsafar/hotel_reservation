from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Hotel, City, Room, Gallery
from config.helper import helper


# Create your views here.
def get_cities():
    cities = City.objects.filter(status='yes')
    data = []
    for i in cities:
        temp = {
            'name': i,
            'id': str(i.id),
            'status': i.status,
            'state': i.state,
            'city': i.city,
        }
        data.append(temp)
    return data


def hotels_view(request):
    try:
        data = dict()
        data['hotels'] = []
        data['location'] = request.GET.get('location', '')
        data['start_date'] = request.GET.get('start_date', '')
        data['end_date'] = request.GET.get('end_date', '')
        data['last_url'] = f"?location={data['location']}&start_date={data['start_date']}&end_date={data['end_date']}"
        data['limit'] = int(request.GET.get('limit', 10))
        data['page'] = request.GET.get('page', 1)

        if data['location']:
            hotels = Hotel.objects.filter(city=data['location'], status='yes')
        else:
            hotels = Hotel.objects.filter(status='yes')

        for hotel in hotels:
            rooms = Room.objects.filter(hotel=hotel.id)
            hotel_low_price = 0
            if rooms:
                temp2 = [int(room.price) for room in rooms]
                hotel_low_price = min(temp2)
            temp = {
                'hotel': {
                    'id': hotel.id,
                    'name': hotel.name,
                    'description': hotel.description,
                    'class_hotel': hotel.class_hotel,
                    'city': hotel.city,
                    'address': hotel.address,
                    'status': hotel.status,
                    'cover': hotel.cover
                },
                'price': hotel_low_price
            }
            data['hotels'].append(temp)
        paginator = Paginator(data['hotels'], data['limit'])
        objects = paginator.get_page(data['page'])
        # print(type(objects))
        # for i in objects:
        #     print(i)
        data['cities'] = get_cities()
        return render(request, 'hotels.html', data)
    except Exception as e:
        print(e)
    # except cities.DoesNotExist as e:
    #     print(e)


def hotel_details(request, pk):
    try:
        data = dict()
        data['location'] = request.GET.get('location', '')
        data['start_date'] = request.GET.get('start_date', '')
        data['end_date'] = request.GET.get('end_date', '')
        data['cities'] = get_cities()
        data['date_interval'] = helper.date_interval(helper.ptg(data['start_date']), helper.ptg(data['end_date']))
        if helper.check_dates(helper.ptg(data['start_date']), helper.ptg(data['end_date'])):
            return render(request, 'hotel_details.html', data)

        data['hotel'] = Hotel.objects.filter(id=pk, status='yes').first()
        data['gallery'] = Gallery.objects.filter(hotel=pk)
        rooms1 = Room.objects.filter(hotel=pk, status='yes')
        data['rooms'] = []
        for i in rooms1:
            temp = {
                'id': i.id,
                'hotel': i.hotel,
                'room_Type': i.room_Type,
                'capacity': i.capacity,
                'price': int(i.price) * int(data['date_interval']),
                'status': i.status,
                'breakfast': i.breakfast,
                'extra_bed': i.extra_bed,
            }
            data['rooms'].append(temp)

        return render(request, 'hotel_details.html', data)
    except Exception as e:
        print(e)
