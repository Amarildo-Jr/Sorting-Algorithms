comparison_quantity_bubble = 0
ordened = True

def add_comparision_quantity():
    global comparison_quantity_bubble
    comparison_quantity_bubble += 1


def get_comparision_quantity_bubblesort():
    return comparison_quantity_bubble


def bubblesort(array, chamador):
    global comparison_quantity_bubble
    comparison_quantity_bubble = 0
    length = len(array)
    result = True
    while result:
        add_comparision_quantity()
        result = False
        i = 0
        while (i < length-1):
            add_comparision_quantity()

            add_comparision_quantity()
            if (array[i] > array[i+1]):
                tempVar = array[i]
                array[i] = array[i+1]
                array[i+1] = tempVar
                result = True
                if chamador == "hybrid":
                    return array, False
            i = i+1
        add_comparision_quantity()

    add_comparision_quantity()

    return array, ordened

# vetor = [5, 8, 3, 6, 9, 0, 2, 4, 1, 7, 10] #Caso para teste de ordenacao
# print(bubblesort(vetor))
