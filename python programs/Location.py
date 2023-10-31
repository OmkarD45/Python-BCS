import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Input validation for the phone number
while True:
    number = input("Enter the PhoneNumber with the country code: ")
    try:
        phoneNumber = phonenumbers.parse(number)
        break
    except phonenumbers.phonenumberutil.NumberFormatException:
        print("Invalid phone number format. Please enter a valid phone number.")

# Replace 'YOUR_OPENCAGE_API_KEY' with your actual API key
Key = "1b7b64a2410a4d80bf2fa0ba546e5205"

yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + yourLocation)

yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Service provider: " + yourServiceProvider)

geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

    myMap.save("Location.html")
    print("Map saved as Location.html")
else:
    print("Location not found.")
