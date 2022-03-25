from cmath import inf

def mergesort(A, p, u):
    if p < u:
        q = (p + u)//2
        mergesort(A, p, q)
        mergesort(A, q + 1, u)
        merge(A, p, q, u)
    return A

def merge(A, p, q, u):
    n1 = q - p + 1
    n2 = u - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = float(inf)
    R[n2] = float(inf)
    j = 0
    i = 0
    for k in range(p, u + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    
# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(mergesort(vetor, 0, len(vetor) - 1))