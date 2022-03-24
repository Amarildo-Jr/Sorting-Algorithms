def quickSortAlt(A, p, u):
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
        quickSortAlt(A, p, j)
    if u > i:
        quickSortAlt(A, i, u)
    return A

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    aux = A[i + 1]
    A[i + 1] = A[r]
    A[r] = aux
    return i + 1

# vetor = [8, 27, 9, 6, 16, 21, 5, 3, 26, 10, 15, 17, 29, 24, 14]
# print(quickSortAlt(vetor, 0, len(vetor) - 1))
# print(quicksort(vetor, 0, len(vetor) - 1))