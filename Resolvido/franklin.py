
class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

    def __str__(self):
        node = self
        lista_str = '['
        while node != None:
            lista_str += str(node.info)
            if node.prox:
                lista_str += ', '
            node = node.prox
        lista_str += ']'

        return lista_str

def insere_final(linked_list, valor):
    if linked_list == None:
        linked_list = Node(valor)
        return linked_list

    node = linked_list 
    while node.prox != None:
        node = node.prox
    node.prox = Node(valor)

    return linked_list

def insere_inicio(linked_list, valor):
    if linked_list == None:
        linked_list = Node(valor)
        return linked_list

    node = Node(valor)
    node.prox = linked_list 
    linked_list = node

    return linked_list 

def remove_inicio(linked_list):
    if linked_list == None:
        return

    if linked_list.prox == None:
        linked_list = None

        return linked_list

    q = linked_list 
    linked_list = linked_list.prox
    #dispose(q)

    return linked_list

def insere_inicio(linked_list, valor):
    if linked_list == None:
        linked_list = Node(valor)
        return linked_list

    node = Node(valor)
    node.prox = linked_list 
    linked_list = node

    return linked_list  

def insere_ordenado(linked_list, valor):
    if linked_list == None:
        return insere_inicio(linked_list, valor)
    elif linked_list.info > valor:
        return insere_inicio(linked_list, valor)
    else:
        atual = linked_list 

        while atual.prox != None and atual.prox.info < valor:
            atual = atual.prox
        
        node = Node(valor)
        node.prox = atual.prox
        atual.prox = node
        
        return linked_list 
    
def soma_recursiva(lista, l=0, r=None):
    if r == None:
        r = len(lista) - 1

    if l >= len(lista):
        return 0

    return lista[l] + soma_recursiva(lista, l + 1, r)

def inicializa_lista(vetor):
    lista = None

    for i in reversed(vetor):
        lista = insere_inicio(lista, i)
    
    return lista

lista = inicializa_lista([1,2,3,4,5,6,7,8])

def soma_ligada_recursiva(lista):
    if lista == None:
        return 0

    return lista.info + soma_ligada_recursiva(lista.prox)       

def fibo_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibo_rec(n):
    if n <= 1:
        return n
    
    return fibo_rec(n - 1) + fibo_rec(n - 2)

def busca_vetor(lista, n, i=0):
    if i > len(lista) - 1:
        return False

    if lista[i] == n:
        return True

    return busca_vetor(lista, n, i + 1)

def potencia_recursiva(x, n):
    if n == 0:
        return 1

    return x * potencia_recursiva(x, n - 1)

def maior_recursiva(lista, i=0):
    if i > len(lista) - 1:
        return None

    n1 = lista[i]
    n2 = maior_recursiva(lista, i + 1)

    if n2 == None:
        return n1

    if n1 > n2:
        return n1
    return n2

def print_lista_ligada_inversa(lista):
    if lista.prox != None:
        print_lista_ligada_inversa(lista.prox)
    print(lista.info)

def print_lista_ligada_inversa_iter(lista):
    anterior = None
    atual = lista
    
    while atual.prox != None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo

    while atual.prox != None:
        print(atual)
        atual = atual.prox

def inverter_lista(lista):
    anterior = None
    atual = lista
    
    while atual != None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo

    return anterior

def inverter_lista_esvaziar(lista):
    nova_lista = Node(lista.info)
    lista = lista.prox

    while lista != None:
        nova_lista = insere_inicio(nova_lista, lista.info)
        lista = lista.prox

    return nova_lista

def ordena_lista(linked_list):
    nova_lista = None

    atual = linked_list
    
    while atual != None:
        nova_lista = insere_ordenado(nova_lista, atual.info)
        atual = atual.prox

    return nova_lista

def lista_ordenada(linked_list):
    atual = linked_list

    while atual != None:
        if atual.prox == None:
            return True
        if atual.info > atual.prox.info:
            return False

        atual = atual.prox

def remover_negativos(linked_list):
    if linked_list == None:
        return linked_list

    atual = linked_list

    if atual.info < 0:
        q = atual
        linked_list = atual.prox
        #dispose(q)

    while atual.prox != None:
        if atual.prox.info < 0:
            q = atual.prox
            atual.prox = atual.prox.prox
            #dispose(q)
        else: 
            atual = atual.prox
        

    return linked_list

lista_com_negativos = inicializa_lista([-5, 10, 1, -3, 2, -6, 3, -0 , -9])

def par_primeiro(linked_list):
    atual = linked_list

    if linked_list == None:
        return linked_list

    while atual.prox != None:
        if atual.prox.info % 2 == 0:
            q = atual.prox
            atual.prox = atual.prox.prox
            linked_list = insere_inicio(linked_list, q.info)
        else:
            atual = atual.prox

    return linked_list

def lista_tem_repetidos(linked_list):
    if linked_list == None or linked_list.prox == None:
        return False

    p1 = linked_list

    while p1 != None:
        p2 = p1.prox
        while p2 != None:
            print(p1.info, p2.info)
            if p1.info == p2.info:
                return True
            p2 = p2.prox
        p1 = p1.prox

    return False

def concatenar_lista(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    node = l1

    while node.prox != None:
        node = node.prox

    node.prox = l2
    
    return l1

def mesclar_listas_ordenadas(l1, l2):
    l3 = None

    def insere_inicio(l3, node):
        q = node
        node = node.prox
        q.prox = l3
        l3 = q

        return l3, node

    while l1 != None and l2 != None:
        print(l1, l2, l3)
        if l1 == None:
            l3, l2 = insere_inicio(l3, l2)
            continue
        if l2 == None:
            l3, l1 = insere_inicio(l3, l1)
            continue
        if l1.info > l2.info:
            l3, l2 = insere_inicio(l3, l2)
            continue
        l3, l2 = insere_inicio(l3, l2)


    return l3

print(mesclar_listas_ordenadas(inicializa_lista([-10, -5, 0, 5]), inicializa_lista([-15, -1, 5, 15])))
