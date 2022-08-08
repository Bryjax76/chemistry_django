from django.shortcuts import render
from app_chemistry.models import Elements

# Create your views here.

def canvas(request):
    return render(request, 'canvas.html')

def homepage(request):
    elements = Elements.objects.all()
    group1 = Elements.objects.filter(group=1)
    group2 = Elements.objects.filter(group=2)
    group3 = Elements.objects.filter(group=3)
    group4 = Elements.objects.filter(group=4)
    group5 = Elements.objects.filter(group=5)
    group6 = Elements.objects.filter(group=6)
    group7 = Elements.objects.filter(group=7)
    group8 = Elements.objects.filter(group=8)
    group10 = Elements.objects.filter(group=10, is_lanthanides=False, is_actinides=False)
    group11 = Elements.objects.filter(group=11)
    group12 = Elements.objects.filter(group=12)
    group13 = Elements.objects.filter(group=13)
    group14 = Elements.objects.filter(group=14)
    group15 = Elements.objects.filter(group=15)
    group16 = Elements.objects.filter(group=16)
    group17 = Elements.objects.filter(group=17)
    group18 = Elements.objects.filter(group=18)
    group19 = Elements.objects.filter(group=19)
    lanthanides = Elements.objects.filter(is_lanthanides=True)
    actinides = Elements.objects.filter(is_actinides=True)

    return render(request, 'home.html', {
        'group1': group1,
        'group2': group2,
        'group3': group3,
        'group4': group4,
        'group5': group5,
        'group6': group6,
        'group7': group7,
        'group8': group8,
        'group10': group10,
        'group11': group11,
        'group12': group12,
        'group13': group13,
        'group14': group14,
        'group15': group15,
        'group16': group16,
        'group17': group17,
        'group18': group18,
        'group19': group19,
        'lanthanides': lanthanides,
        'actinides': actinides,
        'elements': elements,
    })
