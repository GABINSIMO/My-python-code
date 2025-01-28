import random
FILE = "risposte.txt"


def carica_risposte():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            risposte = {}
            for line in lines:
                domanda, risposta = line.strip().split("|")
                risposte[domanda] = risposta
            return risposte
    except FileNotFoundError:
        return {}


def salva_risposte(risposte):
    with open(FILE, "w", encoding="utf-8") as f:
        for domanda, risposta in risposte.items():
            line = f"{domanda}|{risposta}\n"
            f.write(line)

risposte = carica_risposte()



def rispondi(domanda):
    if domanda in risposte:
        risposta = risposte[domanda]
        conferma = input(f"{risposta} [S/N]? ").strip().lower()
        if conferma == "n":
            nuova_risposta = input("Qual è la risposta corretta? ").strip()
            risposte[domanda] = nuova_risposta
            salva_risposte(risposte)
            print("Grazie per avermi insegnato qualcosa di nuovo!")
        else:
            print("Ottimo, sono contento di aver dato la risposta giusta!")
    else:
        print("Mi dispiace, non conosco la risposta a questa domanda.")
        nuova_risposta = input("Puoi aiutarmi a imparare? Qual è la risposta corretta? ").strip()
        risposte[domanda] = nuova_risposta
        salva_risposte(risposte)
        print("Grazie per avermi insegnato qualcosa di nuovo!")

        
while True:
    domanda = input("Ciao, di cosa hai bisogno? ").strip().lower()
    rispondi(domanda)


