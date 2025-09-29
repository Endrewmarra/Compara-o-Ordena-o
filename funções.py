import time
import random

#*=====Função Bubble Sort =====*#

def bubble_sort(lista):
    inicio_bubble_sort = time.perf_counter()
    fim = len(lista)
    for j in range(fim - 1):
        trocou = False
        for i in range(fim-1-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocou = True
        if not trocou:
            break
    fim_bubble_sort = time.perf_counter()
    tempo = fim_bubble_sort - inicio_bubble_sort
    return lista, tempo

#*=====Função Selection Sort =====*#

def selection_sort(lista):
    inicio_selecion_sort = time.perf_counter()
    fim = (len(lista))
    for j in range(fim):
        indice_menor = j
        for i in range(j+1, fim):
            if lista[i] < lista[indice_menor]:
                indice_menor = i
        lista[j], lista[indice_menor] = lista[indice_menor], lista[j]
    fim_selection_sort = time.perf_counter()
    tempo = fim_selection_sort - inicio_selecion_sort
    return lista, tempo

#*=================Configuração da lista=================*#

tamanho = int(input("Digite o tamanho da lista: ")) #! <---- tamanho da lista
tempo_lista_inicial = time.perf_counter() #? <---- Timer
lista = list(range(tamanho)) #? <---- Cria a lista
tempo_lista_final = time.perf_counter() #? <---- Timer
print(f'Tempo para criar a lista: {tempo_lista_final - tempo_lista_inicial:.10f} segundos') #? <---- Tempo para criar a lista

#*=================Embaralhar a lista=================*#

embaralhar = input("Deseja embaralhar a lista? (s/n): ").strip().lower() #! <---- verifica se o usuário quer embaralhar a lista
if embaralhar == 's':
    tempo_random_inicial = time.perf_counter() #? <---- Timer
    random.shuffle(lista) #? <---- Embaralha a lista
    tempo_random_final = time.perf_counter() #? <---- Timer
    print(f'Tempo para embaralhar a lista: {tempo_random_final - tempo_random_inicial:.10f} segundos') #? <---- Tempo para embaralhar a lista

# #*=================Cópias para cada método=================*#

lista_bubble = lista.copy()
lista_selection = lista.copy()

#*=================Execução dos métodos=================*#

l_bubble, t_bubble = bubble_sort(lista_bubble)
l_selection, t_selection = selection_sort(lista_selection)

t_sort_inicio = time.perf_counter()
lista.sort()
t_sort_fim = time.perf_counter()
t_sort = t_sort_fim - t_sort_inicio

#*=================Resultados=================*#

print(f'Bubble Sort: {t_bubble:.10f} segundos')
print(f'Selection Sort: {t_selection:.10f} segundos')
print(f'tim sort (nativo .sort): {t_sort:.10f} segundos')

# l, t = bubble_sort(lista)
# l, t = selection_sort(lista)