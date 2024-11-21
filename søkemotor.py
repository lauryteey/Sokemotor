import PySimpleGUI as sg

#Funksjon for å lese innhold fra en fil
def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as f:  #Bruker encoding for spesialtegn som æ, ø, å
            return f.readlines()  #Leser alle linjer fra filen
    except FileNotFoundError:
        return []  #Returnerer en tom liste hvis filen ikke finnes

#Funksjon for å sjekke om et ord finnes i teksten
def finnOrd(ord):
    ord_lower = ord.lower()  #Gjør søkeordet til små bokstaver
    return any(ord_lower in linje.lower() for linje in tekst)  #Sjekker om ordet finnes i noen linje

#Funksjon for å finne linje(r) som inneholder ordet
def finnLinje(ord):
    ord_lower = ord.lower()  #Gjør søkeordet til små bokstaver
    linjer = [f"Linje {i + 1}: {linje.strip()}" for i, linje in enumerate(tekst) if ord_lower in linje.lower()]
    return "\n".join(linjer) if linjer else f"Ordet '{ord}' ble ikke funnet i noen linje."  #Returnerer linjer eller melding

def printOrd(ord):
    global tekst  #Bruker global for å oppdatere teksten hvis nødvendig
    if not tekst:  #Hvis teksten er tom, prøv å lese fra fil
        filnavn = values["-FILE-"]  # Henter filnavn fra input-feltet
        tekst = lesInnTekst(filnavn)  #Leser inn tekst fra fil

    if not tekst:  #Hvis teksten fortsatt er tom
        return "Ingen tekst funnet. Vennligst velg en fil."  #Feilmelding

    ord_lower = ord.lower()  #Gjør søkeordet til små bokstaver
    resultater = []  #Liste for å lagre resultater

    for linje_nr, linje in enumerate(tekst, start=1):  #går gjennom linjer med linjenummer
        ord_liste = linje.strip().split()  #Deler linjen inn i ord
        for indeks, hvert_ord in enumerate(ord_liste, start=1):  #går gjennom hvert ord med indeks
            if hvert_ord.lower() == ord_lower:  #Sjekker om ordet samsvarer
                resultater.append(f"Linje {linje_nr}, ord {indeks}: {hvert_ord}")  #Legger til resultat

    if resultater:  #Hvis ordet ble funnet
        return f"Ordet '{ord}' finnes i teksten:\n" + "\n".join(resultater)
    else:
        return f"Ordet '{ord}' finnes ikke i teksten."  #Hvis ordet ikke ble funnet


#Funksjon for å telle antall ganger et ord dukker opp i teksten
def tellOrd(ord):
    ord_lower = ord.lower()  #Gjør søkeordet til små bokstaver
    antall = sum(linje.lower().count(ord_lower) for linje in tekst)  #Teller antall forekomster
    return f"Ordet '{ord}' ble funnet {antall} ganger."  #Returnerer resultat

#Funksjon for å validere søkeordet
def sjekkerOrd(ord):
    ekskluderte_ord = ["at", "og", "om", "men"]  #Liste med ord som ikke kan søkes etter
    if len(ord) < 3:  #Sjekker om ordet er kortere enn 3 bokstaver
        return False, "Ordet må være minst 3 bokstaver."  #Returnerer feil hvis ordet er for kort
    if ord.lower() in ekskluderte_ord:  #Sjekker om ordet er i listen over ekskluderte ord
        return False, "Bindeord kan ikke søkes etter."  #Returnerer feil hvis det er et bindeord
    return True, ""  #Returnerer at ordet er gyldig yippieeeeee



# Oppsett for GUI
layout = [
    [sg.Text("Velg en fil:"), sg.Input(key="-FILE-"), sg.FileBrowse()],  #Input-felt og knapp for å velge fil
    [sg.Text("Skriv inn et ord:"), sg.Input(key="-WORD-")],  #Input-felt for å skrive inn et ord
    [sg.Button("Vis tekst"), sg.Button("Søk etter ord"), sg.Button("Finn linje"), sg.Button("Tell ord")],  #Knappene
    [sg.Multiline(size=(70, 15), key="-OUTPUT-")]  #Tekstboks for å vise resultater
]

# Opprettelse av vindu
window = sg.Window("Søkeprogram", layout)


tekst = []  #Variabel for å lagre tekstinnholdet
while True:
    event, values = window.read()  #Leser hendelser og verdier fra GUI
    if event == sg.WINDOW_CLOSED:  #Lukker vinduet hvis "Avslutt" trykkes
        break
    
    if event == "Vis tekst":
        filnavn = values["-FILE-"]  #Henter filnavnet fra input-feltet
        tekst = lesInnTekst(filnavn)  #Leser innholdet fra filen
        if not tekst:
            window["-OUTPUT-"].update("Filen ble ikke funnet eller er tom.")  #Viser feil hvis filen er tom
        else:
            window["-OUTPUT-"].update("".join(tekst))  #Viser innholdet i tekstboksen
            
    elif event == "Søk etter ord":
        ord = values["-WORD-"]  #Henter søkeordet fra input-feltet
        gyldig, melding = sjekkerOrd(ord)  #Validerer ordet
        if not gyldig:
             window["-OUTPUT-"].update(melding)  #Viser feilmeldingen hvis ordet er ugyldig
        else:
            resultater = printOrd(ord)  #Bruker printOrd-funksjonen
            window["-OUTPUT-"].update(resultater)  #Viser resultat i tekstboksen


    elif event == "Finn linje":
        ord = values["-WORD-"]  #Henter søkeordet fra input-feltet
        gyldig, melding = sjekkerOrd(ord)  #Validerer ordet
        if not gyldig:
            window["-OUTPUT-"].update(melding)  #Viser feilmeldingen hvis ordet er ugyldig
        else:
            linjer = finnLinje(ord)  #Bruker finnLinje-funksjonen
            window["-OUTPUT-"].update(linjer)  #Viser linjer i tekstboksen
            
    elif event == "Tell ord":
        ord = values["-WORD-"]  #Henter søkeordet fra input-feltet
        gyldig, melding = sjekkerOrd(ord)  #Validerer ordet
        if not gyldig:
            window["-OUTPUT-"].update(melding)  #Viser feilmeldingen hvis ordet er ugyldig
        else:
            antall = tellOrd(ord)  #Bruker tellOrd-funksjonen
            window["-OUTPUT-"].update(antall)  #Viser antall i tekstboksen

window.close()  #Lukker vinduet (baby bye bye byee)
