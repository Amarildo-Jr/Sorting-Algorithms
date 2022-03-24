import os
from random import randint

def gerar_numeros(quantidade, maximo):
    '''gerar numeroa inteirps aleatorios'''

    lista = []
    for i in range(quantidade):
        lista.append(randint(0, maximo))

    print('quantidade de elementos gerados = ', len(lista))
    print(lista)
    file = open(os.getcwd() + '/numeros.txt', 'w')
    for i in range(len(lista)):
        if i == 999:
            file.write(str(lista[i]))
        else:
            file.write(str(lista[i])+'\n')
    file.close()


if __name__ == '__main__':
    gerar_numeros(quantidade=500, maximo=500)