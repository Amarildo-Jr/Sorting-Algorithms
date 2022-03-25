def insertionsort(vetor):
    x = 0
    j = 0
    for i in range(1, len(vetor)):
        x = vetor[i]
        j = i - 1
        while j >= 0 and x < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = x
    return vetor

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(insertionsort(vetor))