from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
    city=request.GET.get('city','Bengaluru') 
    url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a212a565ff73a21fb09d8306b3c067ea'
    data=requests.get(url).json()
    # print(data)
    payload={'city':data['name'],
    'weather':data['weather'][0]['main'],
    'icon':data['weather'][0]['icon'],
    'kelvi_temperature':data['main']['temp'],
    'celci_temperature':int(data['main']['temp']-273),
    'pressure':data['main']['pressure'],
    'humidity':data['main']['humidity'],
     'description':data['weather'][0]['description'],}
    context={'data':payload}
    # print(context)
    return render(request,'weatherapp/weather.html',context)