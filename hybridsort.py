from quicksort import quicksort, get_comparision_quantity_quicksort
from bubblesort import bubblesort, get_comparision_quantity_bubblesort

comparison_quantity_hybrid = 0

def get_comparision_quantity_hybridsort():
    return comparison_quantity_hybrid

def hybridsort(vetor):
    vetor, ordened = bubblesort(vetor, "hybrid") 
    global comparison_quantity_hybrid
    comparison_quantity_hybrid = 0
    if ordened:
        comparison_quantity_hybrid = get_comparision_quantity_bubblesort()
        return vetor

    vetorOrdenado = quicksort(vetor, 0, len(vetor) - 1, True)
    comparison_quantity_hybrid += get_comparision_quantity_quicksort()
    return vetorOrdenado