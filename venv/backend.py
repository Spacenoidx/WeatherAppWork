import requests

# get zip code from user
zip_code = input("What is your United States ZIP Code?")

# make a request to the API
def makerequest(zip_code):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid=c7b76719fbe4781adb2aa67ac72c1123")

    if str(response.status_code) == "200":
        print(f"Success! Status Code: {response.status_code}")

    # store JSON data in a dictionary variable
    zip_data = response.json()
    return zip_data

zip_data = makerequest(zip_code)

# define the latitude and longitude globally
lati = zip_data["lat"]
longi = zip_data["lon"]

def display():
        try:
            # display the user's latitude and longitude
            print("You are currently in:", zip_data["name"])

            print(f"Your latitude is: {lati} and your longitude is {longi} \n \n ")

        except(KeyError):
            print("ZIP code not found. Exiting program.")
            quit()



def secondcall():
    # transpose latitude and longitude into the caller URL
    secondcallURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid=c7b76719fbe4781adb2aa67ac72c1123"

    # make second request to API
    secondresponse = requests.get(secondcallURL)

    weather = secondresponse.json()

    for key, value in weather["main"].items():
        print(f"{key}:  {value}")

display()
secondcall()
