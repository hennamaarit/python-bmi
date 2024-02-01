# Sovellus painoindeksin laskemiseen ja metabolisen oireyhtymän määrittelemiseen

# Funktioiden ja kirjastojen tuominen
from bmi_functions import * 
from mbo_functions import *
from text_functions import * 
from alcohol_functions import *
from datetime import datetime
import json

#Aika nyt
time_now = datetime.now()
# pp/kk/vv H:M:S (tunnit/minuutit/sekunnin)
day_and_time = time_now.strftime("%d/%m/%Y %H:%M:%S")
#Tyhjä kokoelma, johon lisätään käyttäjän tiedot avain-arvopareina
customer_dictionary = {}
#Tiedosto, johon lisätään käyttäjän tiedot
customer_file = "customer.txt"

# Alkuteksti text_functions.py tiedostosta
Info()

# Käyttäjän nimi
name = input("\nAnna nimesi: ")

#Kutsutaan painoindeksikohdan kyselyn funktiota
Bmi()

#Kutsutaan metabolisen oireyhtymän kyselyn funktiota
Mbo()

#Kutsutaan alkoholin käytön riskipistelaskurin funktiota
Alcohol()

#Tuloksien tulostus
print (f"\nKiitos vastauksista {name}! Seuraavaksi näytetään yhteenveto saamistasi tuloksista: ")

#Painoindeksin tulos tulostetaan
if len(bmi_list) < 1:
    print ("\nPainoindeksi: ei syötettyjä tietoja. Jos haluat tulokset nähtäville, palaa alkuun ja vastaa kysymyksiin.")
else:
    print ("\n", *bmi_list, sep="")

#Metabolisen oireyhtymän testin tulos tulostetaan
if len(mbo_list) < 1:
    print ("\nMetabolinen oireyhtymä: ei syötettyjä tietoja. Jos haluat tulokset nähtäville, palaa alkuun ja vastaa kysymyksiin.")
else: 
    print ("\n", *mbo_list, sep="")

#Alkoholin riskipistelaskurin tulos tulostetaan
if len(audit_list) < 1:
    print ("\nAlkoholin käytön riskipistelaskuri: ei syötettyjä tietoja. Jos haluat tulokset nähtäville, palaa alkuun ja vastaa kysymyksiin.\n")
else: 
    print ("\n", *audit_list, sep="")
    print ("\n")

#Käyttäjän syöttämät tiedot lisätään kansioon
customer_dictionary [day_and_time] = name, bmi_list, mbo_list, audit_list 
while True: 
    try:
        file_customer = open(customer_file, "a")
        customer_json = json.dumps(customer_dictionary, indent = 4)
        file_customer.write(customer_json)
        break
    except:
        print ("Virhe tietojen tallentamisessa, tietojen tallentumisesta ei ole varmuutta. Ole yhteydessä pääkäyttäjään.")
        break

# Lopputeksti text_functions.py tiedostosta
End_info()