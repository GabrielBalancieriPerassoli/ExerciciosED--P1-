from Pilha import Pilha

# Considere uma partida do jogo Torre de Hanoi com cinco discos no pino inicial.
# Apresente a sequência de operações Empilha / Desempilha executada para passar os cinco discos para uma outra pilha

tamanho = 4

P1 = Pilha(tamanho)
P2 = Pilha(tamanho)
P3 = Pilha(tamanho)

print("\n")

pilhas = {}

for i in range(1, 3 + 1):
    pilhas[f'p{i}'] = Pilha(tamanho)

pilhas = {'P1':P1, 'P2':P2, 'P3':P3}

P1.Empilha(5)
P1.Empilha(4)
P1.Empilha(3)
P1.Empilha(2)
P1.Empilha(1)

pergunta = None

primeira_jogada = True
                 
while pergunta != 3:

    print("====================================")
    print("           TORRE DE HANOI           ")
    print("====================================\n")
    print("               AÇÕES                \n")
    
    if primeira_jogada:
        print("1 - REMOVER ELEMENTO EM UMA PILHA PARA COLOCAR EM OUTRO")
        print("2 - VER AS PILHAS")
        print("3 - SAIR\n")
    else:
        print("1 - REMOVER ELEMENTO EM UMA PILHA PARA COLOCAR EM OUTRO")
        print("2 - VER AS PILHAS")
        print("3 - SAIR\n")
    
    pergunta = int(input("Qual dessas opções você escolhe? "))

    if primeira_jogada and pergunta == 2:
        print("Você não pode ver as pilhas na primeira jogada. Escolha outra opção.")

    elif pergunta == 1:
        
        pilha_remover = input(f"De qual pilha você quer remover um elemento? P1 a P3: ")

        if not pilhas[pilha_remover].PilhaVazia():

            pilha_inserir = input(f"Em qual pilha você quer inserir o elemento removido? P1 a P3: ")

            if not pilhas[pilha_inserir].PilhaCheia():

                if pilhas[pilha_inserir].PilhaVazia():
   
                    x = pilhas[pilha_remover].ElementoDoTopo()
                    pilhas[pilha_remover].Desempilha()
                    print(x)

                    pilhas[pilha_inserir].Empilha(x)
                    
                    print(f"Elemento {x} inserido na pilha {pilha_inserir}.")

                else:

                    if pilhas[pilha_remover].ElementoDoTopo() > pilhas[pilha_inserir].ElementoDoTopo():
    
                        print("Você não pode inserir um elemento neste pino pois e maior que o de baixo")

                    else:    
                        
                        x = pilhas[pilha_remover].ElementoDoTopo()
                        pilhas[pilha_remover].Desempilha()
                        print(x)

                        pilhas[pilha_inserir].Empilha(x)
                        
                        print(f"Elemento {x} inserido na pilha {pilha_inserir}.")     

            else:
    
                print(f"A pilha {pilha_inserir} está cheia. Não é possível inserir mais elementos.")         
        else:

            print("Não é possível remover de uma pilha vazia.")    

        primeira_jogada = False  

    elif pergunta == 2:
        print("\n")
        print("Pilhas:")
        for chave, valor in pilhas.items():
            print("\n")
            print(f"Pilha {chave}:")
            print("\n")
            for i in range(tamanho, -1, -1):
                if i <= valor.topo:
                    elem = valor.elem[i] if valor.elem[i] is not None else " " 
                    print(f"|   {elem:^3}   |")
                else:
                    print(f"|{' ':^9}|")
            print("+---------+")

        # Verifica se alguma pilha contém todos os discos empilhados em ordem
        # for chave, valor in pilhas.items():
        #     if valor.elem == [5, 4, 3, 2, 1]:
        #         print("\n")
        #         print("Você ganhou o jogo!")
        #         pergunta = 3  # Encerra o jogo
        #         break  # Para de verificar as outras pilhas
    else:

        pergunta = 3        

    print("\n") 