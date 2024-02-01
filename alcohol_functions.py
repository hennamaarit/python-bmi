#Alkoholin käytön riskipistelaskuri Audit-C

#Lista, johon tallentuu käyttäjän tiedot alkoholin käytön riskien osalta
audit_list = []

def Alcohol():
    while True:
        alcohol = input("\nKiitos! Haluatko siirtyä seuraavaksi alkoholin käytön riskipistelaskuriin? (Vastaa:Kyllä/Ei) ")
        # Alkoholin riskikäytön laskuriin siirtymisen kysyminen ja laskurin käynnistäminen funktiota kutsumalla
        if alcohol == "Kyllä" or alcohol == "Kyllä" or alcohol == "kyllä" or alcohol == "kyllä " or alcohol == "KYLLÄ" or alcohol == "K" or alcohol == "k":
            Audit_C()
            break
        elif alcohol == "Ei" or alcohol == "Ei " or alcohol == "ei" or alcohol == "ei " or alcohol == "EI" or alcohol == "E" or alcohol == "e":
            break

#Alkoholin riskikäytön laskuri
def Audit_C():
    #Laskuri i
    i = 0
    #Kysymykset, joiden vastausten perusteella laskurin lukema kasvaa
    while True:
        try:
            how_often = int(input("Kuinka usein juot olutta, viiniä tai muita alkoholijuomia? Koeta ottaa mukaan myös ne kerrat, jolloin nautit vain pieniä määriä, esim. pullon keskiolutta tai tilkan viiniä? \n1. Ei koskaan \n2. noin kerran kuussa tai harvemmin \n3. 2-4 kertaa kuussa \n4. 2-3 kertaa viikossa \n5. 4 kertaa viikossa tai useammin \nVastaus: "))
            if how_often >= 1 and how_often <= 5:
                if how_often == 1:
                    i += 0
                if how_often == 2:
                    i+= 1
                if how_often == 3:
                    i+= 2
                if how_often == 4:
                    i+= 3
                if how_often == 5:
                    i+= 4
                break
            elif how_often < 1 or how_often > 5:
                print ("Tarkista vastaus, vastausvaihtoehto ei ole sallittu")
                continue
        except:
            print("Virhe vastauksessa, tarkista että vastaukseksi on annettu pelkkä numero") 
            continue
    while True:
        try:
            how_many = int(input("\nKuinka monta annosta alkoholia yleensä olet ottanut niinä päivinä, jolloin käytit alkoholia? \n1. 1-2 annosta \n2. 3-4 annosta \n3. 5-6 annosta \n4. 7-9 annosta \n5. 10 tai enemmän \nVastaus: "))
            if how_many >= 1 and how_many <= 5:
                if how_many == 1:
                    i += 0
                if how_many == 2:
                    i+= 1
                if how_many == 3:
                    i+= 2
                if how_many == 4:
                    i+= 3
                if how_many == 5:
                    i+= 4
                break
            elif how_many < 1 or how_many > 5:
                print ("Tarkista vastaus, vastausvaihtoehto ei ole sallittu")
                continue
        except:
            print("Virhe vastauksessa, tarkista että vastaukseksi on annettu pelkkä numero") 
            continue
    while True:
        try:
            how_often_2 = int(input("\nKuinka usein olet juonut kerralla kuusi tai useampia annoksia?: \n1. en koskaan \n2. harvemmin kuin kerran kuussa \n3. kerran kuussa \n4. kerran viikossa \n5. päivittäin tai lähes päivittäin \nVastaus: "))
            if how_often_2 >= 1 and how_often_2 <= 5:
                if how_often_2 == 1:
                    i += 0
                if how_often_2 == 2:
                    i+= 1
                if how_often_2 == 3:
                    i+= 2
                if how_often_2 == 4:
                    i+= 3
                if how_often_2 == 5:
                    i+= 4
                break
            elif how_often_2 < 1 or how_often_2 > 5:
                print ("Tarkista vastaus, vastausvaihtoehto ei ole sallittu")
                continue
        except:
            print("Virhe vastauksessa, tarkista että vastaukseksi on annettu pelkkä numero") 
            continue
    #Sukupuolen kysyminen ja vastausten tallentuminen listaan
    while True:
        try:
            gender = input("\nSukupuoli (nainen/mies): ")
            if gender == "Nainen" or gender == "Nainen " or gender == "nainen" or gender == "nainen " or gender == "NAINEN" or gender == "NAINEN " or gender == "N" or gender == "n":
                if i >= 5:
                    audit_list.append(f"Sait alkoholin käytön riskipistekyselystä {i} pistettä. Täytä verkossa pitkä AUDIT testi tarkempien tuloksien saamiseksi.")
                    break
                if i < 5:
                    audit_list.append(f"Sait alkoholin käytön riskipistekyselystä {i} pistettä. Tämän testin mukaan ei ole tarvetta tehdä laajempaa AUDIT testiä.")
                    break
            elif gender == "Mies" or gender == "Mies " or gender == "mies" or gender == "mies " or gender == "MIES" or gender == "MIES " or gender == "M" or gender == "m":  
                if i >= 6:
                    audit_list.append(f"Sait alkoholin käytön riskipistekyselystä {i} pistettä. Täytä verkossa pitkä AUDIT testi tarkempien tuloksien saamiseksi.")
                    break
                if i < 6:
                    audit_list.append(f"Sait alkoholin käytön riskipistekyselystä {i} pistettä. Tämän testin mukaan ei ole tarvetta tehdä laajempaa AUDIT testiä.")
                    break
            else:
                print ("Virhe syötteessä, tarkasta syöte")
                continue
        except:
            print ("Virhe syötteessä, tarkista syöte")
            continue