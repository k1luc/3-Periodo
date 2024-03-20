
def pesquisaBin(lista, valor):
    baixo = 0
    alto = len(lista)-1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == valor:
            return meio
        elif chute > valor:
            alto = meio - 1
        elif chute < valor:
            baixo = meio + 1
        else:
            return None
    
lista = [1, 3, 5, 10, 23, 55, 99]


print(pesquisaBin(lista, 55))
print(pesquisaBin(lista, 3))
print(pesquisaBin(lista, 4))
print(pesquisaBin(lista, 99))
