import csv

path="C:\\Users\\Gabin\\Downloads\\test0.csv"



def count_word():
    with open(path, newline="", encoding="ISO-8859-1") as filecsv:     
        lettore = csv.reader(filecsv,delimiter=";")
        header = next(lettore)
        print(header[0])
        virgola = 0
        for parola in header[0]:
            if parola == ",":
                virgola+= 1
        print(virgola)
        num = virgola +1
        return num
    

def find_carattero_vuoto():
    with open(path, newline="", encoding="ISO-8859-1") as filecsv:     
        lettore = csv.reader(filecsv,delimiter=";")
        header = next(lettore)
        print(header[0])
        vuoto = 0
        for i, caratteri in enumerate(header[0]):
            if i+1 != len(header[0]):
                next_caratteri = header[0][i+1]
            if caratteri == "," and next_caratteri == ",":
                return(i+1)


def find_null():
    with open(path, newline="", encoding="ISO-8859-1") as filecsv:     
        lettore = csv.reader(filecsv,delimiter=";")
        header = next(lettore)
        print (header[0])
        lista = []
        parola = ""
        for i in header[0]:
            if i == ",":
                lista.append(parola)
                parola = ""
            if i != ",":
                parola += i
        for i, parola in enumerate(lista):
            if parola == "":
                return i
    
                

def write_on_csv():
    with open(path,"a", newline="", encoding="ISO-8859-1") as filecsv:
        i = 0
        print ("i suoi dati sono composti da 1.user 2.identifier 3.first name 4.second name")
        while True:
            filecsv.write("\n")
            for i in range(count_word()):
                if i == find_null():
                    filecsv.write(" ")
                else:
                    username = input("inserire il suo user: ")
                    filecsv.write(username)
                    filecsv.write(",")
            answer = int(input("""vuoi inserire i dati di un'altra persona ?
                                1.yes
                                0.no """))
            if answer == 0:
                break

write_on_csv()
