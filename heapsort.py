comparison_quantity = 0

def add_comparision_quantity():
    global comparison_quantity
    comparison_quantity += 1

def get_comparision_quantity_heapsort():
    return comparison_quantity

def parent(i):
    return i/2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapsort(vetor):
    build_max_heap(vetor)
    heap_size = len(vetor) - 1
    
    for i in range(len(vetor)-1, 0, -1):
        add_comparision_quantity()
        aux = vetor[0]
        vetor[0] = vetor[i]
        vetor[i] = aux
        heap_size -= 1
        max_heapify(vetor, 0, heap_size)
    add_comparision_quantity()

    return vetor

def build_max_heap(vetor):
    for i in range((len(vetor) - 1)//2, -1, -1):
        add_comparision_quantity()
        max_heapify(vetor, i, len(vetor) - 1)
    add_comparision_quantity()
    return vetor

def max_heapify(vetor, i, heap_size):
    l = left(i)
    r = right(i)
    higher = 0
    
    add_comparision_quantity()
    if l <= heap_size and vetor[l] > vetor[i]:
        higher = l
    else:
        higher = i
    
    add_comparision_quantity()
    if r <= heap_size and vetor[r] > vetor[higher]:
        add_comparision_quantity()
        higher = r
        
    add_comparision_quantity()
    if higher != i:
        aux = vetor[i]
        vetor[i] = vetor[higher]
        vetor[higher] = aux

        max_heapify(vetor, higher, heap_size)

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(heapsort(vetor))