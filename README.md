# Ravintolat
Sovelluksessa käyttäjä voi etsiä ravintoloita sekä antaa niille arvosteluja.
## Toiminnallisuudet
- Käyttäjä
  - voi luoda uuden tunnuksen **tehty**
  - voi poistaa olemassa olevan tunnuksen
  - voi kirjautua sisään ja ulos luomillaan tunnuksilla **tehty**
  - näkee ravintoloiden tiedot (aukioloajat, lyhyt kuvaus, hintaluokka) **tehty**
  - voi etsiä ravintoloita tietyillä hakusanoilla
  - voi etsiä ravintoloita valmiiksi muodostetuista kategorioista
  - näkee ravintolat järjestyksessä arvostelujen perusteella
  - voi antaa ravintolalle arvosanan asteikolla 1-5 sekä halutessaan lyhyen sanallisen arvion (max 1 arvostelu tietylle ravintolalle per käyttäjä) **tehty**
  - voi muokata aiemmin antamaansa arviota
- Ylläpitäjä
  - voi luoda uuden tunnuksen **tehty**
  - voi poistaa olemassa olevan tunnuksen
  - voi kirjautua sisään ja ulos luomillaan tunnuksilla **tehty**
  - voi lisätä **tehty**, poistaa ja muokata ravintoloita
  - voi poistaa käyttäjien antamia epäasiallisia arvosteluja
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


