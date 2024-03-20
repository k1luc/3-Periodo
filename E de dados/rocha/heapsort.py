def maxheapify(A, n, i):
    maior = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[left] > A[i]:
        maior = left
    if right < n and A[right] > A[maior]:
        maior = right
    if maior != i:
        (A[i], A[maior]) = (A[maior], A[i])
        maxheapify(A, n, maior)

def heapsort(A):
    n = len(A)
    for i in range(n//2-1, -1, -1):
        maxheapify(A, n, i)
    for i in range(n-1, 0, -1):
        (A[i], A[0]) = (A[0], A[i])
        maxheapify(A, i, 0)

if __name__ == "__main__":
    A = [4, 7, 12, 3, 10, 2, 15, 1, 9, 6, 13, 5, 8, 14, 11]
    print(f"Vetor A: {A}")
    heapsort(A)
    print(f"Vetor Ordenado: {A}")