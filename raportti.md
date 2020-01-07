# Ohjelmistotuotanto

Tämä on aloitustiedosto.

Projektityö speksataan seuraavasti:

1. Piirtäkää git:in käytöstä yhden A4:n kokoinen kuva josta selviää git:in keskeisen komponentit ja tietojen virtaaminen niiden välillä git-komennoilla. Mallia löydätte varmaan netistä mutta piirtäkää asia kuitenkin itse niin se jää paremmin mieleen. Kuvasta selviää siis komponentit ja tietojen virtaaminen niiden välillä ja mitkä keskeiset git-komennot liittyvät näihin virtaamisiin. Kuvaan voitte lisätä vaikka muistilappuina selityksiä sen keskeisistä osista. Kuvan teemana voisi olla: ”A4-kokoinen kuva git:istä joka selittää yhdellä silmäyksellä kaiken oleellisen siitä”

2. Tukeutuen edelliseen kuvaan tehkää luettelo git:in keskeisistä käsitteistä, ideoista, perusperiaatteista ja rakenteesta ja selittäkää mitä ne tarkoittavat omin sanoin.

3. Tehkää ryhmässänne pieni ohjelmointiprojekti, jonka tekemisen tarkoitus on oppia git:in käyttöä eikä ohjelmointia ja/tai monimutkaisia ohjelmarakenteita. Ohjelmointiprojektissa on tarkoitus kohdata kaikki git:in käytön merkittävät piirteet jotka on syytä osata jokapäiväisessä ohjelmistokehittämisessä yrityksessä. Projektin koon on kuitenkin syytä olla sellainen että siitä pystyy erottamaan kehittämistehtäviä ryhmän eri jäsenille olkoon tehtävät kuinka pieniä tahansa (projekti helposti ositettavissa):
   Alla on ehdotus kehitettäväksi ohjelmaksi:

   - a. Konsolissa toimiva C++ :lla kehitetty laskinohjelma, joka voisi sisältää peruslaskutoimitukset ja mikäli tarvetta on myös vaativampia sellaisia

   - b. Edellinen ohjelma on minisellainen mutta se on tarkoitus kehittää esim. lähteessä https://guides.github.com/introduction/git-handbook/ ehdotun tyypillisen git-työnkulun (typical git workflow) mukaisesti

   - c. Eli ryhmänne jakaa työn todella pieniin osiin (UI, laskentamoottori, laskutoimitukset jne.) ja niiden tekemiset jaetaan eri henkilöille. Henkilöiden on syytä tehdä triviaaleistakin lähdekooditiedostoista monia versioita vaikka se muuten tuntuisi hassulta; treenaammehan git:iä emmekä ohjelmointia! Esim. 1. versio lähdekooditiedostosta voisi sisältää pelkän header-kommentin jne.

   - d. Lisäksi kehitystyössänne on syytä käyttää git:iin liittyvää haaroittamiskäytäntöä (engl. branch): yksi henkilö tekee merkittävän projektiin liittyvän muutoksen omassa kehityshaarassa ja ajaa sen sitten yhteen (merge) päähaaran kanssa jossain kohtaa. Aina parempi mitä vaikeampi merge:stä tulee; siis haaran kehittämisessä muokataan samoja tiedostoja joita muut muokkaavat samaan aikaan. Näin pääsette näkemään mitä ovat haastavat merget git:in käytössä. Esimerkki haarasta voisi olla: aiemmin laskimenne osasi laskea vain int-luvuilla; sitten projektissa päätettiin että laskutoimitukset tehdäänkin tästä eteenpäin double-liukuluvuilla => minne kaikkialle muutos säteilee lähdekoodissa ? Tämän tekee yksi henkilö.
     Tarkkaan ottaen isossa projektissa haarassa oman ominaisuuden kehittänyt henkilö ei ominaisuutta noin vain yhdistä git-repositoryn päähaaraan vaan hän tekee yhdistämispyynnön (pull request) projektin adminille joka hallitsee päärepoa. Ominaisuuden ohjelmakoodit katselmoidaan ja hyväksytään ja vasta sitten admin suostuu tekemään yhdistämisen päähaaraan. Näin toimii myös Linux-kernel -kehitystyö Thorvaldsin ja kumppaneiden ohjaamana ja voisitte pyrkiä sitä simuloimaan – teette niitä pull-request:eja (vetämispyyntö päärepon hallinnoijalle).

4. Selvitä git:in integrointi useimmin käyttämääsi ohjelmankehitysympäristöön olkoon se vaikka Microsoft Visual Studio. Ts. selvitä miten käytät git:in keskeisiä komentoja suoraan IDEsta vai olisiko syytä käyttää komentoriviä täysin tai osittain git-komennoille. Kokeile integoinnin toimivuus vaikka sillä tavoin että kehität laskinohjelmaasi tästä IDEsta joko projektin alusta alkaen tai jostain vaiheesta alkaen. Raportoi todisteet integrointisi onnistumisesta.

5. Ottaen huomioon kaiken edellä tekemäsi kehitä itsellesi yhden A4-arkin kokoinen muistilappu perus-git -käyttöön. Siinä kerrotaan git:in keskeiset komennot aihepiireihin loogisesti jaoteltuna ja myös aikajanalle sopivasti sijoitettuina. Tämä on sinulle git-lunttilappu (cheat sheet) johon voit aina viitata.
