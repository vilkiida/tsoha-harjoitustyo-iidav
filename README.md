# tsoha-harjoitustyo-iidav
## Leffa-arvostelu -sovellus:
Sovelluksessa näkyy eri elokuvia tietoineen ja niille voi kirjoittaa arvosteluja sekä lukea niitä. Sovellusta käytetään joko peruskäyttäjänä tai ylläpitäjänä.
Lisää sovelluksen ominaisuuksista:

- [x] Käyttäjä voi luoda itselleen tunnuksen ja kirjautua sillä sisään sekä ulos.
- [x] Käyttäjä näkee listan elokuvan nimiä ja klikkaamalla nimeä, pääsee näkemään tietoa elokuvasta (kuten julkaisuajankohta, genre, kuvaus, päähenkilöiden esittäjät)
- [ ] Elokuvilla on myös kansikuva, joka näkyy elokuvan tietosivulla ja elokuvalistauksissa.
- [x] Käyttäjä voi antaa tällä elokuvan tieto sivulla arvion elokuvalle (arvosana 0-10 ja halutessaan myös kirjoitetun kommentin) sekä lukea myös muiden antamia arvosteluja.
- [x] Käyttäjä voi tehdä ehdotuksen lisättävästä elokuvasta. Jonka ylläpitäjä voi joko hyväksyä tai hylätä.
- [x] Ylläpitäjä voi lisätä ja poistaa sivustolta elokuvia, sekä määrittää elokuvasta näytettävät tiedot (eli jo edellämainitut julkaisuajankohta, genre, elokuvan kansikuva, kuvaus ja päähenkilöiden esittäjät)
- [x] Ylläpitäjä voi luoda  ja poistaa kategorioita (esim genreittäin), joihin elokuvia voidaan luokitella. Tällöin yksi elokuva voi kuulua moneen ryhmään ja ryhmään voi kuulua monta elokuvaa.
- [x] Käyttäjä voi etsiä kaikki elokuvat, joiden kuvauksessa on jokin annettu sana. Käyttäjä voi etsiä elokuvaa myös nimeltä.
- [x] Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
- [x] Pääsivun elokuvalistan voi lajitella halutessaan joko: uusimmasta-vanhimpaan, vanhimmasta-uusimpaan, parhaimmasta-huonoimpaan, huonoimmasta-parhaimpaan sekä viimeisimmäksi lisätyin -järjestyksessä. Näistä vaihtoehdoista parhaimmasta-huonoimpaan ja huonoimmasta-parhaimpaan vaihtoehdoissa näytetään ainoastaan elokuvat jotka ovat saaneet arvioita (muuten arviotta jääneet olisivat automaattisesti huonoimpia). Jos mitään valintaa ei ole tehty, näytetään elokuvat automaattisesti lisäysjärjestyksessä.

## Nykytilanne (välipalautus 3):
 Sovelluksesta löytyy kaikki toiminnallisuudet kansikuvia lukuunottamatta. Myöskin esimerkiksi csrf-haavoittuvuuden estämis toimenpiteet ovat vielä vaiheessa. Koodissa on  myös vielä kohtia, jotka tarvitsevat lisää "virheviestejä" ja "try - except" kohtia jne. sekä tietysti myös pientä hienosäätöä vielä kaivataan esimerkiksi koodin ulkoasuun liittyen. Tälläistä hienosäätöä olisi esimerkiksi ohjeen [ohjelmointityyli](https://hy-tsoha.github.io/materiaali/pages/ohjelmointityyli.html)-sivun mukaisten asioiden läpikäynti koodissa.

## Testaa sovellusta:
Sovelluksella on tällä hetkellä vain yksi ylläpitäjä käyttäjä. Ylläpitäjänä sovellusta voi testata tunnuksilla:
- Käyttäjätunnus: 'ylläpitäjä'
- Salasana: 'ylläpitäjä'

Voit testata sovellusta [Herokussa](https://tsoha-harjoitustyo-iidav.herokuapp.com/).


