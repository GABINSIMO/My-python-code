


count = 0

def file():
    path="C:\\Users\\Gabin\\Desktop\\python\\multi\\pippo.txt"
    with open(path, "r", encoding="utf-8") as filetxt, open("C:\\Users\\Gabin\\Desktop\\python\\multi\\test.txt", "w", encoding="utf-8") as filetxt_testo:
        lines = filetxt.readlines()
        i = 0
        filetxt.close()
        for i,parola in enumerate(lines):
            filetxt_testo.write(parola.replace("\n", " "))
        filetxt_testo.close()
            
    with open("C:\\Users\\Gabin\\Desktop\\python\\multi\\test.txt", "r", encoding="utf-8") as file:
        line = file.readlines()
        return(line[0])


def text_to_translate():
    line = file()
    iterator = iter(line)
    text = ""
    global count
    reset_count = 0
    for i in range(count, len(line)):
        resto = ""
        text = text + line[i]
        next(iterator)
        count+= 1
        reset_count+= 1
        if reset_count == 50 and next(iterator)== " ":
            return text
            break
        elif reset_count > 50 and line[i] == ".":
            return text
            break
            
def txt():            
    line = file()
    lista = []
    for i in range(2):
        lista.append(text_to_translate())
    return lista


def write_file(path, testo):
    with open (path, "a", encoding="utf-8") as f:
        f.write(testo)

def reset_file(path):
    with open (path, "w", encoding="utf-8") as f:
        f.write("")
        
      

def translation_script():
    from googletrans import Translator
    from googletrans.constants import LANGCODES, LANGUAGES
    translator = Translator()

    while True:
        testo = "Inserisci qua il tuo testo"
        try:
            detection_result = translator.detect(testo)
            codice_lingua_di_partenza = detection_result.lang
            print(codice_lingua_di_partenza, "\n")
        except Exception as e:
            print("\n.................Errore durante il detect della lingua.................\n")
            
        count = 0
        for code,name in LANGUAGES.items():
            path = "C:\\Users\\Gabin\\Desktop\\python\\multi\\trad_"+code+".txt"
            reset_file(path)
        for code,name in LANGUAGES.items():
            try:
                codice_lingua_finale = code
                path = "C:\\Users\\Gabin\\Desktop\\python\\multi\\trad_"+code+".txt"
                traduction = translator.translate(testo, src=codice_lingua_di_partenza, dest=codice_lingua_finale)
                print (traduction.text, "\n")
                write_file(path, traduction.text)
            except:
                print("...............................questa lingua non esiste ancora nel nostro DB.........................................")
        count += 1
        if count == 1:
            break

translation_script()

    
