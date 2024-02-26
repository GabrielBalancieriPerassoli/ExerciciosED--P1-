class Vetor:
    def __init__(self, tamanho):
        self.elementos = [None] * tamanho
        self.tamanho_max = tamanho
        self.n = -1
    def cheio(self):
            return self.tamanho() == self.tamanho_max

    def pegar(self, i):
        if self.n < i or i < 0:
            raise Exception('Indice fora do vetor!') 
        
        return self.elementos[i]

    def inserir(self, i, v):
        if self.cheio():
            raise Exception('Vetor cheio!')
        
        for j in range(self.n + 1, i, -1):
            self.elementos[j] = self.elementos[j - 1]

        self.elementos[i] = v
        self.n += 1

    def acrescentar(self, v):
        if self.cheio():
            raise Exception('Vetor cheio!')
        self.elementos[self.n + 1] = v
        self.n += 1

    def tamanho(self):
        return self.n + 1

    def remover(self, i):
        if self.n < i or i < 0:
            raise Exception('Indice fora do vetor!') 

        x = self.elementos[i]

        for j in range(i, self.n):
            self.elementos[j] = self.elementos[j + 1]
        
        self.n -= 1
        return x

    def concatenar(self, vetor):
        if (self.tamanho() + vetor.tamanho()) > self.tamanho_max:
            raise Exception('A lista não tem espaço suficiente!')

        for i in range(0, vetor.tamanho()):
            self.acrescentar(vetor.elementos[i])

    def cortar(self, i):
        novo_vetor = Vetor(self.tamanho_max)

        for i in range(self.n, i - 1, -1):
            novo_vetor.acrescentar(self.pegar(i))
            self.n -= 1

        return novo_vetor

    def copiar(self):
        novo_vetor = Vetor(self.tamanho_max)

        for i in range(self.tamanho()):
            novo_vetor.acrescentar(self.pegar(i))

        return novo_vetor

    def buscar(self, v):
        for i in range(self.tamanho()):
            if self.pegar(i) == v:
                return i

        return -1    

    def __str__(self):
        return str(self.elementos[:self.n + 1])

class Pilha:
    def __init__(self, tamanho_max):
        self.vetor = [None] * tamanho_max
        self.tamanho_max = tamanho_max
        self.topo_i = -1

    def cheio(self):
        return self.tamanho_max == self.topo_i + 1

    def empilhar(self, v):
        if self.cheio():
            raise Exception('Pilha cheia!')

        self.topo_i += 1
        self.vetor[self.topo_i] = v
    
    def desempilhar(self):
        if self.vazia():
            raise Exception('Pilha vazia!')

        self.topo_i -= 1

        return self.vetor[self.topo_i + 1]

    def topo(self):
        if self.vazia():
            return

        return self.vetor[self.topo_i]
    
    def tamanho(self):
        return self.topo_i + 1

    def vazia(self):
        return self.topo_i == -1

    def __str__(self):
        return str(self.vetor[:self.topo_i + 1])

class Fila:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.vetor = [None] * tamanho_max
        self.esq = -1
        self.dir = -1

    def enfilheirar(self, v):
        if self.cheia():
            raise Exception('Fila cheia!')
        if self.dir == (self.tamanho_max - 1):
            self.deslocar()
        if self.vazia():
            self.esq = 0

        self.dir += 1
        self.vetor[self.dir] = v

    def desenfilheirar(self):
        if self.vazia():
            raise Exception('Fila vazia!')

        self.esq += 1

        return self.vetor[self.esq - 1]

    def deslocar(self):
        desloc = self.esq
        
        for i in range(self.tamanho()):
            self.vetor[i] = self.vetor[i + desloc]

        self.esq = 0
        self.dir = self.dir - desloc 

    def tamanho(self):
        return self.dir - self.esq + 1

    def cheia(self):
        return self.tamanho() == self.tamanho_max

    def vazia(self):
        return self.esq == -1 or self.esq > self.dir 

    def primeiro(self):
        if self.vazia():
            return 

        return self.vetor[self.esq]

    def __str__(self):
        return str(self.vetor[self.esq:(self.dir + 1)])

def parentizacao(expressao):
    pilha = Pilha(len(expressao))

    for i in range(len(expressao)):
        char = expressao[i]

        if char == '(':
            pilha.empilhar(1)
        if char == ')':
            if pilha.vazia():
                return False
            pilha.desempilhar()

    return pilha.vazia()

def parentizacao_avancada(expressao):
    pilha = Pilha(len(expressao))

    for i in range(len(expressao)):
        char = expressao[i]

        if char in ('(', '[', '{'):
            pilha.empilhar(char)
            continue
        if char == ')' and pilha.topo() != '(':
            return False
        if char == ']' and pilha.topo() != '[':
            return False
        if char == '}' and pilha.topo() != '{':
            return False
        if char in (')', ']', '}'):
            if pilha.vazia():
                return False

            pilha.desempilhar()
    return pilha.vazia()

def resolver_expressao(expressao):
    operandos = Pilha(len(expressao))
    operadores = Pilha(len(expressao))

    i = len(expressao) - 1
    while i >= 0:
        char = expressao[i]

        if char in ('+', '-', '*', '/'):
            operadores.empilhar(char)

        elif char != ' ':
            j = i - 1
            operando = char
            while expressao[j] != ' ' and j >= 0:
                operando = expressao[j] + operando
                j -= 1
            operandos.empilhar(int(operando))
            i = j
        i -= 1
    
    while not operadores.vazia():
        a = operandos.desempilhar()
        b = operandos.desempilhar()

        op = operadores.desempilhar()

        if op == '+':
            operandos.empilhar(a + b)
        elif op == '-':
            operandos.empilhar(a - b)
        elif op == '*':
            operandos.empilhar(a * b)
        elif op == '/':
            operandos.empilhar(a / b)
        print(operandos, operadores)

def remover_base(pilha):
    pilha2 = Pilha(pilha.tamanho())

    while not pilha.vazia():
        pilha2.empilhar(pilha.desempilhar())

    pilha2.desempilhar()

    while not pilha2.vazia():
        pilha.empilhar(pilha2.desempilhar())

def inverter_pilha(pilha):
    fila = Fila(pilha.tamanho_max)
    
    while not pilha.vazia():
        fila.enfilheirar(pilha.desempilhar())

    while not fila.vazia():
        pilha.empilhar(fila.desenfilheirar())

pilha = Pilha(10)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print(pilha)
inverter_pilha(pilha)
print(pilha)
