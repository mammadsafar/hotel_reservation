from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Hotel, City, Room


# Create your views here.

def hotels_view(request):
    try:
        location = request.GET.get('location', '')
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')
        limit = int(request.GET.get('limit', 10))
        page = request.GET.get('page', 1)

        if location:
            hotels = Hotel.objects.filter(city=location, active=True)
        else:
            hotels = Hotel.objects.filter(status='yes')

        paginator = Paginator(hotels, limit)
        objects = paginator.get_page(page)
        # print(type(objects))
        # for i in objects:
        #     print(i)
        cities = City.objects.all()
        return render(request, 'hotels.html', {'hotels': objects, 'cities': cities})
    except Exception as e:
        print(e)
    # except cities.DoesNotExist as e:
    #     print(e)


def hotel_details(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    # get hotel rooms
    # rooms = Room.hotel.all()
    rooms1 = Room.objects.filter(hotel=pk)
    rooms=[]
    for i in rooms1:
        rooms.append(i)

    return render(request, 'hotel_details.html', {'hotel': hotel, 'rooms': rooms})
