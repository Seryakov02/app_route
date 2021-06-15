from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import *
from .models import Race, Bus, Suburban


def home(request):
    return redirect("buses/")


def get_buses(request):
    buses = Bus.objects.all()
    paginator = Paginator(buses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/buses.html', {'title': 'Номера автобусов', 'buses': page_obj})


def get_shedule(request, slug):
    shedule = Race.objects.filter(slug=slug)
    return render(request, 'main/shedule.html', {'title': 'Расписание автобусов', 'shedule': shedule})


def get_suburban(request):
    if request.method == "GET":
        start_point = request.GET.get('from')
        end_point = request.GET.get('where')
        route = Suburban.objects.filter(Q(starting_point=start_point) & Q(terminus=end_point))
    form = Search()
    return render(request, 'main/suburban.html', {'title': 'Расписание электричек', 'form': form, 'route': route})


def get_map(request):
    return render(request, 'main/map.html', {'title': 'Карта'})
