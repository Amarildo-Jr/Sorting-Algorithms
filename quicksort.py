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