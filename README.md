# Coding tips

Web-sovellus, johon käyttäjät voivat lisätä lyhyitä ja ytimekkäitä koodausvinkkejä sekä selata muiden käyttäjien lisäämiä vinkkejä kategorioittain.

### Sovellus herokussa

https://coding-tips.herokuapp.com/

### Käyttäjätunnukset testaamista varten:

* username: admin
* password: admin123

### Tarkempi kuvaus

Vain kirjautuneet käyttäjät voivat lisätä vinkkejä. Vinkkeihin voi lisätä tageja, jotka kertovat aihepiirit mihin kyseinen vinkki liittyy (esim. testaaminen, javascript, yms.) sekä linkkejä ulkoisille nettisivuille lisätiedon etsimistä varten. Idea on, että itse vinkit olisivat lyhyehköjä, ja vinkkeihin lisättyjen linkkien avulla voi halutessaan etsiä lisätietoa. Linkit voivat johtaa esimerkiksi aiheeseen liittyviin postauksiin stackoverflowssa, opetusvideoihin youtubessa tai muuta vastaavaa.

Lisäksi käyttäjät voivat merkitä yksittäisen vinkin joko hyödylliseksi tai hyödyttömäksi (käytännössä upvote / downvote).

Käyttäjät voivat hakea vinkkejä joko sisällön, tagien, tykkäyksien tai lisääjän perusteella.

### Sovelluksen tämänhetkinen tila

Tällä hetkellä sovelluksessa toimii:

* Uuden käyttäjän rekisteröityminen

* Olemassa olevan käyttäjän sisäänkirjautuminen

* Vinkkien listaus, lisäys, poisto sekä upvoteaminen/downvoteaminen (näistä vain listaus onnistuu ilman kirjautumista)

* Vinkkien listauksen järjestys joko päivämäärän, upvotejen tai downvotejen mukaan

* Vinkkien filtteröinti tagien perusteella

* Tagien listaus (ulkoasu viilaamatta)

* Käyttäjien listaus. Käyttäjien yhteydessä näytetään tällä hetkellä käyttäjänimi, käyttäjän lisäämien vinkkien kokonaismäärä, käyttäjän vinkkien upvotejen ja downvotejen kokonaismäärä sekä käyttäjän eniten upvotetun linkin liket (sekä linkki kyseiseen vinkkiin)

Tietokannasta löytyy toistaikseksi neljä taulua: yksi vinkeille, yksi käyttäjille, yksi tageille sekä liitostaulu tagien ja vinkkien välillä.

### Alustava käyttöohje

Käyttäjä voi kirjautumatta selata vinkkejä, tageja ja käyttäjiä etusivun linkeistä.

Käyttäjä voi luoda käyttäjätunnuksen klikkaamalla "Sign up" etusivulla ja täyttämällä vaaditut kentät. Tämän jälkeen käyttäjä voi kirjautua sisään klikkaamalla "Log in" ja antamalla käyttäjätunnuksensa.

Kirjautuneena käyttäjä voi luoda uusia vinkkejä klikkaamalla käyttäjätunnustaan ja sen jälkeen "Add new tip" avautuvasta valikosta. Käyttäjän tulee kirjoittaa 8-160 merkkiä pitkä vinkki, ja sen jälkeen lisätä nollasta äärettömään tagia, jotka liittyvät kyseiseen vinkkiin. Tagien lisääminen tapahtuu kirjoittamalla tagi annettuun kenttään ja klikkaamalla sen jälkeen "Add".

Kun vinkki on kirjoitettu ja tagit lisätty, voi käyttäjä lisätä vinkin sivustolle klikkaamalla "Create".

Kirjautunut käyttäjä voi lisäksi muokata tai poistaa jo lisäämiään vinkkejä. Omiin vinkkeihin pääsee helposti käsiksi klikkaamalla omaa käyttäjätunnustaan ja sen jälkeen "My Tips" avautuvasta valikosta.

Kirjatunut käyttäjä voi myös lisätä upvoteja tai downvoteja muiden käyttäjien lisäämiin vinkkeihin. Tämä tapahtuu klikkaamalla vinkin yläpuolella olevia nuoli-ikoneita. Vihrea nuoli ylöspäin lisää upvoten, punainen nuoli alaspäin downvoten.

### Lisätietoa

[Käyttötapaukset (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/user_stories.md)

[Tietokannan rakenne (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/sqlchart.png)