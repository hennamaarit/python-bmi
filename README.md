# Painoindeksin, metabolisen oireyhtymän ja alkoholin käytön riskipistelaskuri

## Ohjelman tarkoitus

Ohjelma on tehty osana Ohjelmoinnin perusteet -kurssia 12/2022. Kyseessä on kurssin harjoitustyö.
Painoindeksi on yleisesti ottaen hyvin tunnettu painon ja pituuden välisen suhteen kertova lukema ja sen sanallinen selitys. Metabolinen oireyhtymä on vähemmän tunnettu aineenvaihduntaan liittyvä kokonaisuus, jossa henkilöllä on samanaikaisesti monia terveyttä vaarantavia tekijöitä. Alkoholin käyttöä kartoittaessa terveydenhuollolla on käytössä erilaisia testejä riskien kartoitukseksi, yleisesti käytettyjä testejä ovat AUDIT (pitkä versio) ja AUDIT-C kyselyt (lyhyt versio).
Ohjelma on hyödyllinen tavallisten kansalaisten lisäksi terveydenhuollon ammattilaisille, jotka voisivat käyttää ohjelmaa työssään esimerkiksi riskipistelaskurien tavoin kartoittaakseen asiakkaiden tilanteita painoindeksin, metabolisen oireyhtymän tai alkoholin käytön osalta. 

### Käytetyt lähteet

Ohjelman laskentakaavat ja -arvot ovat saatu seuraavilta sivustoilta: 

- https://www.terveyskirjasto.fi/dlk00045
- https://www.terveyskirjasto.fi/dlk01001/painoindeksi-bmi 
- https://paihdelinkki.fi/sites/default/files/audit-c_0.pdf 

## Ohjelman toiminta ja sen tarkempi kuvaus

Ohjelmassa kysytään alussa käyttäjän nimi. Käyttäjä voi valita ensin, haluaako hän siirtyä painoindeksilaskuuriin. Jos käyttäjä valitsee kyllä, kysyy ohjelma tarvittavat tiedot ja antaa tulosteena painoindeksilukeman ja sanallisen selityksen. Käyttäjä voi valita seuraavaksi, haluaako siirtyä metabolisen oireyhtymän riskipistelaskuriin. Valitessaan kyllä, ohjelma kysyy tarvittavat tiedot ja laskee pisteet, jotka määrittelevät laskurin tuloksen. Tulos tulostetaan konsoliin tämän jälkeen. Viimeisenä kysytään haluaako käyttäjä siirtyä alkoholin käytön riskipistelaskuriin ja vastatessaan kyllä, ohjelma kysyy tarvittavat tiedot ja tulostaa konsoliin tulokset. Käyttäjä voi myös valita olla siirtymättä laskureihin, jolloin ohjelma tulostaa tiedon siitä, ettei se ole saanut laskettavia tietoja. Kaikki tiedot tallentuvat omiin listoihinsa.  

Listat ja nimitieto tallentuvat arvoina kokoelmaan, jonka arvopariksi tulee sen hetkinen aika "datetime" kirjaston kautta. Kokoelma muutetaan jsoniksi, jonka jälkeen se kirjoitetaan/lisätään tekstitiedostoon myöhempää mahdollista käyttöä varten. 

Ohjelmassa on lisäksi muutama rivi konsoliin tulostettavaa tekstiä erillisessä tektitiedostossa.

## Käytetyt materiaalit

Valtaosa materiaaleista ja ideoista ohjelmaan on saatu kurssilta, koska ohjelmointi ja etenkin python ovat melko tuntemattomia ennestään. Osa ongelmista (esimerkiksi kokoelman muuttaminen jsoniksi ja tallentaminen kansioon) on ratkottu nettihakujen tuloksien avulla. 

## Ajankäyttö 

Aikaa harjoitustyön tekemiseen on mennyt seuraavanlaisesti: 

- Peruskoodi ohjelmaan: 8-9 tuntia
- Virheiden käsittely: 1-2 tuntia
- Kommentointi: 1 tunti
- Viimeistely: 2-3 tuntia

## Tekijä

- Henna Muukkonen, AC6998
- 12/2022
- JAMK, Ohjelmoinnin perusteet