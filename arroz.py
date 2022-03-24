import main
from insertionsort import insertionsort
from bubblesort import bubblesort
from quicksort import quicksort
from mergesort import mergesort
from heapsort import heapsort
from gerar_numeros import gerar_numeros

var_pior = 'pior'
var_melhor = 'melhor'
var_random = 'random'

print('gerando numeros >')
gerar_numeros(quantidade=500, maximo=500)

lista = main.get_lista()
listam, listap = main.get_melhor_pior_caso(lista)

main.calcular_tempo_timeit(lista, var_random)
main.calcular_tempo_timeit(listam, var_melhor)
main.calcular_tempo_timeit(listap, var_pior)

print('gerando os graficos > ')
#gera os gráficos dos tempos
main.get_valores_pro_grafico(var_random, len(lista))
main.get_valores_pro_grafico(var_pior, len(lista))
main.get_valores_pro_grafico(var_melhor, len(lista))

# print(lista, listam, listap, sep="\n")
# main.vendo_listas(lista, listam, listap)