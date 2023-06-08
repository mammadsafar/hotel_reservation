from django.shortcuts import render
from django.views.generic.base import TemplateView
from hotels.models import City


# from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    model = City.objects.all()
    context_object_name = 'cities'

    template_name = 'home.html'


def homeView(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'cities': cities})


class AboutView(TemplateView):
    template_name = 'about.html'
