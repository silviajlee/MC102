#entrada
procurado = int(input())
entrada = input()
lista = entrada.split(" ")
numeros = [int(x) for x in lista]
ordenada = sorted(numeros)
inicio = 0
fim = len(numeros)-1
meio = (inicio + fim)//2

#saida1
print("Elemento procurado:", format(procurado, "03d"))
def imprimenormal(numeros,inicio,meio,fim):
    linhadecima = ""
    linhadebaixo = ""
    linhadomeio = ""
    for i, valor in enumerate(numeros):
        linhadomeio = linhadomeio + ("| " + format(valor, "03d") + " ")
        linhadecima = linhadecima + "+-----"
        linhadebaixo = linhadebaixo + "+-----"
        if i == fim:
            linhadecima = linhadecima + "+"
            linhadomeio = linhadomeio + "|"
            linhadebaixo = linhadebaixo + "+"         
    print(linhadecima)
    print(linhadomeio)
    print(linhadebaixo)
imprimenormal(numeros,inicio,meio,fim)




def imprimelista(numeros, inicio, meio, fim):
    linhadecima = ""
    linhadebaixo = ""
    linhadomeio = ""
    for i, valor in enumerate(numeros):
        if i < inicio:
            linhadomeio = linhadomeio + "      "
            linhadecima = linhadecima + "      "
            linhadebaixo = linhadebaixo + "      "
        elif i == meio:
            linhadomeio = linhadomeio + ("||" + format(valor, "03d") + "|")
            linhadecima = linhadecima + "+====="
            linhadebaixo = linhadebaixo + "+====="
        else:
            linhadomeio = linhadomeio + ("| " + format(valor, "03d") + " ")
            linhadecima = linhadecima + "+-----"
            linhadebaixo = linhadebaixo + "+-----"
        if i == fim:
            linhadecima = linhadecima + "+"
            linhadomeio = linhadomeio + "|"
            linhadebaixo = linhadebaixo + "+"
            
            print(linhadecima)
            print(linhadomeio)
            print(linhadebaixo)


    
    
#buscabinária
def buscaBinaria(numeros, procurado):
    inicio = 0
    fim = len(numeros)-1
    while inicio <= fim:
        meio = (inicio + fim)//2
        #desenho
        if numeros[meio] == procurado:
            imprimelista(numeros, inicio, meio, fim)
            print("Encontrado na posicao:", meio)
            return meio
        elif numeros[meio] > procurado: #antes do meio
            imprimelista(numeros, inicio, meio, fim)
            fim = meio - 1
            #antes = (numeros[0:fim+1]) 
            #print("")
            #desenho(antes)
            continue
        else: #depois do meio
            imprimelista(numeros, inicio, meio, fim)
            inicio = meio + 1
            
    
#ordenada
if (numeros != ordenada):
    print("Lista nao ordenada")
    exit()
else:
    buscaBinaria(numeros, procurado)
    if procurado not in numeros:
        print("O elemento nao foi encontrado")






    



















