import requests

# create a function for menu
def print_menu():
    print("1. Enter a city name")
    print("2. Settings")
    print("3. Exit")
    print('-----------------------------------------------------------------------')


# create a function to get the weather of any city
def print_weather(city_name):
    weather_data = get_weather_data(city_name)
    if weather_data != None:
        print('-----------------------------------------------------------------------')
        print('                 Weather Details of ', weather_data['name'])
        print("Country Name: ", weather_data['sys']['country'])
        print("Temperature: ", weather_data['main']['temp'], 'K')
        print("Pressure: ", weather_data['main']['pressure'], 'hPa')
        print("Humidity: ", weather_data['main']['humidity'], '%')
        print("Wind Speed: ", weather_data['wind']['speed'], 'm/s')
        print("Weather: ", weather_data['weather'][0]['main'])
        print("Weather Description: ", weather_data['weather'][0]['description'])
        print('-----------------------------------------------------------------------')
        print()
    
# add your api here
g_api_key = "add_your_api_key"
g_city = 'patna'
g_lang = 'en'


def update_url_lang(lang):
    global g_lang
    g_lang = lang

# create a function to get weather data from openweathermap api    
def get_weather_data(city):

    g_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={g_api_key}&lang={g_lang}"
    
    response = requests.get(g_url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error occurred while fetching weather data.")
        return None


# create a function to print language
def print_lang():
    print("1. hi")
    print("2. en")
    print("3. fr")
    print("4. ja")
    print("5. ru")
    print("6. zh_tw")
    print()


def change_lang():
    print_lang()
    lang = input("Enter your choice: ")
    if lang == "1":
        return "hi"
    elif lang == "2":
        return "en"
    elif lang == "3":
        return "fr"
    elif lang == "4":
        return "ja"
    elif lang == "5":
        return "ru"
    elif lang == "6":
        return "zh_tw"
    else:
        print("Invalid choice. Please try again.")
        return "en"    
    

    


    


# main program
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        city = input("Enter the city name: ")
        print_weather(city)
    elif choice == "2":
        # print("Settings")
        lang = change_lang()
        update_url_lang(lang)
        print("Language changed successfully.")
        print()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
