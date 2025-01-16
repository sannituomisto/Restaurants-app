# Restaurants-app
Sovelluksessa käyttäjä voi etsiä ravintoloita sekä antaa niille arvosteluja.
## Toiminnallisuudet
- Käyttäjä
  - voi luoda uuden tunnuksen **tehty**
  - voi poistaa olemassa olevan tunnuksen **tehty**
  - voi kirjautua sisään ja ulos luomillaan tunnuksilla **tehty**
  - voi lisätä ravintoloita suosikkeihin ja poistaa ravintoloita suosikeista **tehty**
  - näkee ravintoloiden tiedot (aukioloajat, lyhyt kuvaus, hintaluokka) **tehty**
  - näkee ravintolat järjestyksessä arvostelujen perusteella **tehty**
  - näkee ravintolat järjestyksessä hintaluokan perusteella **tehty**
  - voi antaa ravintolalle arvosanan asteikolla 1-5 sekä halutessaan lyhyen sanallisen arvion **tehty**
  - voi poistaa aiemmin antamaansa arvion **tehty**
- Ylläpitäjä
  - voi luoda uuden tunnuksen **tehty**
  - voi poistaa olemassa olevan tunnuksen **tehty**
  - voi kirjautua sisään ja ulos luomillaan tunnuksilla **tehty**
  - voi lisätä ja poistaa ravintoloita **tehty**
  - voi poistaa käyttäjien antamia epäasiallisia arvosteluja **tehty**
  - voi järjestää ravintolat eri kategorioihin **tehty**
  
## Sovelluksen käynnistäminen paikallisesti
1. Kloonaa tämä repositorio koneellesi ja siirry sen juurikansioon.   

2. Luo .env-tiedosto, jonka sisältö on seuraavanlainen:

> DATABASE_URL=\<tietokannan-paikallinen-osoite>   
> SECRET_KEY=\<salainen-avain>

3. Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

`$ python3 -m venv venv`  
`$ source venv/bin/activate`  
`$ pip install -r ./requirements.txt`

4. Määritä tietokannan skeema komennolla

`$ psql < schema.sql`

5. Nyt sovellus käynnistyy komennolla

`$ flask run`

## Huom
Sovelluksessa ei ole valmiina ravintoloita vaan admin-käyttäjän täytyy itse lisätä ravintoloita sovellukseen.


