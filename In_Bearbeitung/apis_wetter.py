

import requests





#config_dict = get_default_config()
#config_dict['language'] = 'de'
api_key = '18bca685e2b3a0f410b5f71a66a8a621'
#mgr = owm.weather_manager()
#mgg = owm.geocoding_manager()


def gps_decoder(ort):
    ruckgabe = []

    gps = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                            params ={'q':ort,'limit':'1' ,'appid':api_key} )
    gps_json = gps.json()
    if gps_json == []:
        raise ValueError
    ruckgabe.append(gps_json[0]['lon'])
    ruckgabe.append(gps_json[0]['lat'])
    ruckgabe.append(gps_json[0]['country'])

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
                            params={'lon':coords[0],'lat':coords[1],'appid':api_key,'units':'metric','lang':'de'})

        data_json = data.json()
        temp = data_json['main']['temp']


        wetter = data_json['weather'][0]['description']
        emoji = emoji_lookup(data_json['weather'][0]['main'])


        print(f"\033[1m \033[95m Wetterbericht für {ort} in {coords[2]} \033[0m")
        print(f'\033[96mIn {ort} in ist es gerade {wetter} {emoji}')
        print(f'In {ort} hat es gerade {temp}°C 🌡')
        print("\033[0m"*2)






while True:
    print(f"\033[1m\033[36mHerzlich Willkommen bei Ihrem persönlichen Wetterbericht!")
    while True:
        try:
            print("\033[0m")
            ort = input("Bitte geben sie den Ort für den Sie gerne einen Wetterbericht hätten ein: ")
            coords=gps_decoder(ort)

        except :
            print(f'\033[1m\033[91mIch konnte {ort} nicht finden :(')
            continue
        break
    print("\n"*100)
    get_weather(coords,api_key,ort)
    reset = input("\033[4mMöchten Sie noch einen Ort abfragen? (j/n)")
    if reset == 'n':
        break
    else:
        print("\n" * 100)
        continue
