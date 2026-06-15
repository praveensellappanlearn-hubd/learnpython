import requests as rq
import 

def get_latlan(city_name):
    data=rq.get('https://geocoding-api.open-meteo.com/v1/search?name='+city_name)
    data_json=data.json()
    print(data_json)
  
        
   # return [13.091461734944524, 80.26626431184138]
    


city_name="mumbi"
data=get_latlan(city_name)
#print(data)
###############################3
