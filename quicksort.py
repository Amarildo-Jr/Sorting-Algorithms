def quicksort(A, p, u):
    i = p
    j = u
    x = A[(p + u)//2]
    while i <= j:
        while A[i] < x:
            i = i + 1
        while A[j] > x:
            j = j - 1
        if i <= j:
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            i = i + 1
            j = j - 1
    if p < j:
        quicksort(A, p, j)
    if u > i:
        quicksort(A, i, u)
    return A

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(quicksort(vetor, 0, len(vetor) - 1))