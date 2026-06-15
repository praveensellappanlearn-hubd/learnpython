import requests as rq
import pandas as pd

def get_latlan(city_name):
    data=rq.get('https://geocoding-api.open-meteo.com/v1/search?name='+city_name)
    data_json=data.json()
   # print(data_json)
  
        
   # return [13.091461734944524, 80.26626431184138]

city_name="mumbi"
data=get_latlan(city_name)
def mar_data(place_name):
    data=rq.get('https://geocoding-api.open-meteo.com/v1/search?name={place}&count=1')
    print(data.json())

mar_data('chennai')


def mar_price(year):
    data_price=rq.get("https://api.datausa.io/tesseract/data.jsonrecords?cube=acs_yg_total_population_5&measures=Population&include=Year:{year};State:04000US01&drilldowns=State,Year")
    #print(data_price.json())

mar_price('2025')

def mar_dog():
    data_dog=rq.get('https://dog.ceo/api/breeds/image/random')
    print(data_dog.json())

mar_dog()

def mar_curr(curr):
    data_currency=rq.get("https://api.frankfurter.app/latest?amount=100&from=USD&to="+curr)
    print(data_currency.json())

mar_curr('INR')