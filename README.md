# tsoha-harjoitustyo-iidav
## Leffa-arvostelu -sovellus:
Sovelluksessa näkyy eri elokuvia tietoineen ja niille voi kirjoittaa arvosteluja sekä lukea niitä. Sovellusta käytetään joko peruskäyttäjänä tai ylläpitäjänä.
Lisää sovelluksen ominaisuuksista:

- [x] Käyttäjä voi luoda itselleen tunnuksen ja kirjautua sillä sisään sekä ulos.
- [x] Käyttäjä näkee listan elokuvan nimiä ja klikkaamalla nimeä, pääsee näkemään tietoa elokuvasta (kuten julkaisuajankohta, genre, kuvaus, päähenkilöiden esittäjät)
- [ ] Elokuvilla on myös kansikuva, joka näkyy elokuvan tietosivulla ja elokuvalistauksissa.
- [x] Käyttäjä voi antaa tällä elokuvan tieto sivulla arvion elokuvalle (arvosana 0-10 ja kirjoitetun kommentin) sekä lukea myös muiden antamia arvosteluja.
- [x] Käyttäjä voi tehdä ehdotuksen lisättävästä elokuvasta. Jonka ylläpitäjä voi joko hyväksyä tai hylätä.
- [x] Ylläpitäjä voi lisätä ja poistaa sivustolta elokuvia, sekä määrittää elokuvasta näytettävät tiedot (eli jo edellämainitut julkaisuajankohta, genre, elokuvan kansikuva, kuvaus ja päähenkilöiden esittäjät)
- [x] Ylläpitäjä voi luoda  ja poistaa kategorioita (esim genreittäin), joihin elokuvia voidaan luokitella. Tällöin yksi elokuva voi kuulua moneen ryhmään ja ryhmään voi kuulua monta elokuvaa.
- [x] Käyttäjä voi etsiä kaikki elokuvat, joiden kuvauksessa on jokin annettu sana. Käyttäjä voi etsiä elokuvaa myös nimeltä.
- [x] Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
- [ ] Listan elokuvista nähdä halutessaan joko uutuusjärjestyksessä tai arvostelujen arvosana keskiarvojen mukaisessa paremmuus järjestyksessä.

## Nykytilanne (välipalautus 3):
 Sovelluksesta löytyy kaikki toiminnallisuudet kansikuvia ja listan järjestys valintaa lukuunottamatta. Myöskin csrf-haavoittuvuuden estämis toimenpiteet ovat vielä vaiheessa. Lisäksi koodissa on vielä kohtia, jotka tarvitsevat lisää "virheviestejä" ja "try - except" kohtia jne. ja pientä hienosäätöä vielä kaivataan.

## Testaa sovellusta:
[Herokussa](https://tsoha-harjoitustyo-iidav.herokuapp.com/)


Sovelluksella on tällä hetkellä vain yksi ylläpitäjä käyttäjä. Ylläpitäjänä sovellusta voi testata tunnuksilla:
- Käyttäjätunnus: 'ylläpitäjä'
- Salasana: 'ylläpitäjä'


