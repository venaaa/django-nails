from django.shortcuts import render

# Create your views here.

def landing(request):
    name = 'Serge Brew'
    current_day= '08.03.2020'
    return render(request, 'landing.html', locals())