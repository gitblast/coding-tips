# Coding tips

Web-sovellus, johon käyttäjät voivat lisätä lyhyitä ja ytimekkäitä koodausvinkkejä sekä selata muiden käyttäjien lisäämiä vinkkejä kategorioittain.

### Sovellus herokussa

https://coding-tips.herokuapp.com/

### Tarkempi kuvaus

Vain kirjautuneet käyttäjät voivat lisätä vinkkejä. Vinkkeihin voi lisätä tageja, jotka kertovat aihepiirit mihin kyseinen vinkki liittyy (esim. testaaminen, javascript, yms.) sekä linkkejä lisätietoa varten. Idea on, että itse vinkit olisivat lyhyehköjä, ja vinkkeihin lisättyjen linkkien avulla voi halutessaan etsiä lisätietoa.

Lisäksi käyttäjät voivat merkitä yksittäisen vinkin joko hyödylliseksi tai hyödyttömäksi (käytännössä upvote / downvote).

Käyttäjät voivat hakea vinkkejä joko sisällön, tagien, tykkäyksien tai lisääjän perusteella.

### Sovelluksen tämänhetkinen tila

Tällä hetkellä sovelluksessa toimii ainoastaan vinkkien lisäys, listaus ja upvoteaminen / downvoteaminen (toistaiseksi ilman kirjautumista). Tietokanta sisältää toistaiseksi vain yhden taulun. Käyttäjiin liittyvä toiminnallisuus ei myöskään vielä koodissa.

### Lisätietoa

[Käyttötapaukset (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/user_stories.md)

[Tietokannan rakenne (alustava)](https://github.com/gitblast/coding-tips/blob/master/documentation/sqlchart.png)