from fileinput import close
import os, timeit, time
import matplotlib.pyplot as plt
from insertionsort import insertionsort
from bubblesort import bubblesort
from quicksort import quicksort
from mergesort import mergesort
from heapsort import heapsort

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

def calcular_tempo_timeit(lista, caso):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd() +'/timeIt/' + "temposTimeit" + caso + str(len(lista)) +'.txt'
    name_file1 = os.getcwd() +'/timeIt/' + "temposApenasNum" + caso + str(len(lista)) +'.txt'
    arquivo = open(name_file, operacao)
    arquivo1 = open(name_file1, operacao)

    #calculando o InsertionSort()
    print('>>> calculando insertionsort em caso ', caso)
    tempo_insertionSort = timeit.timeit("insertionsort({})".format(lista), setup="from __main__ import insertionsort", number=1)
    arquivo.write("InsertionSort " + caso + " :"  + str(float(tempo_insertionSort))+'\n')
    arquivo1.write(str(float(tempo_insertionSort))+'\n')
    print('insertion done.')

    print('>>> calculando bubble em caso ', caso)
    # calculando o BubbleSort()
    tempo_BubbleSort = timeit.timeit("bubblesort({})".format(lista), setup="from __main__ import bubblesort", number=1)
    arquivo.write("BubbleSort: " + caso + " :"  + str(float(tempo_BubbleSort))+'\n')
    arquivo1.write(str(float(tempo_BubbleSort))+'\n')
    print('bubble done.')

    # calculando o HeapSort()
    print('>>> calculando heap em caso ', caso)
    tempo_HeapSort = timeit.timeit("heapsort({})".format(lista), setup="from __main__ import heapsort", number=1)
    arquivo.write("HeapSort: " + caso + " :"  + str(float(tempo_HeapSort))+'\n')
    arquivo1.write(str(float(tempo_HeapSort))+'\n')
    print('heap done.')

    # calculando o QuickSort()
    print('>>> calculando quick em caso ', caso)
    tempo_QuickSort = timeit.timeit("quicksort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import quicksort", number=1)
    arquivo.write("QuickSort: " + caso + " :"  + str(float(tempo_QuickSort))+'\n')
    arquivo1.write(str(float(tempo_QuickSort))+'\n')
    print('quick done.')

    # calculando o MergeSort()
    print('>>> calculando merge em caso ', caso)
    tempo_MergeSort = timeit.timeit("mergesort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import mergesort", number=1)
    arquivo.write("MergeSort " + caso + " :" + str(float(tempo_MergeSort))+'\n')
    arquivo1.write(str(float(tempo_MergeSort))+'\n')
    print('merge done.')

    arquivo.close()
    arquivo1.close()

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

def gerar_grafico(insertion, buble, quick, tipo):
    ''''''
    y_axis = [insertion, buble, quick]
    x_axis = range(len(y_axis))
    width_n = 0.4
    bar_color = 'green'
    algortirmos = ['insertion', 'buble', 'quick']

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
    plt.ylabel('Tempo')
    plt.xlabel('Algoritmos')
    plt.xticks(x_axis, algortirmos, rotation='vertical')
    plt.title('Caso '+str(tipo))
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.getcwd()+'/_plot/'+str(tipo)+'.png')
    print('>>> figura ', tipo, '.png salva!')
    plt.show()

def get_valores_pro_grafico(tipo, tam):
    ''''''
    arquivo = open(os.getcwd()+'/timeIt/temposApenasNum'+str(tipo)+str(tam)+'.txt', 'r')
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
    #implementar o v4, v5 para permitirem que o grafico contenha tambem o heap, merge
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
        else:
            tmp += valores[i]

        # print(valores[i])
    print('s = ', insertion, ' b1 = ', bubble, ' b2 = ', quick)

    a = float(insertion[:10])
    b = float(bubble[:10])
    c = float(quick[:10])
    gerar_grafico(a,b,c,tipo=tipo)