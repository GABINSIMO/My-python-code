path0 = "C:\\Users\\Gabin\\Desktop\\python\\animal.txt"
path1 = "C:\\Users\\Gabin\\Desktop\\python\\_animaliNONdoppioni.txt"

def element_exists(element, lst):
    return element in lst

def compare():
    with open(path0, "r", encoding="utf-8") as filetxt, open(path1, "r", encoding="utf-8") as filetxt0:
        lines = filetxt.readlines()
        lines0 = filetxt0.readlines()

        print(lines0)
        print(lines)

        lista_comune = []
        lista = []
        for i in range(len(lines)):
                if element_exists(lines[i], lines0) == True:
                    lista_comune.append(lines[i])
                else:
                    lista.append(lines[i])
        print(lista_comune,"\n", lista)

compare()
