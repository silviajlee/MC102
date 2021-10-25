#"Roteiro do Lab.11: https://www.ic.unicamp.br/~mc102/mc102-1s2020/labs/roteiro-lab11.html"
#usuarios
usuario = input()
lista_nomes = []
lista_nomes.append(usuario)
while (usuario != "--"):
    usuario = input()
    lista_nomes.append(usuario)
del lista_nomes[-1]
lista_nomes.sort()


#pares de usuarios e leitura das amizades
dicionario = {}  
pares_usuario = ""
while (pares_usuario != "--"):
    pares_usuario = input()
    amigos = pares_usuario.split(" ")
    if (pares_usuario == "--"):
        break
    if (amigos[0]) in (dicionario):
        dicionario[amigos[0]].add(amigos[1])
    else:
        dicionario[amigos[0]] = {amigos[1]}
    if (amigos[1]) in (dicionario):
        dicionario[amigos[1]].add(amigos[0])
    else:
        dicionario[amigos[1]] = {amigos[0]}
#função
def comum (n1,n2):
    com = []
    for x in n1:
        if x in n2:
            com.append(x)
    for x in n2:
        if (x not in com and x in n1):
            com.append(x)
    com.sort()
    return com


#print

for i in range(len(lista_nomes)):
    for j in range (i+1, len(lista_nomes)):
        one = lista_nomes[i]
        two = lista_nomes[j]
        if one in dicionario:
            common = comum(dicionario[one], dicionario[two])
            if (len(common) == 0):
                print(one, two, ":")
            else:
                print(one, two, ":", end=" ")
                for k in range (len(common)-1):
                    print(common[k]+ ",", end=" ")
                print(common[len(common)-1])
        else:
            print(one, two, ":")

