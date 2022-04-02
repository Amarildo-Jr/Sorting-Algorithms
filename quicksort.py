comparison_quantity_quicksort = 0

def add_comparision_quantity():
    global comparison_quantity_quicksort
    comparison_quantity_quicksort += 1

def get_comparision_quantity_quicksort():
    print("quick comp: ", id(comparison_quantity_quicksort))
    return comparison_quantity_quicksort

def quicksort(A, p, u):
    global comparison_quantity_quicksort
    comparison_quantity_quicksort = 0
    i = p
    j = u
    x = A[(p + u)//2]

    while i <= j:
        add_comparision_quantity()

        while A[i] < x:
            add_comparision_quantity()
            i = i + 1
        add_comparision_quantity()

        while A[j] > x:
            add_comparision_quantity()
            j = j - 1
        add_comparision_quantity()

        add_comparision_quantity()
        if i <= j:
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            i = i + 1
            j = j - 1
    add_comparision_quantity()

    add_comparision_quantity()
    if p < j:
        quicksort(A, p, j)
    
    add_comparision_quantity()
    if u > i:
        quicksort(A, i, u)
        
    return A

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(quicksort(vetor, 0, len(vetor) - 1))