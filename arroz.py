import matplotlib.pyplot as plt
import os

def gerar_grafico(y_axis_crescente, y_axis_decrescente, y_axis_random, tamanho):
    ''''''
    
    x_axis_crescente = range(len(y_axis_crescente))
    x_axis_decrescente = range(len(y_axis_decrescente))
    x_axis_random = range(len(y_axis_random))
    algoritmos = ['insertion', 'bubble', 'quick', 'heap', 'merge']

    plt.plot(x_axis_crescente, y_axis_crescente, label="Crescente")
    plt.plot(x_axis_decrescente, y_axis_decrescente, label="Decrescente")
    plt.plot(x_axis_random, y_axis_random, label="Aleatório")
    plt.legend()

    plt.ylabel('Tempo(s)')
    plt.xlabel('Algoritmos')

    plt.xticks(x_axis_crescente, algoritmos, rotation='vertical')
    plt.xticks(x_axis_decrescente, algoritmos, rotation='vertical')
    plt.xticks(x_axis_random, algoritmos, rotation='vertical')

    plt.title('Caso '+'de tamanho '+str(tamanho))
    plt.tight_layout()
    plt.grid(True)

    plt.savefig(os.getcwd()+'/_plot2/tempos-'+str(tamanho)+'.png')
    print('>>> figura ', str(tamanho), '.png salva!')
    plt.close()
    # plt.show()

def gerar_grafico_comparacoes(y_axis_crescente, y_axis_decrescente, y_axis_random, tamanho):

    x_axis_crescente = range(len(y_axis_crescente))
    x_axis_decrescente = range(len(y_axis_decrescente))
    x_axis_random = range(len(y_axis_random))
    algoritmos = ['insertion', 'bubble', 'quick', 'heap', 'merge']

    plt.plot(x_axis_crescente, y_axis_crescente, label="Crescente")
    plt.plot(x_axis_decrescente, y_axis_decrescente, label="Decrescente")
    plt.plot(x_axis_random, y_axis_random, label="Aleatório")
    plt.legend()
    algoritmos = ['insertion', 'bubble', 'quick', 'heap', 'merge']

    plt.ylabel('Comparações')
    plt.xlabel('Algoritmos')

    plt.xticks(x_axis_crescente, algoritmos, rotation='vertical')
    plt.xticks(x_axis_decrescente, algoritmos, rotation='vertical')
    plt.xticks(x_axis_random, algoritmos, rotation='vertical')
    
    plt.title('Caso '+' de tamanho '+str(tamanho))
    plt.tight_layout()
    plt.grid(True)

    plt.savefig(os.getcwd()+'/_plot2/comparacoes-'+str(tamanho)+'.png')
    print('>>> figura ', '.png salva!')
    plt.close()
    # plt.show()


def get_valores_pro_grafico(tam, valor_tipo):
    ''''''
    if valor_tipo == "tempo":
        arquivo_crescente = open(os.getcwd()+'/timeIt/temposApenasNum'+"crescente"+str(tam)+'.txt', 'r')
        arquivo_decrescente = open(os.getcwd()+'/timeIt/temposApenasNum'+"decrescente"+str(tam)+'.txt', 'r')
        arquivo_random = open(os.getcwd()+'/timeIt/temposApenasNum'+"random"+str(tam)+'.txt', 'r')
    else:
        arquivo_crescente = open(os.getcwd()+'/comparisons/comparacoesApenasNum'+"crescente"+str(tam)+'.txt', 'r')
        arquivo_decrescente = open(os.getcwd()+'/comparisons/comparacoesApenasNum'+"decrescente"+str(tam)+'.txt', 'r')
        arquivo_random = open(os.getcwd()+'/comparisons/comparacoesApenasNum'+"random"+str(tam)+'.txt', 'r')

    arquivos = [arquivo_crescente, arquivo_decrescente, arquivo_random]
    valores_por_tipo = []
    for i in range(0, len(arquivos)):
        valores = arquivos[i].read()

        arquivos[i].close()
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
        for j in range(len(valores)):

            if valores[j] == '\n':
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
                tmp += valores[j]
        print('insertion = ', insertion, ' bubble = ', bubble, 'quick = ', quick, ' heap = ', heap, ' merge = ', merge)
        valores_por_tipo.append([float(insertion), float(bubble), float(quick), float(heap), float(merge)])

        
    if valor_tipo == "tempo":
        gerar_grafico(valores_por_tipo[0],valores_por_tipo[1],valores_por_tipo[2], tamanho=tam)
    else:
        gerar_grafico_comparacoes(valores_por_tipo[0],valores_por_tipo[1],valores_por_tipo[2], tamanho=tam)

if __name__ == "__main__":
    get_valores_pro_grafico(100, "tempo")
    get_valores_pro_grafico(500, "tempo")
    get_valores_pro_grafico(1000, "tempo")
    get_valores_pro_grafico(5000, "tempo")
    get_valores_pro_grafico(30000, "tempo")
    get_valores_pro_grafico(50000, "tempo")
    get_valores_pro_grafico(100000, "tempo")
    get_valores_pro_grafico(150000, "tempo")
    #get_valores_pro_grafico(200000, "tempo")

    get_valores_pro_grafico(100, "comparacoes")
    get_valores_pro_grafico(500, "comparacoes")
    get_valores_pro_grafico(1000, "comparacoes")
    get_valores_pro_grafico(5000, "comparacoes")
    get_valores_pro_grafico(30000, "comparacoes")
    get_valores_pro_grafico(50000, "comparacoes")
    get_valores_pro_grafico(100000, "comparacoes")
    get_valores_pro_grafico(150000, "comparacoes")
    #get_valores_pro_grafico(200000, "comparacoes")