import PySimpleGUI as sg
import string


#Funksjon for å lese teksten og fjerne tegnesetting
def preprocess_text(text):
    translator = str.maketrans('', '', string.punctuation)  #mappen som sletter disse symboler
    return text.translate(translator)

#Funksjon for å lese innhold fra en fil
def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as f:  #Bruker encoding for spesialtegn som æ, ø, å
            return f.readlines()  #Leser alle linjer fra filen
    except FileNotFoundError:
        return []  #Returnerer en tom liste hvis filen ikke finnes

# Funksjon for å sjekke om et ord finnes i teksten
def finnOrd(ord):
    global tekst  #Bruker global for å få tilgang til teksten
    if not tekst:  #Sjekker om teksten er tom
        filnavn = values.get("-FILE-")  #Henter filnavnet fra input-feltet
        if filnavn:
            tekst = lesInnTekst(filnavn)  #Prøver å laste teksten fra filen
        if not tekst:  #Hvis teksten fortsatt er tom
            return False  #Returnerer False fordi teksten ikke er lastet

    ord_lower = preprocess_text(ord.lower())  #Forbehandler søkeordet ved å gjøre det til små bokstaver og fjerne tegnsetting
    return any(
        ord_lower in [preprocess_text(word).lower() for word in linje.split()]  #Sjekker om ordet finnes i listen av ord i linjen
        for linje in tekst  #Går gjennom hver linje i teksten
    )


# Funksjon for å finne linjer som inneholder ordet
def finnLinje(ord):
    global tekst  #Bruker global for å få tilgang til teksten
    if not tekst:  #Sjekker om teksten er tom
        filnavn = values.get("-FILE-")  #Henter filnavnet fra input-feltet
        if filnavn:
            tekst = lesInnTekst(filnavn)  #Prøver å laste teksten fra filen
        if not tekst:  #Hvis teksten fortsatt er tom
            return "Tekst er ikke lastet. Vennligst velg en fil og vis teksten først."

    ord_lower = preprocess_text(ord.lower())  #Forbehandler søkeordet
    linjer = [
        f"Linje {i + 1}: {linje.strip()}"  #Formaterer linjene som inneholder ordet
        for i, linje in enumerate(tekst)  #Går gjennom alle linjene i teksten
        if ord_lower in [preprocess_text(word).lower() for word in linje.split()]  #Sjekker hvert ord i linjen
    ]
    return "\n".join(linjer) if linjer else f"Ordet '{ord}' ble ikke funnet i noen linje."


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
        ord_liste =  preprocess_text(linje).strip().split()   #Deler linjen inn i ord
        for indeks, hvert_ord in enumerate(ord_liste, start=1):  #går gjennom hvert ord med indeks
            if hvert_ord.lower() == ord_lower:  #Sjekker om ordet samsvarer
                resultater.append(f"Linje {linje_nr}, ord {indeks}: {hvert_ord}")  #Legger til resultat

    if resultater:  #Hvis ordet ble funnet
        return f"Ordet '{ord}' finnes i teksten:\n" + "\n".join(resultater)
    else:
        return f"Ordet '{ord}' finnes ikke i teksten."  #Hvis ordet ikke ble funnet


#Funksjon for å telle antall ganger et ord dukker opp i teksten
def tellOrd(ord):
    global tekst  #Får tilgang til den globale variabelen
    if not tekst:  #Sjekker om teksten er tom
        filnavn = values.get("-FILE-")  # Henter filnavnet fra input-feltet
        if filnavn:
            tekst = lesInnTekst(filnavn)  #Prøver å laste teksten fra filen
        if not tekst:  #Hvis teksten fortsatt er tom
            return "Tekst er ikke lastet. Vennligst velg en fil."

    ord_lower = preprocess_text(ord.lower())  #Gjør søkeordet til små bokstaver og fjerner tegnsetting
    antall = sum(
        word.lower() == ord_lower  #Sjekker om ordet samsvarer nøyaktig
        for linje in tekst  #Går gjennom hver linje
        for word in preprocess_text(linje).split()  #Deler opp linjen i ord
    )  #Teller antall forekomster
    return f"Ordet '{ord}' ble funnet {antall} ganger."  #Returnerer resultat




#Funksjon for å validere søkeordet
def sjekkerOrd(ord):
    ekskluderte_ord = ["at", "og", "om", "men"]  #Liste med ord som ikke kan søkes etter
    if len(ord) < 3:  #Sjekker om ordet er kortere enn 3 bokstaver
        return False, "Ordet må være minst 3 bokstaver."  #Returnerer feil hvis ordet er for kort
    if ord.lower() in ekskluderte_ord:  #Sjekker om ordet er i listen over ekskluderte ord
        return False, "Bindeord kan ikke søkes etter."  #Returnerer feil hvis det er et bindeord
    return True, ""  #Returnerer at ordet er gyldig yippieeeeee


file_history = []  #for å lagre de siste filene som ble åpent (max. 3)



# Oppsett for GUI
layout = [
    [sg.Text("Velg en fil:"), sg.Input(key="-FILE-"), sg.FileBrowse()],  #Input-felt og knapp for å velge fil
    [sg.Text("Skriv inn et ord:"), sg.Input(key="-WORD-")],  #Input-felt for å skrive inn et ord
    [sg.Button("Vis tekst"), sg.Button("Søk etter ord"), sg.Button("Finn linje"), sg.Button("Tell ord")],  #Knappene
    [sg.Text("Filhistorikk (siste 3):")],
    [sg.Listbox(values=[], size=(70, 3), key="-FILE_HISTORY-", enable_events=True)],
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
        filnavn = values["-FILE-"]
        if filnavn:
            tekst = lesInnTekst(filnavn)
            if not tekst:
                window["-OUTPUT-"].update("Filen ble ikke funnet eller er tom.")
            else:
                window["-OUTPUT-"].update("".join(tekst))
                
                #Oppdaterer filene som vises
                if filnavn not in file_history:
                    file_history.insert(0, filnavn)
                    if len(file_history) > 3:
                        file_history.pop()  #Beholder bare de 3 sister filer
                window["-FILE_HISTORY-"].update(file_history)
        else:
            window["-OUTPUT-"].update("Ingen fil valgt.")


    elif event == "-FILE_HISTORY-":  #Handle clicks on the file history
        selected_file = values["-FILE_HISTORY-"][0] if values["-FILE_HISTORY-"] else None
        if selected_file:
            tekst = lesInnTekst(selected_file)
            if not tekst:
                window["-OUTPUT-"].update("Filen fra historikken ble ikke funnet eller er tom.")
            else:
                window["-OUTPUT-"].update("".join(tekst))
                
            
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
