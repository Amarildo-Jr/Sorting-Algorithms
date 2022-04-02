from quicksort import quicksort
from bubblesort import bubblesort
from gerar_numeros import gerar_numeros 

def hybridsort(vetor):
    vetor, ordened = bubblesort(vetor) 
    if ordened:
        return vetor

    return quicksort(vetor, 0, len(vetor) - 1)