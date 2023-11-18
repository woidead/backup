import eel
import pyowm
# city = 'Osh, Kyrgyzstan'
owm = pyowm.OWM('485c3101b0010086873d4c0a44cfa203')
@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return('in city ' + city + ' ' + str(temp))















eel.init('web')
eel.start('main.html', size = (900, 900))