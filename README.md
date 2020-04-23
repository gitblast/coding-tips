# Coding tips

Web-sovellus, johon käyttäjät voivat lisätä lyhyitä ja ytimekkäitä koodausvinkkejä sekä selata muiden käyttäjien lisäämiä vinkkejä kategorioittain.

### Sovellus herokussa

https://coding-tips.herokuapp.com/

### Käyttäjätunnukset testaamista varten:

* username: admin
* password: admin123

### Tarkempi kuvaus

Vain kirjautuneet käyttäjät voivat lisätä vinkkejä. Vinkkeihin voi lisätä tageja, jotka kertovat aihepiirit mihin kyseinen vinkki liittyy (esim. testaaminen, javascript, yms.) sekä linkkejä ulkoisille nettisivuille lisätiedon etsimistä varten. Idea on, että itse vinkit olisivat lyhyehköjä, ja vinkkeihin lisättyjen linkkien avulla voi halutessaan etsiä lisätietoa. Linkit voivat johtaa esimerkiksi aiheeseen liittyviin postauksiin stackoverflowssa, opetusvideoihin youtubessa tai muuta vastaavaa.

Lisäksi käyttäjät voivat merkitä yksittäisen vinkin joko hyödylliseksi tai hyödyttömäksi (käytännössä like / dislike).

Käyttäjät voivat hakea vinkkejä joko sisällön, tagien, tykkäyksien tai lisääjän perusteella.

### Sovelluksen tämänhetkinen tila

Tällä hetkellä sovelluksessa toimii:

* Uuden käyttäjän rekisteröityminen

* Olemassa olevan käyttäjän sisäänkirjautuminen

* Vinkkien listaus ja listauksen järjestys joko päivämäärän, upvotejen tai downvotejen mukaan sekä listauksen filtteröinti tagien tai lisääjän perusteella

* Tagien listaus

* Käyttäjien listaus. Käyttäjien yhteydessä näytetään tällä hetkellä käyttäjänimi, käyttäjän lisäämien vinkkien kokonaismäärä, käyttäjän vinkkien likejen ja dislikejen kokonaismäärä sekä käyttäjän eniten liketetyn linkin likemäärä (sekä linkki kyseiseen vinkkiin)

* Kirjautuneena käyttäjänä vinkkien lisäys (lisäyksen yhteydessä voi lisätä myös aiheeseen liittyviä tageja sekä linkkejä lisätiedon hakemista varten), muokkaus, poisto sekä muiden käyttäjien lisäämien vinkkien like/dislike

Tietokannasta löytyy toistaikseksi viisi taulua: yksi vinkeille, yksi käyttäjille, yksi tageille, yksi linkeille sekä liitostaulu tagien ja vinkkien välillä.

### Alustava käyttöohje

Käyttäjä voi kirjautumatta selata vinkkejä, tageja sekä käyttäjiä etusivun linkeistä.

##### Tips -sivu:

Tips -sivulla on listattuna käyttäjien lisäämät vinkit.

Vinkkejä voi järjestää päivämäärän, likemäärän tai dislikemäärän mukaan klikkaamalla listauksen vasemmasta yläreunasta löytyviä painikkeita.

Lisäksi listausta voi filtteröitä oikeasta ylänurkasta löytyvien valikkojen avulla. Filtteröidä voi joko käyttäjän (eli vinkin lisääjän) tai tagien mukaan.

Jos vinkin lisääjä on lisännyt vinkkiinsä linkkejä lisätiedon hakemista varten, saa nämä linkit näkyviin klikkaamalla vinkin alareunasta löytyvää "More information" -painiketta.

##### Tags -sivu:

Tags -sivulta löytyy kaikki järjestelmästä löytyvät tagit.

Sivun yläreunasta löytyy sekä suosituin tagi (eli tagi, jolla on merkitty eniten vinkkejä), sekä tagi, jolla merkittyjen tykkäysten kokonaismäärä on suurin.

Näiden alla on listattuna kaikki tagit, niihin liittyvien vinkkien määrä sekä vinkki, jolla on eniten tykkäyksiä kyseisellä tagilla merkityistä vinkeistä.

Klikkaamalla vinkkien määrää avautuu vinkkien listaus kyseisellä tagilla filtteröitynä.

##### Users -sivu:

Users -sivulta löytyvät kaikki järjestelmään rekisteröityneet käyttäjät.

Sivun yläreunasta löytyy käyttäjä, jolla on eniten lisättyjä vinkkejä, käyttäjä, jonka lisäämillä vinkeillä on eniten tykkäyksiä sekä käyttäjä, jonka lisäämillä vinkeillä on eniten dislikejä.

Näiden alta löytyy kaikki järjestelmän käyttäjät sekä kyseisten käyttäjien lisäämien vinkkien määrä, tykkäysten ja dislikejen kokonaismäärät sekä linkki kyseisen käyttäjän eniten tykkäyksiä saamaan vinkkiin.

##### Rekisteröityminen ja kirjautunminen:

Käyttäjä voi luoda käyttäjätunnuksen klikkaamalla "Sign up" etusivulla ja täyttämällä vaaditut kentät. Tämän jälkeen käyttäjä voi kirjautua sisään klikkaamalla "Log in" ja antamalla käyttäjätunnuksensa.

##### Kirjautuneen käyttäjän toiminnot:

Kirjautuneena käyttäjä voi luoda uusia vinkkejä klikkaamalla käyttäjätunnustaan ja sen jälkeen "Add new tip" avautuvasta valikosta. Käyttäjän tulee kirjoittaa 8-160 merkkiä pitkä vinkki, ja sen jälkeen lisätä nollasta äärettömään tagia, jotka liittyvät kyseiseen vinkkiin. Tagien lisääminen tapahtuu kirjoittamalla tagi annettuun kenttään ja klikkaamalla sen jälkeen "Add".

Tämän jälkeen käyttäjä voi halutessaan lisätä vinkkiin linkkejä, joista vinkin lukija löytää lisätietoa aiheeseen liittyen. Linkkien lisääminen tapahtuu lisäämällä linkin URL annettuun kenttään ja klikkaamalla "Add".

Kun vinkki on kirjoitettu ja tagit sekä linkit lisätty, voi käyttäjä lisätä vinkin sivustolle klikkaamalla "Create".

Kirjautunut käyttäjä voi lisäksi muokata tai poistaa jo lisäämiään vinkkejä. Omiin vinkkeihin pääsee helposti käsiksi klikkaamalla omaa käyttäjätunnustaan ja sen jälkeen "My Tips" avautuvasta valikosta.

Kirjatunut käyttäjä voi myös lisätä upvoteja tai downvoteja muiden käyttäjien lisäämiin vinkkeihin. Tämä tapahtuu klikkaamalla vinkin yläpuolella olevia nuoli-ikoneita. Vihrea nuoli ylöspäin lisää upvoten, punainen nuoli alaspäin downvoten.

### Lisätietoa

[Käyttötapaukset (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/user_stories.md)

[Tietokannan rakenne (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/sqlchart.png)