
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave
    return lista


lista = [21, 5, 3, 45, 5, 21, 7, 1]
print(insertion_sort(lista))