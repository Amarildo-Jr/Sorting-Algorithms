# Algoritmos de Ordenação

> Este trabalho foi desenvolvido na linguagem Python com o intuito de fazer a comparação entre os algoritmos de ordenação para entradas variadas(100-200.000) e três tipos de entradas: vetor aleatório, vetor ordenado em ordem crescente e decrescente. 
> Atividade feita para a disciplina de Projeto e Análise de Algoritmos do curso de Ciência da Computação.

>

## Requisitos para execução

- Para acessar os recursos deste trabalho e interagir basta baixar o projeto e executar o arquivo app.py, responsável por implementar a aplicação do trabalho.
- Além disso, é necessário ter instalado a biblioteca Matplotlib, utilizada para gerar os gráficos. Para instalar utilizando o pip(gerenciador de pacotes do Python), é só digitar o comando
    
    ```
    pip install matplotlib
    ```

## Cálculo do tempo

- Para calcular o tempo de execução de cada algoritmo, foi utilizada a biblioteca timeIt, por retornar o tempo mais preciso ao invés de obter o tempo através da marcação do tempo, subtraindo o valor final do inicial

## Números Aleatórios

- O algoritmo utilizado para gerar uma lista com valores aleatórios está contido no arquivo gerar_numeros.py, que recebe a entrada e o valor máximo que pode-se assumir dentro daquele intervalo.
- Os valores aleatórios resultantes são salvos no arquivo numeros.txt

## Executando

Para utilizar o projeto para a comparação dos algoritmos, basta seguir os passos a seguir:
1. Após executar o app.py, deve-se definir uma entrada através da opção 1 e selecionar o tamanho correspondente.
2. Após isso, executar os algoritmos com a opção 2. Neste caso, os algoritmos já são executados três vezes e o tempo resultante é a média das três execuções.
3. Ainda é possível visualizar no console os valores de tempo para cada algoritmo e o numero de comparações, basta escolher a opção 3. 
4. Ademais, você pode gerar os gráficos para uma melhor comparação entre cada um(opção 4).
