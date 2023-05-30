import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&APPID=2a34333e1c43c98809eeaf89b5eddd00'
    # city = 'paris'

    form = CityForm(request.POST)
    if request.method == "POST":
        #form = CityForm(request.POST)
        form.save()
        #print(request.POST) #to see the request from user on command line
    
    #form = CityForm() 

    # to import all the cities from the database which we have just added
    cities = City.objects.all()
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json() # requesting and getting the response , store the response in r variable
        #print(r.text) #this will print all the details
    
        city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon']
            }
        weather_data.append(city_weather)

    # print(weather_data) # to print the weather_data

    # to pass the information to API
    context = {'weather_data': weather_data,'form':form}
    # after this passing context to template through render

    
    # print(city_weather) you can print this to see the relevant details


    return render(request,'weather/weather.html',context) # include here the template location

def about(request):
    return render(request,'weather/about.html')

def contact(request):
    return render(request,'weather/contact.html')