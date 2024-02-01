#Metabolisen oireyhtymän riskipistelaskurin tiedot 

#Lista, johon tallentuu käyttäjän tiedot metabolisen oireyhtymän osalta
mbo_list = []

#Metabolisen oireyhtymän riskipistelaskurin kysely
def Mbo():
    while True:
        mbo_calculator = input("\nKiitos vastauksesta! Haluatko siirtyä seuraavaksi metabolisen oireyhtymän riskipistelaskuriin? (Vastaa:Kyllä/Ei) ")
        if mbo_calculator == "Kyllä" or mbo_calculator == "Kyllä" or mbo_calculator == "kyllä" or mbo_calculator == "kyllä " or mbo_calculator == "K" or mbo_calculator == "k":
            Mbo_calculator()
            break
        elif mbo_calculator == "Ei" or mbo_calculator == "Ei " or mbo_calculator == "ei" or mbo_calculator == "ei " or mbo_calculator == "E" or mbo_calculator == "e":
            break

#Metabolisen oireyhtymän pisteiden määräytyminen 
def Mbo_calculator():
    while True:
        try:
            gender = input("Sukupuoli (nainen/mies): ")
            if gender == "Nainen" or gender == "Nainen " or gender == "nainen" or gender == "nainen " or gender == "NAINEN" or gender == "NAINEN " or gender == "N" or gender == "n" or gender == "Mies" or gender == "Mies " or gender == "mies" or gender == "mies " or gender == "MIES" or gender == "MIES " or gender == "M" or gender == "m": 
                break
            else:
                print ("Virhe syötteessä, tarkasta syöte")
                continue
        except:
            print ("Virhe syötteessä, tarkista syöte")
            continue
    while True: 
        try: 
            weist = float(input("Vyötärönympärys (senttimetreinä, esim. 85): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku (Huom! Annoithan luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia.)")
            continue
    while True:
        try: 
            trigly = float(input("Veren triglyseridipitoisuus (esim. 1.0): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku (Huom! Annoithan luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia.)")
            continue
    while True: 
        try:
            hdl = float(input("Veren hdl-kolesterolin pitoisuus (esim. 3.0): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku (Huom! Annoithan luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia.)")
            continue
    while True:
        try:
            blood_pressure1 = int(input("Verenpainelukema, yläpaine (esim. 120): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku.")
            continue
    while True:
        try:
            blood_pressure2 = int(input("Verenpainelukema, alapaine (esim. 80): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku.")
            continue
    while True: 
        try:
            blood_sugar = float(input("Paastoverensokeri (esim. 3.8): "))
            break
        except:
            print ("Virhe syötteessä, tarkista annettu luku (Huom! Annoithan luvun numerona ja käytithän pilkun sijasta pistettä ennen desimaalia.)")
            continue

    #Laskuri i
    #Tulokset pisteytetään
    i = 0
    if gender == "Mies" or gender == "Mies " or gender == "mies" or gender == "mies " or gender == "MIES" or gender == "MIES " or gender == "M" or gender == "m":
        if weist > 100:
            i += 1
        if hdl < 1.0:
            i += 1
    if gender == "Nainen" or gender == "Nainen " or gender == "nainen" or gender == "nainen " or gender == "NAINEN" or gender == "NAINEN " or gender == "N" or gender == "n":
        if weist > 90:
            i += 1
        if hdl < 1.3:
            i += 1
    if trigly > 1.7:
        i += 1
    if blood_pressure1 >= 130 and blood_pressure2 >= 85:
        i += 1
    if blood_sugar >= 5.6:
        i += 1
    #Sanalliset tulokset lisätään listaan laskurin pisteiden määräytymisen mukaan
    if i >= 3:
        mbo_list.append(f"Sait metabolisen oireyhtymän testistä {i} pistettä. Testin mukaan sinulla on metabolinen oireyhtymä, olethan yhteydessä omaan terveydenhuoltoon. Lisätietoja aiheesta esimerkiksi verkkosivuilla: https://www.terveyskirjasto.fi/dlk00045.")
    else:
        mbo_list.append(f"Sait metabolisen oireyhtymän testistä {i} pistettä. Testin mukaan sinulla ei ole metabolista oireyhtymää.")