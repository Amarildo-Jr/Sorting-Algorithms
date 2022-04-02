comparison_quantity_insertion = 0

def add_comparision_quantity():
    global comparison_quantity_insertion
    comparison_quantity_insertion += 1

def get_comparision_quantity_insertionsort():
    return comparison_quantity_insertion

def insertionsort(vetor):
    global comparison_quantity_insertion
    comparison_quantity_insertion = 0
    x = 0
    j = 0

    for i in range(1, len(vetor)):
        add_comparision_quantity()

        x = vetor[i]
        j = i - 1

        while j >= 0 and x < vetor[j]:
            add_comparision_quantity()
            add_comparision_quantity()
            vetor[j + 1] = vetor[j]
            j -= 1
        add_comparision_quantity()

        vetor[j + 1] = x
        
    add_comparision_quantity()
    return vetor

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(insertionsort(vetor))