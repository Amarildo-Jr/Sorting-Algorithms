import main
from insertionsort import insertionsort
from bubblesort import bubblesort
from quicksort import quicksort
from mergesort import mergesort
from heapsort import heapsort
from gerar_numeros import gerar_numeros

var_decrescente = 'decrescente'
var_crescente = 'crescente'
var_random = 'random'

option = 1
algoritmos_executados = False
lista, listam, listap = [], [], []
print("\nBem-vindo a aplicacao dos Algoritmos de ordenacao. \nPara iniciar, defina uma entrada e após isso execute os algoritmos.",
    "\nPor ultimo pode gerar os graficos de comparacao com o tempo de cada")
while option:
    print("\n0. Sair da aplicação",
    "1. Gerar uma entrada de numeros com determinado tamanho", 
    "2. Executar os algoritmos e salvar os tempos de ordenacao de cada",
    "3. Verificar os graficos de comparacao de cada", 
    "4. Vizualizar as listas: aleatoria, ordenada e ordenada inversamente", sep="\n")
    option = int(input("Digite a opcao desejada: "))
    if option == 1:
        quantidade_numeros = 0
        opcao_correta = True
        print("\nTamanhos da entrada\n a) 100", " b) 500", " c) 1.000", " d) 5.000", " e) 30.000", " f) 50.000", " g) 100.000", " h) 150.000", " i) 200.000", sep='\n')
        opcao_entrada = str(input("Digite apenas a letra da opcao corresponde ao tamanho da entrada que deseja: ")).lower()
        if 'a' in opcao_entrada:
            quantidade_numeros = 100
        elif 'b' in opcao_entrada:
            quantidade_numeros = 500
        elif 'c' in opcao_entrada:
            quantidade_numeros = 1000
        elif 'd' in opcao_entrada:
            quantidade_numeros = 5000
        elif 'e' in opcao_entrada:
            quantidade_numeros = 30000
        elif 'f' in opcao_entrada:
            quantidade_numeros = 50000
        elif 'g' in opcao_entrada:
            quantidade_numeros = 100000
        elif 'h' in opcao_entrada:
            quantidade_numeros = 150000
        elif 'i' in opcao_entrada:
            quantidade_numeros = 200000
        else:
            print("--> Digite uma entrada valida")
            opcao_correta = False
        if opcao_correta:
            print('>>>gerando numeros')
            gerar_numeros(quantidade=quantidade_numeros, maximo=quantidade_numeros - 1)
            lista = main.get_lista()
            listam, listap = main.get_melhor_pior_caso(lista)
            algoritmos_executados = False
    elif option == 2:
        if lista == [] or listam == [] or listap == []:
            print("\n--> Defina o tamanho de uma entrada antes de executar os algoritmos.")
        else:
            main.calcular_tempo_timeit(lista, var_random)
            main.calcular_tempo_timeit(listam, var_crescente)
            main.calcular_tempo_timeit(listap, var_decrescente)
            algoritmos_executados = True
    elif option == 3:
        if lista == [] or listam == [] or listap == []:
            print("\n--> Defina o tamanho de uma entrada antes de executar os algoritmos.")
        elif not algoritmos_executados:
            print("\n--> Execute os algoritmos primeiro para poder gerar os graficos")
        else:
            print('>>> gerando os graficos')
            #gera os gráficos dos tempos
            main.get_valores_pro_grafico(var_random, len(lista))
            main.get_valores_pro_grafico(var_decrescente, len(lista))
            main.get_valores_pro_grafico(var_crescente, len(lista))
    elif option == 4:
        main.vendo_listas
        main.vendo_listas(lista, listam, listap)
