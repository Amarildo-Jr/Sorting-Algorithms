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
        aux = vetor[0]
        vetor[0] = vetor[i]
        vetor[i] = aux
        heap_size -= 1
        max_heapify(vetor, 0, heap_size)
    return vetor

def build_max_heap(vetor):
    for i in range((len(vetor) - 1)//2, -1, -1):
        max_heapify(vetor, i, len(vetor) - 1)
    
    return vetor

def max_heapify(vetor, i, heap_size):
    l = left(i)
    r = right(i)
    higher = 0
    
    if l <= heap_size and vetor[l] > vetor[i]:
        higher = l
    else:
        higher = i
    
    if r <= heap_size and vetor[r] > vetor[higher]:
        higher = r
    if higher != i:
        aux = vetor[i]
        vetor[i] = vetor[higher]
        vetor[higher] = aux

        max_heapify(vetor, higher, heap_size)

vetor1 = [4,1,3,2,16,9,10,14,8,7]
vetor2 = [4,1,3,2,16,9,10,14,8,7]

print(build_max_heap(vetor1)) 
print(heapsort(vetor2))