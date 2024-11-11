from collections import deque
from time import time

# Funções para medir o tempo de adição e remoção de elementos na frente e atrás da estrutura

# Teste com lista
def list_performance(num_elements):
    list_structure = []
    # Adicionar elementos ao final
    start_time = time()
    for element in range(num_elements):
        list_structure.append(element)
    append_time = time() - start_time

    # Remover elementos do início
    start_time = time()
    for _ in range(num_elements):
        list_structure.pop(0)
    pop_front_time = time() - start_time

    return append_time, pop_front_time

# Teste com deque
def deque_performance(num_elements):
    deque_structure = deque()
    # Adicionar elementos ao final
    start_time = time()
    for element in range(num_elements):
        deque_structure.append(element)
    append_time = time() - start_time

    # Remover elementos do início
    start_time = time()
    for _ in range(num_elements):
        deque_structure.popleft()
    pop_front_time = time() - start_time

    return append_time, pop_front_time

# Configuração do teste com uma quantidade significativa de elementos
num_elements = 300000

# Executar e comparar o tempo para lista e deque
list_append_time, list_pop_front_time = list_performance(num_elements)
deque_append_time, deque_pop_front_time = deque_performance(num_elements)

# Imprimir resultados
print(f"Lista - Tempo para adicionar ao final: {list_append_time:.4f} segundos")
print(f"Lista - Tempo para remover do início: {list_pop_front_time:.4f} segundos")
print(f"Deque - Tempo para adicionar ao final: {deque_append_time:.4f} segundos")
print(f"Deque - Tempo para remover do início: {deque_pop_front_time:.4f} segundos")
