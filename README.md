# Søkemotor i Python 🔎

Dette programmet er et enkelt søkemotor som lar brukeren lese innhold fra en tekstfil og søke etter spesifikke ord. Programmet er bygget med Python og PySimpleGUI. 

Programmet sjekker om tekstfilen er lastet før søk blir gjort. Søkeordet må være minst tre bokstaver langt og kan ikke være et vanlig bindeord som ````og````, ````at````, ````men````. Den også leter kun etter hele ord, og ignorere tegnsetting og store/små bokstaver.

--- 

### Krav 

- Python 3
- PySimpleGUI-biblioteket

  
## Funksjonalitet

- Vis tekst: Laster og viser innholdet i en valgt tekstfil.

- Søk etter ord: Søker etter et spesifikt ord i teksten og viser hvilke linjer det finnes i.

- Finn linje: Viser hele linjene der det spesifikke ordet finnes.

- Tell ord: Teller hvor mange ganger et bestemt ord dukker opp i teksten.

- Filhistorikk: Viser de siste tre filene som ble åpnet, slik at brukeren enkelt kan velge dem igjen.


# Hvordan laste ned PySimpleGUI

Åpne terminalen og kjør følgende kommando

``````bash
pip install PySimpleGUI
``````

Dette vil laste ned og installere biblioteket automatisk. 

Du kan sjekke at alt fungerer ved å åpne en Python-terminal og skrive:

``````bash
import PySimpleGUI
``````

``````bash
 print(PySimpleGUI.__version__)
``````

Hvis ingen feil oppstår, og versjonen vises, er installasjonen klart! 🌸


 
