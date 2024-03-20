#Selection do Livro
def menor(lista):
    minimo = lista[0]
    menor_index = 0
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            menor_index = i
    return menor_index

def selectionSort(lista):
    nLista = []
    for i in range(len(lista)):
        min = menor(lista)
        nLista.append(lista.pop(min))
    return nLista

lista = [7, 5, 1, 8, 3]
print(selectionSort(lista))

#algoritmo do cara

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    return lista


lista = [7, 5, 1, 8, 3]
print(selection_sort(lista))
