#search https://opencagedata.com to get the key to use the Geocoding API,it will provide a trial key at first after that you need to pay for a key to make it work. 
#another python file called as test.py will hold the phone number of the device of which, u want the location.U can change the zoom on the 29th statement for clearer view or a zoomed out view.
#thank you 
import phonenumbers
from phonenumbers import geocoder
import folium
from test import number

Key = ""

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)


from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
results =geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")


