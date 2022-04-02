from quicksort import quicksort
from bubblesort import bubblesort
from gerar_numeros import gerar_numeros 
import timeit
import main

def hybridsort(vetor):
    vetor, ordened = bubblesort(vetor) 
    if ordened:
        return vetor
    
    return quicksort(vetor, 0, len(vetor) - 1)

gerar_numeros(150000, 150000)

lista = main.get_lista()
listam, listap = main.get_melhor_pior_caso(lista)

print(timeit.timeit("hybridsort({})".format(listam), setup="from __main__ import hybridsort", number=1))