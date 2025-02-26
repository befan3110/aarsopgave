# Årsopgave i programmering 


Læs disse punkter **grundigt** før du går i gang

- Løs så mange opgaver som du kan i løbet af projektet
- Der må ikke bruges AI, heller ikke Copilot
- Få hver løsning godkendt før du går videre til næste opgave
- Man må gerne samarbejde men alle afleverer individuelt
- Husk at kommentere koden efter python-standarder

**github**
- Gemme din arbejde i github når du er færdig med en opgave
- Gem kun kode der fungerer i github

## Forberedelser 
Repo: https://github.com/kirkby/progb/tree/main/aarsopgave

- [ ] Opret en mappe ved navn "aarsopgave" der hvor du har din kode.
- [ ] Hent filerne fra repo'et og læg dem i den nye mappe
- [ ] Vælg File->Open Folder og tilføj mappen "aarsopgave"
- [ ] Vælg File->Save workspace og giv den navnet "aarsopgave"
- [ ] Kontroller af koden fungerer

#### Opret Github repo
- [ ] Opret konto hos github.com
- [ ] Tilføj din login oplysninger i accounts (nederste venstre hjørne)
- [ ] Tilføj en fil README.MD med en kort beskrivelse af projektet
- [ ] Push din kode til github ved afslutningen af hver lektion

## Filer
Opgaven består af følgende filer:
- main.py
- price_list.py
- shopping_list.py
- price_list.csv

## Klasser
Opgaven består af følgende klasser:

**PriceList**  
Denne klasse håndterer en prisliste (en list af produkter med priser).
Til klassen hører en csv-fil med data, `price_list.csv`.

**ShoppingList**  
Denne klasse håndterer en indkøbsliste af produkter.

## Opgave A
Lav en ny udgave af `shopping_list` som tilføjer antal, således
at man angive flere af samme produkt, fx 2 Boosters.

Test det med at oprette en instans af objektet `shopping_list` og udskriv listen af produkter.

## Opgave B
Tilføj et produkt ID til `price_list` så hvert produkt har et unikt id.

Tip: brug en id som er "læselig" tekst, fx "BOOST" for Booster og "BIGM" for Big Mac Menu.
Tip: opdater klassen price_list og datafilen.

Test det med at oprette en instans af objektet `price_list` og udskriv listen af produkter med ID.

## Opgave C
Byg klassen `price_list` ind i klassen `shopping_list` så denne klasse selv kan beregne priser. Håndter den situation hvor varen ikke er på prislisten.

Test det med at oprette en instans af objektet `shopping_list` og udskriv listen af produkter med priser.

## Opgave D
Lav en metode i `shopping_list` som udskriver det samlede beløb for alle varer på listen.

Test det med at oprette en instans af objektet `shopping_list` og udskriv listen af produkter med ID.

## Opgave E
Lad klassen `price_list` hente prislisten fra nettet, fx herfra:
curl https://kirkby.github.io/price_list.json

Tjek data med curl
``` bash 
mkm@MacBookAir ~ % curl -s https://kirkby.github.io/price_list.json
{
    "Booster": 25,
    "Velo": 54,
    "Pizza": 85,
    "Big Mac Menu": 75
}%  
```

Tip: kik i de gamle eksempler og find en løsning på hvordan man requester data fra et api.

Bemærk: denne liste har ikke produkt-id'er. Hvad gør vi så?

## Opgave F
Har du mere tid?  
Giv din app en grænseflade med `tkinter`.  
Mere info følger.  