#entrada
lista = []
entrada = input()
x = "".join(entrada.split())
lista.extend(x)
numeros = [int(x) for x in lista]


#print
def desenho(lista):
    z = len(numeros)
    y = (z + 2)
    print(y * ".")
    maior = max(lista)
    for i in range(maior):
        print(".", end="")
        for j in range(len(lista)):
            if lista[j] >= (maior - i):
                print("|", end="")
            else:
                print(" ", end="")
        print(".")
    print(y * ".")
desenho(numeros)

    


#ordenação
def bubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                z = len(numeros)
                y = (z + 2)
                print(y * ".")
                maior = max(lista)
                for i in range(maior):
                    print(".", end="")
                    for j in range(len(lista)):
                        if lista[j] >= (maior - i):
                            print("|", end="")
                        else:
                            print(" ", end="")
                    print(".")
                print(y * ".")
bubbleSort(numeros)




        










    
