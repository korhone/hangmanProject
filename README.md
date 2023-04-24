Työn kuvaus:

Käyttäjä pyydetään määrittämään millä vaikeusasteella hän haluaa pelata peliä. Mitä haastavampi, sitä vähemmän elämiä on jäljellä.
Kun käyttäjä on määrittänyt vaikeusasteen, peli alkaa. Salainen sana näytetään ?-merkeillä, josta käyttäjä näkee monta kirjainta sanasta puuttuu.
Väärä vastaus vähentää henkiä, oikea vastaus päivittää arvattavan sanan ja ?-merkki vaihtuu kirjaimeksi, joka arvattiin oikein. 
Peli päättyy joko henkien loppumiseen tai oikean sanan arvaamiseen kirjainkirjaimelta tai suoraan sanan arvauksella. 

Toteutuksesta, ja miksi jokin on tehty miksi on: 

Kielenä Python, salaiset sanat saa itse määrittää txt-tiedostossa "secret_word_list.txt" ja lista päivittyy aina kun ohjelman ajaa alusta. Tämä mahdollistaa txt-tiedostoon per pelikerta arvattavien sanojen määrittelyn.
Random.chosella valitaan listan sanoista sana mitä käyttäjä lähtee sitten arvuuttelemaan. Sana voi olla pitkä tai lyhyt, ei tarvitse olla tietyn mittainen että se sopisi peliin, sovellus tukee myös lauseita, mutta silloin pitää arvata myös välilyönnit. Poikkeudenkäsittelyä käytetty, jos määritetyssä tiedoston nimessä olisi jotain väärin, palautetaan virhesanoma, joka pyytää tarkistamaan tiedoston nimen. 

Funktiot difficulty() ja update_clue() ovat tehty helpottamaan ohjelman ajamista. 
Difficultyssä numeroilla 1, 2, 3, käyttäjä määrittää vaikeusasteen. 
Poikkeuskäsittelyä on käytetty tilanteissa että käyttäjä syöttää kirjaimia tai numeron 1-3 ulkopuolelta. 
Update_clue() päivittää ????-salaisen sanan merkit aina indeksinumero kerrallaan ja korvaa ?-merkin oikealla kirjaimella, jos se löytyy sanasta. 

Pääohjelmassa määritetään funktio difficultyn avulla elämien määrä mitä kierroksella käytetään, while-loopilla pyydetään käyttäjää arvaamaan sana niin monta kertaa kunnes hän saa sen arvattua tai elämät loppuvat. Tähän käytin if-elseä, koska koin sen helpoimmaksi tavaksi toteuttaa. Käyttäjän syöttämällä kirjaimen koolla ei ole väliä, sillä input käännetään ISOKSI KIRJAIMIKSI.
Pääohjelmassa on myös poikkeudenkäsittely, jos jotain jollain tavalla saisi siinä menemään vinksalleen, suosittelen olemaan vahvasti itseeni yhteydessä. 

Lopuksi käyttäjälle kerrotaan tulosteella, voittiko hän pelin vai hävisikö hän sen. 
