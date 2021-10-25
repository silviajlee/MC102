"Roteiro do Lab. 10: https://www.ic.unicamp.br/~mc102/mc102-1s2020/labs/roteiro-lab10.html"
import copy
#entrada
padrao = []
quadros = 0
while True:
    leitura =list(input(""))
    if(leitura[0].isnumeric()):
        quadros = int("".join(leitura))
        break
    else:
        padrao.append(leitura)


def imprimir_matriz (M):
    for i in M:
        print("".join(i))

    
#matriz
def matriz (M):
    c = copy.deepcopy(M)
    for i in range (1, len(M)-1):
        for j in range (1, len(M[i])-1):
            vizinho = 0
            if (M[i-1][j])== "@":
                vizinho = vizinho + 1
            if (M[i-1][j-1]) == "@":
                vizinho = vizinho + 1
            if (M[i-1][j+1]) == "@":
                vizinho = vizinho + 1
            if (M[i][j-1]) == "@":
                vizinho = vizinho + 1
            if (M[i][j+1]) == "@":
                vizinho = vizinho + 1
            if (M[i+1][j]) == "@":
                vizinho = vizinho + 1
            if (M[i+1][j-1]) == "@":
                vizinho = vizinho + 1
            if (M[i+1][j+1]) == "@":
                vizinho = vizinho + 1
            if M[i][j] == "@" and 2<=vizinho<=3:
                c[i][j] = "@"
            else:
                c[i][j] = " "
            if M[i][j] == " " and (vizinho == 3):
                c[i][j] = "@"
    return c

imprimir_matriz(padrao)

for _ in range(quadros):
    padrao = matriz(padrao)
    imprimir_matriz(padrao)
    



            
                




