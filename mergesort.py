from cmath import inf

comparison_quantity = 0

def add_comparision_quantity():
    global comparison_quantity
    comparison_quantity += 1

def get_comparision_quantity_mergesort():
    return comparison_quantity

def mergesort(A, p, u):
    add_comparision_quantity()
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
        add_comparision_quantity()
        L[i] = A[p + i]
    add_comparision_quantity()

    for j in range(0, n2):
        add_comparision_quantity()
        R[j] = A[q + j + 1]
    L[n1] = float(inf)
    R[n2] = float(inf)
    add_comparision_quantity()

    j = 0
    i = 0

    for k in range(p, u + 1):
        add_comparision_quantity()

        add_comparision_quantity()
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    add_comparision_quantity()

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(mergesort(vetor, 0, len(vetor) - 1))