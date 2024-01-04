import phonenumbers
import opencage
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
# +import json 

from fghg import number
# enter_here = input("enter here: ")

pHoneNu = phonenumbers.parse(number)
loCation = geocoder.description_for_number(pHoneNu,'en')
print(loCation)

serv_provider = phonenumbers.parse(number)
print(carrier.name_for_number(serv_provider,'en'))

my_apiKEY = 'fb063c57a16d49f08dbf51fe0b8d81f0'
geocoder = OpenCageGeocode(my_apiKEY)
query = str(loCation)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

# pretty_data = json.dumps(result, indent=3)
# print(pretty_data)

mY_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=loCation).add_to(mY_map)
mY_map.save("mgh.html")
