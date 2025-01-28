from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from bs4 import BeautifulSoup
import requests
import datetime
import re 


start = input("insert where you want to sart: ")
destination = input ("insert your destination: ")
URL = 'https://www.google.it/maps/dir/'+start+'/'+destination
#URL = 'https://www.google.it/maps/dir/Milano/bergamo'


"""
paesi_lingue = {
"Afghanistan": "ps",
"Albania": "sq",
"Algeria": "ar",
"Andorra": "ca",
"Angola": "pt",
"Antigua e Barbuda": "en",
"Arabia Saudita": "ar",
"Argentina": "es",
"Armenia": "hy",
"Australia": "en",
"Austria": "de",
"Azerbaigian": "az",
"Bahamas": "en",
"Bahrein": "ar",
"Bangladesh": "bn",
"Barbados": "en",
"Belgio": "nl, fr, de",
"Belize": "en",
"Benin": "fr",
"Bhutan": "dz",
"Bielorussia": "be",
"Birmania (Myanmar)": "my",
"Bolivia": "es",
"Bosnia ed Erzegovina": "bs, hr, sr",
"Botswana": "en",
"Brasile": "pt",
"Brunei": "ms",
"Bulgaria": "bg",
"Burkina Faso": "fr",
"Burundi": "fr, rn",
"Cambogia": "km",
"Camerun": "fr, en",
"Canada": "en, fr",
"Capo Verde": "pt",
"Ciad": "fr, ar",
"Cile": "es",
"Cina": "zh",
"Cipro": "el, tr",
"Colombia": "es",
"Comore": "ar, fr, sw",
"Congo (Brazzaville)": "fr",
"Congo (Kinshasa)": "fr",
"Corea del Nord": "ko",
"Corea del Sud": "ko",
"Costa d’Avorio": "fr",
"Costa Rica": "es",
"Croazia": "hr",
"Cuba": "es",
"Danimarca": "da",
"Dominica": "en",
"Ecuador": "es",
"Egitto": "ar",
"El Salvador": "es",
"Emirati Arabi Uniti": "ar",
"Eritrea": "ti, ar, en",
"Estonia": "et",
"Eswatini": "en, ss",
"Etiopia": "am",
"Figi": "en, fj, hi",
"Filippine": "tl, en",
"Finlandia": "fi, sv",
"Francia": "fr",
"Gabon": "fr",
"Gambia": "en",
"Georgia": "ka",
"Germania": "de",
"Ghana": "en",
"Giamaica": "en",
"Giappone": "ja",
"Gibuti": "fr, ar",
"Giordania": "ar",
"Grecia": "el",
"Grenada": "en",
"Guatemala": "es",
"Guinea": "fr",
"Guinea-Bissau": "pt",
"Guinea Equatoriale": "es, fr, pt",
"Guyana": "en",
"Haiti": "fr, ht",
"Honduras": "es",
"India": "hi, en",
"Indonesia": "id",
"Iran": "fa",
"Iraq": "ar, ku",
"Irlanda": "en, ga",
"Islanda": "is",
"Isole Cook": "en",
"Isole Marshall": "en, mh",
"Isole Salomone": "en",
"Israele": "he",
"Italia": "it",
"Kazakistan": "kk, ru",
"Kenya": "sw, en",
"Kirghizistan": "ky, ru",
"Kiribati": "en",
"Kuwait": "ar",
"Laos": "lo",
"Lesotho": "en, st",
"Lettonia": "lv",
"Libano": "ar",
"Liberia": "en",
"Libia": "ar",
"Liechtenstein": "de",
"Lituania": "lt",
"Lussemburgo": "lb, fr, de",
"Madagascar": "mg, fr",
"Malawi": "en, ny",
"Maldive": "dv",
"Malesia": "ms",
"Mali": "fr",
"Malta": "mt, en",
"Marocco": "ar",
"Mauritania": "ar",
"Mauritius": "en",
"Messico": "es",
"Micronesia": "en",
"Moldavia": "ro",
"Monaco": "fr",
"Mongolia": "mn",
"Montenegro": "sr, bs, sq, hr",
"Mozambico": "pt",
"Namibia": "en",
"Nauru": "na, en",
"Nepal": "ne",
"Nicaragua": "es",
"Niger": "fr",
"Nigeria": "en",
"Norvegia": "no",
"Nuova Zelanda": "en, mi",
"Oman": "ar",
"Paesi Bassi": "nl",
"Pakistan": "ur, en",
"Palau": "en, pau",
"Palestina": "ar",
"Panama": "es",
"Papua Nuova Guinea": "en, tpi, hmo",
"Paraguay": "es, gn",
"Perù": "es",
"Polonia": "pl",
"Portogallo": "pt",
"Qatar": "ar",
"Regno Unito": "en",
"Repubblica Ceca": "cs",
"Repubblica Centrafricana": "fr, sg",
"Repubblica Dominicana": "es",
"Romania": "ro",
"Ruanda": "rw, fr, en",
"Russia": "ru",
"Saint Kitts e Nevis": "en",
"Saint Vincent e Grenadine": "en",
"Samoa": "sm, en",
"San Marino": "it",
"Santa Lucia": "en",
"Sao Tomé e Principe": "pt",
"Senegal": "fr",
"Serbia": "sr",
"Seychelles": "fr, en, crs",
"Sierra Leone": "en",
"Singapore": "en, ms, zh, ta",
"Siria": "ar",
"Slovacchia": "sk",
"Slovenia": "sl",
"Somalia": "so, ar",
"Spagna": "es",
"Sri Lanka": "si, ta",
"Stati Uniti d’America": "en",
"Sudafrica": "af, en, zu, xh, st, tn, ts, ss, ve, nr",
"Sudan": "ar, en",
"Sudan del Sud": "en",
"Suriname": "nl",
"Svezia": "sv",
"Svizzera": "de, fr, it, rm",
"Tagikistan": "tg",
}
"""



def screemshoot():    
    driver = webdriver.Chrome() # Configura il driver di Chrome
    driver.get(URL) 
    lista = []
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".lssxud"))).click()
        time.sleep(3)
        count = 0
        results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".m6Uuef")))
        for result in results:
            count += 1
            #if  == WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "img[aria-label^='Mit dem Auto']"))):
            if count == 2:
                car_time = result.text
                lista.append(car_time)
            if count == 3:
                public_transport_time = result.text
                lista.append(public_transport_time)
            if count == 4:
                foot_time = result.text
                lista.append(foot_time)
            if count == 5:
                bicycle_time = result.text
                lista.append(bicycle_time)
            if count == 6:
                plan_time = result.text
                lista.append(plan_time)

        if car_time == "" and public_transport_time == "" and foot_time == "" and bicycle_time == "" and plan_time == "":
            print("ooopppss! you insert a wrong destination")
            lista = []
        else:
            print("the time with the car is: ",car_time)
            print("the time with the public transport is: ",public_transport_time)
            print("the time to go on foot is: ",foot_time)
            print("the time with the bicycle is: ",bicycle_time)
            print("the time with the plan is: ",plan_time)

            return lista
    except Exception as e:
        print(f"non è stato possibile cliccare sul bottone {e}")


    time.sleep(5)
    driver.save_screenshot('screenshot.png') # Fai lo screenshot e salvalo come file 
    driver.quit() # Chiudi il browser




def convertion_time(n):
    day = re.compile(r'(\d+)\s*Tage') #replace Tage with day 
    hour = re.compile(r'(\d+)\s*h')
    minute = re.compile(r'(\d+)\s*min')
    hour_minute = re.compile(r'(\d+)\s*h\s*(\d+)\s*min')

    d = 0
    h = 0
    m = 0
    
    day_match = day.search(n)
    if day_match:
        d = int(day_match.group(1))
        
    hour_minute_match = hour_minute.search(n)
    if hour_minute_match:
        h = int(hour_minute_match.group(1))
        m = int(hour_minute_match.group(2))
    else:
        hour_match = hour.search(n)
        if hour_match:
            h = int(hour_match.group(1))
            
        min_match = minute.search(n)
        if min_match:
            m = int(min_match.group(1))
        else:
            if 'h' in n:
                minu = n.split('h')[-1].strip()
                if minu.isdigit():
                    m = int(minu)
                
    munite_convert = (d*1440) + (h*60) + m
    return munite_convert




def best_time():
    times = screemshoot()
    lista = []
    for el in times:
        if el == '' :
            continue
        else :
            #print(convertion_time(el))
            lista.append(int(convertion_time(el)))
    best = lista[0]
    for i in range(len(lista)):
        if lista[i] < best:
            best = lista[i]
    print("the fastest way to go have: ", best, "min")
    
        
        
best_time()










