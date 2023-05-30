from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model=City # as we are only interested in the city name
        fields = ['name']
        widgets ={'name' : TextInput(attrs={'class':'input' , 'placeholder':'City Name'})}