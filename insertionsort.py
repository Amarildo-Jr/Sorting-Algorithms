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

vetor = [4,1,3,2,16,9,10,14,8,7]

print(insertionsort(vetor))