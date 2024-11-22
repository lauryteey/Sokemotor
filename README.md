#Søkemotor i Python 

Dette programmet er et enkelt søkemotor som lar brukeren lese innhold fra en tekstfil og søke etter spesifikke ord. Programmet er bygget med Python og PySimpleGUI. 

Programmet sjekker om tekstfilen er lastet før søk blir gjort. Søkeordet må være minst tre bokstaver langt og kan ikke være et vanlig bindeord som "og", "at", "men", osv. Den også leter kun etter hele ord, og ignorere tegnsetting og store/små bokstaver.

Funksjonalitet

- Vis tekst: Laster og viser innholdet i en valgt tekstfil.

- Søk etter ord: Søker etter et spesifikt ord i teksten og viser hvilke linjer det finnes i.

- Finn linje: Viser hele linjene der det spesifikke ordet finnes.

- Tell ord: Teller hvor mange ganger et bestemt ord dukker opp i teksten.

- Filhistorikk: Viser de siste tre filene som ble åpnet, slik at brukeren enkelt kan velge dem igjen.

Det bruktes verktøy som W3Schools.com, geeksforgeeks.org og chatGPT for utvikling av programmet.

Krav 

- Python 3
- PySimpleGUI-biblioteket

Hvordan laste ned PySimpleGUI

Åpne terminalen og kjør følgende kommando

- pip install PySimpleGUI

Dette vil laste ned og installere biblioteket automatisk. 

Du kan sjekke at alt fungerer ved å åpne en Python-terminal og skrive:

- import PySimpleGUI
- print(PySimpleGUI.__version__)

Hvis ingen feil oppstår, og versjonen vises, er installasjonen vellykket.


 