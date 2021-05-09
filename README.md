# tsoha-harjoitustyo-iidav
## Leffa-arvostelu -sovellus:
Sovelluksessa on listattuna elokuvia tietoineen ja käyttäjä voi lukea niille annettuja arvosteluja tai tehdä arvosteluja itse. Sovellusta käytetään joko peruskäyttäjänä tai ylläpitäjänä.

###  Sovelluksen ominaisuudet:

- [x] Käyttäjä voi luoda itselleen tunnuksen ja kirjautua sillä sisään sekä ulos.
- [x] Käyttäjä näkee listan elokuvan nimiä ja klikkaamalla nimeä, pääsee näkemään tietoa elokuvasta (kuten julkaisuajankohta, genre, kuvaus, päähenkilöiden esittäjät)
- [x] Käyttäjä voi antaa tällä elokuvan tieto sivulla arvion elokuvalle (arvosana 0-10 ja halutessaan myös kirjoitetun kommentin) sekä lukea myös muiden antamia arvosteluja.
- [x] Käyttäjä voi tehdä ehdotuksen lisättävästä elokuvasta, jonka ylläpitäjä voi joko hyväksyä tai hylätä.
- [x] Käyttäjä voi etsiä kaikki elokuvat, joiden kuvauksessa on jokin annettu sana. Käyttäjä voi etsiä elokuvaa myös nimeltä.
- [x] Ylläpitäjä voi lisätä ja poistaa sivustolta elokuvia, sekä määrittää elokuvasta näytettävät tiedot (eli jo edellämainitut julkaisuajankohta, genre, elokuvan kansikuva, kuvaus ja päähenkilöiden esittäjät)
- [x] Ylläpitäjä voi luoda  ja poistaa kategorioita (esim genreittäin), joihin elokuvia voidaan luokitella. Tällöin yksi elokuva voi kuulua moneen kategoriaan ja yhteen kategoriaan voi kuulua monta elokuvaa. Ylläpitäjä voi lisätä elokuvan kategoriaan.
- [x] Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
- [x] Ylläpitäjä voi nähdä listan ylläpitäjistä ja muuttaa haluamansa käyttäjätunnuksen ylläpitäjäksi.
- [x] Pääsivun elokuvalistan voi lajitella halutessaan joko: uusimmasta-vanhimpaan, vanhimmasta-uusimpaan, parhaimmasta-huonoimpaan, huonoimmasta-parhaimpaan sekä viimeisimmäksi lisätyin -järjestyksessä. Näistä vaihtoehdoista parhaimmasta-huonoimpaan ja huonoimmasta-parhaimpaan vaihtoehdoissa näytetään ainoastaan elokuvat jotka ovat saaneet arvioita (muuten arviotta jääneet olisivat automaattisesti huonoimpia). Jos mitään valintaa ei ole tehty, näytetään elokuvat automaattisesti lisäysjärjestyksessä.

## Sovelluksen testaaminen Herokussa:
Sovellusta voi käyttää tavallisena käyttäjänä esim. luomalla uuden tunnuksen. Ylläpitäjänä sovellusta voi testata tunnuksilla:
- Käyttäjätunnus: "ylläpitäjä"
- Salasana: "ylläpitäjä"

Voit testata sovellusta [Herokussa](https://tsoha-harjoitustyo-iidav.herokuapp.com/).


