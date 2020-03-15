from django.shortcuts import render
from .forms import SubscriberForm
# Create your views here.

def landing(request):
    name = 'Serge Brew'
    current_day= '08.03.2020'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        
        form_save = form.save()
    return render(request, 'landing.html', locals())