# Funktiot, joilla luetaan tiedostoa ja printataan tekstiä main.py tiedostoon

#Tekstitiedosto
file_info = "info.txt"
#Tuotu kirjasto, jonka avulla muutetaan luettavia tekstiosuuksia utf-8 formaattiin
import codecs

#Alkuinfo: kansio avataan, sen 1. rivi tulostetaan (utf-8) konsoliin ja kansio suljetaan. 
def Info ():
    while True:
        try:
            file = open(file_info, "r")
            #muutetaan teksti utf-8 formaattiin
            print (file.readlines(codecs.BOM_UTF8)[0])
            file.close()
            break
        except:
            print ("Hei! Tervetuloa painoindeksin ja metabolisen oireyhtymän laskentaohjelmaan! Anna omat tietosi alla oleviin kohtiin. Muistathan laittaa kokonaisluvun ja desimaalin väliin pilkun sijasta pisteen.")
            break

#Loppuinfo: kansio avataan, sen 2., 3. ja 4. rivit tulostetaan (utf-8) konsoliin ja kansio suljetaan. 
def End_info():
    while True:
        try:
            file = open(file_info, "r")
            #muutetaan teksti utf-8 formaattiin
            print (file.readlines(codecs.BOM_UTF8)[1])
            file = open(file_info, "r")
            #muutetaan teksti utf-8 formaattiin
            print (file.readlines(codecs.BOM_UTF8)[2])
            file.close()
            break
        except: 
            print ("Kiitos ohjelman testaamisesta! Tulokset eivät ole diagnooseja eikä yksistään niiden perusteella voida sairauksia diagnosoida. Jos tulokset tai oma terveydentilanne mietityttävät, ole yhteydessä omaan terveydenhuoltoon. \nKäytetyt lähteet: Painoindeksilaskurin tiedot on laskettu sivuston: https://www.terveyskirjasto.fi/dlk01001/painoindeksi-bmi mukaisesti. Metabolisen oireyhtymän tiedot ovat saatu sivustolta: https://www.terveyskirjasto.fi/dlk00045.") 
            break