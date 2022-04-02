from fileinput import close
import matplotlib.pyplot as plt
import os, timeit, time
from insertionsort import insertionsort, get_comparision_quantity_insertionsort
from bubblesort import bubblesort, get_comparision_quantity_bubblesort
from quicksort import quicksort, get_comparision_quantity_quicksort
from mergesort import mergesort, get_comparision_quantity_mergesort
from heapsort import heapsort, get_comparision_quantity_heapsort

def get_lista():
    lista_int = []
    file = open(os.getcwd()+'/numeros.txt', 'r')
    lista = file.read()
    file.close()

    tmp = ''

    for i in lista:
        if i != '\n':
            tmp += str(i)
        else:
            lista_int.append(int(tmp))
            tmp = ''

    return lista_int

def get_melhor_pior_caso(lista_int):
    print('>>>processando lista ordenada em ordem crescente e outra em decrescente')

    lista_m = sorted(lista_int)
    lista_p = []
    for i in range(len(lista_m)):
        pos = len(lista_m) - i
        lista_p.append(lista_m[pos - 1])
    print('>>>listas criadas ')
    return lista_m, lista_p,

def vendo_listas(lista_int,lista_m, lista_p):
    print('lista aleatoria = ', lista_int, ' tam = ', len(lista_int))
    print('lista ja ordenada = ', lista_m, ' tam = ', len(lista_m))
    print('lista ordenada inversamente = ', lista_p, ' tam = ', len(lista_p))

def calcular_tempo_hibrido_timeit(lista, caso):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd() +'/timeIt/' + "temposHibridoTimeit" + caso + str(len(lista)) +'.txt'

    arquivo = open(name_file, operacao)

    #calculando o hybridsort()
    print('>>> calculando hybridsort em caso ', caso)
    tempo_hybridsort = 0
    for i in range (0, 3):
        tempo_hybridsort += timeit.timeit("hybridsort({})".format(lista), setup="from main import hybridsort", number=1)
    tempo_hybridsort /= 3
    arquivo.write("Hybridsort " + caso + ": "  + str(float(tempo_hybridsort)) + "; comparacoes: " + str(get_comparision_quantity_bubblesort() + get_comparision_quantity_quicksort()) + '\n')
    print('hybrid done.')

    arquivo.close()

def calcular_tempo_timeit(lista, caso):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd() +'/timeIt/' + "temposTimeit" + caso + str(len(lista)) +'.txt'
    name_file1 = os.getcwd() +'/timeIt/' + "temposApenasNum" + caso + str(len(lista)) +'.txt'

    name_file_comparisons = os.getcwd() +'/comparisons/' + "comparacoesApenasNum" + caso + str(len(lista)) +'.txt'

    arquivo = open(name_file, operacao)
    arquivo1 = open(name_file1, operacao)
    arquivo2 = open(name_file_comparisons, operacao)

    #calculando o InsertionSort()
    print('>>> calculando insertionsort em caso ', caso)
    tempo_insertionSort = 0
    for i in range (0, 3):
        tempo_insertionSort += timeit.timeit("insertionsort({})".format(lista), setup="from __main__ import insertionsort", number=1)
    tempo_insertionSort /= 3
    arquivo.write("InsertionSort " + caso + ": "  + str(float(tempo_insertionSort)) + "; comparacoes: " + str(get_comparision_quantity_insertionsort()) + '\n')
    arquivo1.write(str(float(tempo_insertionSort))+'\n')
    arquivo2.write(str(get_comparision_quantity_insertionsort())+'\n')
    print('insertion done.')

    print('>>> calculando bubble em caso ', caso)
    # calculando o BubbleSort()
    tempo_BubbleSort = 0
    for i in range (0, 3):
        tempo_BubbleSort = timeit.timeit("bubblesort({})".format(lista), setup="from __main__ import bubblesort", number=1)
    tempo_BubbleSort /= 3
    arquivo.write("BubbleSort " + caso + ": "  + str(float(tempo_BubbleSort)) + "; comparacoes: " + str(get_comparision_quantity_bubblesort()) + '\n')
    arquivo1.write(str(float(tempo_BubbleSort))+'\n')
    arquivo2.write(str(get_comparision_quantity_bubblesort())+'\n')
    print('bubble done.')

    # calculando o HeapSort()
    print('>>> calculando heap em caso ', caso)
    tempo_HeapSort = 0
    for i in range (0, 3):
        tempo_HeapSort = timeit.timeit("heapsort({})".format(lista), setup="from __main__ import heapsort", number=1)
    tempo_HeapSort /= 3
    arquivo.write("HeapSort " + caso + ": "  + str(float(tempo_HeapSort))+ "; comparacoes: " + str(get_comparision_quantity_heapsort()) + '\n')
    arquivo1.write(str(float(tempo_HeapSort))+'\n')
    arquivo2.write(str(get_comparision_quantity_heapsort())+'\n')
    print('heap done.')

    # calculando o QuickSort()
    print('>>> calculando quick em caso ', caso)
    tempo_QuickSort = 0
    for i in range (0, 3):
        tempo_QuickSort = timeit.timeit("quicksort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import quicksort", number=1)
    tempo_QuickSort /= 3
    arquivo.write("QuickSort " + caso + ": "  + str(float(tempo_QuickSort)) + "; comparacoes: " + str(get_comparision_quantity_quicksort()) + '\n')
    arquivo1.write(str(float(tempo_QuickSort))+'\n')
    arquivo2.write(str(get_comparision_quantity_quicksort())+'\n')
    print('quick done.')

    # calculando o MergeSort()
    print('>>> calculando merge em caso ', caso)
    tempo_MergeSort = 0
    for i in range (0, 3):
        tempo_MergeSort = timeit.timeit("mergesort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import mergesort", number=1)
    tempo_MergeSort /= 3
    arquivo.write("MergeSort " + caso + ": " + str(float(tempo_MergeSort))+ "; comparacoes: " + str(get_comparision_quantity_mergesort()) + '\n')
    arquivo1.write(str(float(tempo_MergeSort))+'\n')
    arquivo2.write(str(get_comparision_quantity_mergesort())+'\n')
    print('merge done.')

    arquivo.close()
    arquivo1.close()
    arquivo2.close()

def calcular_tempo_fim_menos_inicio(lista):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd()+'/fim-Inicio/'+ "tempoFim-Inicio" + str(len(lista)) + '.txt'
    arquivo = open(name_file, operacao)

    #calculando o InsertionSort()
    inicio = time.time()
    insertionsort(lista)
    fim = time.time()
    tempo_insertionSort = fim-inicio
    arquivo.write("InsertionSort" + str(float(tempo_insertionSort))+'\n')

    # calculando o BubleSort()
    inicio = time.time()
    bubblesort(lista)
    fim = time.time()
    tempo_BubbleSort = fim - inicio
    arquivo.write("BubbleSort" + str(float(tempo_BubbleSort))+'\n')

    # calculando o HeapSort()
    inicio = time.time()
    heapsort(lista)
    fim = time.time()
    tempo_heapSort = fim - inicio
    arquivo.write("HeapSort" + str(float(tempo_heapSort))+'\n')

    # calculando o QuickSort()
    inicio = time.time()
    quicksort(lista, 0, len(lista) - 1)
    fim = time.time()
    tempo_quickSort = fim - inicio
    arquivo.write("QuickSort" + str(float(tempo_quickSort))+'\n')

    # calculando o MergeSort()
    inicio = time.time()
    mergesort(lista, 0, len(lista) - 1)
    fim = time.time()
    tempo_mergeSort = fim - inicio
    arquivo.write("MergeSort" + str(float(tempo_mergeSort))+'\n')
    arquivo.close()

def gerar_grafico(insertion, buble, quick, heap, merge, tipo, tamanho):
    ''''''

    y_axis = [insertion, buble, quick, heap, merge]
    x_axis = range(len(y_axis))
    width_n = 0.4
    bar_color = 'green'
    algoritmos = ['insertion', 'bubble', 'quick', 'heap', 'merge']

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Algoritmos')
    plt.xticks(x_axis, algoritmos, rotation='vertical')
    plt.title('Caso '+str(tipo)+' de tamanho '+str(tamanho))
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.getcwd()+'/_plot/tempos-'+str(tipo)+str(tamanho)+'.png')
    print('>>> figura ', tipo, '.png salva!')
    plt.show()

def gerar_grafico_comparacoes(comp_insertion, comp_bubble, comp_quick, comp_heap, comp_merge, tipo, tamanho):

    y_axis = [comp_insertion, comp_bubble, comp_quick, comp_heap, comp_merge]
    x_axis = range(len(y_axis))
    width_n = 0.4
    bar_color = 'blue'
    algoritmos = ['insertion', 'bubble', 'quick', 'heap', 'merge']

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
    plt.ylabel('Comparações')
    plt.xlabel('Algoritmos')
    plt.xticks(x_axis, algoritmos, rotation='vertical')
    plt.title('Caso '+str(tipo)+' de tamanho '+str(tamanho))
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.getcwd()+'/_plot/comparacoes-'+str(tipo)+str(tamanho)+'.png')
    print('>>> figura ', tipo, '.png salva!')
    plt.show()

def get_valores_pro_grafico(tipo, tam, valor_tipo):
    ''''''
    arquivo = ""
    if valor_tipo == "tempo":
        arquivo = open(os.getcwd()+'/timeIt/temposApenasNum'+str(tipo)+str(tam)+'.txt', 'r')
    else:
        arquivo = open(os.getcwd()+'/comparisons/comparacoesApenasNum'+str(tipo)+str(tam)+'.txt', 'r')

    valores = arquivo.read()
    # print(valores)
    arquivo.close()
    insertion = 0
    bubble = 0
    quick = 0
    heap = 0
    merge = 0
    tmp = ''
    v1 = True
    v2 = False
    v3 = False
    v4 = False
    v5 = False
    for i in range(len(valores)):

        if valores[i] == '\n':
            if insertion == 0 and v1:
                insertion = tmp
                tmp = ''
                v1 = False
                v2 = True
            elif bubble == 0 and v2:
                bubble = tmp
                tmp = ''
                v2 = False
                v3 = True
            elif quick == 0 and v3:
                quick = tmp
                tmp = ''
                v3 = False
                v4 = True
            elif heap == 0 and v4:
                heap = tmp
                tmp = ''
                v4 = False
                v5 = True
            elif merge == 0 and v5:
                merge = tmp
                tmp = ''
        else:
            tmp += valores[i]
    print('insertion = ', insertion, ' bubble = ', bubble, 'quick = ', quick, ' heap = ', heap, ' merge = ', merge)

    a = float(insertion)
    b = float(bubble)
    c = float(quick)
    d = float(heap)
    e = float(merge)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    if valor_tipo == "tempo":
        gerar_grafico(a,b,c,d,e,tipo=tipo, tamanho=tam)
    else:
        gerar_grafico_comparacoes(a,b,c,d,e,tipo=tipo, tamanho=tam)

def mostrarResultados(tipo, tam):
    arquivo = open(os.getcwd()+'/timeIt/temposTimeit'+str(tam)+str(tipo)+'.txt', 'r')
    valores = arquivo.read()
    arquivo.close()
    print("\nAlgoritmo->caso->tempo(s)->n de comparacoes\n")
    print(valores)