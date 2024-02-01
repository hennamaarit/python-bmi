# Bmi sanallisissa tulkinnoissa lähteenä käytetty sivustoa: https://www.terveyskirjasto.fi/dlk01001/painoindeksi-bmi

#Lista, johon tallentuu käyttäjän tiedot painoindeksin osalta
bmi_list = []

#Painoindeksilaskurin kysely
def Bmi():
    while True:
        bmi_calculator = input("\nHei! Haluatko siirtyä seuraavaksi painoindeksilaskuriin? (Vastaa:Kyllä/Ei) ")
        # Painoindeksin laskemisen kysyminen ja laskurin käynnistäminen funktiota kutsumalla
        if bmi_calculator == "Kyllä" or bmi_calculator == "Kyllä" or bmi_calculator == "kyllä" or bmi_calculator == "kyllä " or bmi_calculator == "KYLLÄ" or bmi_calculator == "K" or bmi_calculator == "k":
            Bmi_calculator()
            break
        elif bmi_calculator == "Ei" or bmi_calculator == "Ei " or bmi_calculator == "ei" or bmi_calculator == "ei " or bmi_calculator == "EI" or bmi_calculator == "E" or bmi_calculator == "e":
            break

#Painoindeksin laskeminen 
def Bmi_calculator(): 
    while True: 
        #Tarvittavat tiedot syötekenttinä
        try:
            weight = float(input("Paino (kg): "))
            break
        except:
            print ("Syötettä ei voitu lukea, tarkasta syöte (Huom! Syötithän luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia?)")
            continue
    while True:
        try:
            height = float(input("Pituus (metreinä esim. 1.85): "))
        except:
            print ("Syötettä ei voitu lukea, tarkasta syöte (Huom! Syötithän luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia?)")
            continue
        #Laskukaava
        bmi = weight / height ** 2
        break
    
    #Sanalliset tulokset tallentuvat listaan laskukaavan tuloksen mukaisesti
    if bmi >= 40:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Sairaalloisesti lihava")
    elif bmi >= 35:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Vaikeasti lihava")
    elif bmi >= 30:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Merkittävästi lihava")
    elif bmi >= 25:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Lievästi lihava")
    elif bmi >= 18.5:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Normaalipainoinen")
    if bmi < 18.5:
        bmi_list.append(f"Painoindeksin lukema on {bmi:.1f}, sen mukaan olet: Alipainoinen")