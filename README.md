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

Tietokannasta löytyy toistaikseksi kaksi taulua, toinen vinkeille ja toinen käyttäjille.

### Lisätietoa

[Käyttötapaukset (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/user_stories.md)

[Tietokannan rakenne (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/sqlchart.png)