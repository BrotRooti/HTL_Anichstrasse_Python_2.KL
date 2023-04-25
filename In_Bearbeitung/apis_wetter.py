
from pyowm.commons.exceptions import NotFoundError
import requests





#config_dict = get_default_config()
#config_dict['language'] = 'de'
api_key = '18bca685e2b3a0f410b5f71a66a8a621'
#mgr = owm.weather_manager()
#mgg = owm.geocoding_manager()


def decoder(ort):
    ruckgabe = []

    gps = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                            params ={'q':ort,'limit':'1' ,'appid':api_key} )
    gps_json = gps.json()
    print(gps_json)
    if gps_json == []:
        raise NotFoundError
    ruckgabe.append(gps_json[0]['lon'])
    ruckgabe.append(gps_json[0]['lat'])
    print(gps.url)
    print(ruckgabe)
    return ruckgabe

def emoji_lookup (status):
    match status:
        case 'Clear':
            emoji = '☀️'
        case 'Clouds':
            emoji = '☁️'
        case 'Rain':
            emoji = '☔'
        case 'Snow':
            emoji = '❄️'
        case 'Thunderstorm':
            emoji = '⛈️'
        case 'Drizzle':
            emoji = '🌧️'
        case 'Mist':
            emoji = '🌫️'
        case 'Smoke':
            emoji = '🔥'
        case 'Haze':
            emoji = '😶‍🌫️'
        case 'Dust':
            emoji = '🌫️'
        case 'Fog':
            emoji = '🌁'
        case 'Sand':
            emoji = '🌫️'
        case 'Ash':
            emoji = '🌋'
        case 'Squall':
            emoji = '💨'
        case 'Tornado':
            emoji = '🌪️'
        case _ :
            emoji = '??'
    return emoji



def get_weather(coords,api_key,ort):

        data = requests.get("https://api.openweathermap.org/data/2.5/weather",
                            params={'lat':coords[0],'lon':coords[1],'appid':api_key,'units':'metric','lang':'de'})

        data_json = data.json()
        temp = data_json['main']['temp']


        wetter = data_json['weather'][0]['description']
        emoji = emoji_lookup(wetter)


        print("Wetterbericht")
        print(f'In {ort} ist es gerade {wetter} {emoji}')
        print(f'In {ort} hat es gerade {temp}°C 🌡')






while True:
    print("Herzlich Willkommen bei Ihrer persönlichen Wetter-API")
    while True:
        try:
            ort = input("Bitte geben sie den Ort ein: ")
            coords=decoder(ort)
        except NotFoundError:
            print(f'Ich konnte {ort} nicht finden :(')
            continue
        break

    get_weather(coords,api_key,ort)
    reset = input("Möchten Sie noch einen Ort abfragen? (j/n)")
    if reset == 'n':
        break
    else:
        continue
