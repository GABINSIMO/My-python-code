
import datetime
from datetime import timedelta
import locale
import pytz
from pytz import country_timezones
import pycountry

def get_time_difference(city1, city2):

    if city1 not in pytz.all_timezones or city2 not in pytz.all_timezones:
        return "citta non valida"
    # Ottenere il fuso orario delle città
    tz1 = pytz.timezone(city1)
    tz2 = pytz.timezone(city1)

    # Ottenere l'ora corrente nelle città
    city1_time = datetime.datetime.now(tz1)
    city2_time = datetime.datetime.now(tz1)

    # Calcolare la differenza di tempo
    time_difference = city1_time.utcoffset() - city2_time.utcoffset()

    return time_difference

   # Esempio di utilizzo
city1 = 'Toronto'
city2 = 'Asia/Tokyo'
difference = get_time_difference(city1, city2)
print(f"La differenza di tempo tra {city1} {city2} è di {difference}.")
