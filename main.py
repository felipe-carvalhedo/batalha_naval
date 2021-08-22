from random import randint
grid_jogador = [0]*100
grid_pc = [0]*100
#CODIGO DO JOGADOR

#Printa o grid do JOGADOR.
#Manual:
# * -> Espaço que ainda não foi jogado
# X -> Espaço que não havia barco
# O -> Espaço que acertou o barco
# B -> Onde há barco
def print_grid(grid_jogador, show_boats=False):
    cont = 0
    for i in range(0, 10):
        for j in range(0, 99):
            if j in [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]:
                print("[", end=" ")

            if j in [4, 10, 16, 22, 28, 34, 40, 46, 52, 58]:
                print(']', end=' ')
    
            if j in [2, 8, 14, 20, 26, 32, 38, 44, 50, 56]:
                if grid_jogador[cont] == "B":
                    if show_boats == True:
                        print("B", end= " ")
                        cont += 1
                    else:
                        print("*", end= " ")
                        cont += 1
                elif grid_jogador[cont] == 2:
                    print("O", end=" ")
                    cont += 1
                elif grid_jogador[cont] == 0:
                    print("*", end=" ")
                    cont += 1
                elif grid_jogador[cont] == 1:
                    print("X", end=" ")
                    cont += 1
        print()
# 1 7 13 19 25 31 37 43 49 55 61 -> [
# 4 10 16 22 28 34 40 46 52 58-> ]
# 2 8 14 20 26 32 38 44 50   -> VAZIO

#Recebe e faz a validação da jogada.
def ask_move(grid, human_player=True):
    while True:
        opcao_escolhida = input("Digite o local que deseja jogar(0-99): ") if human_player else randint(0, 99)

        #1. Input é inteiro?
        try:
            opcao_escolhida = int(opcao_escolhida)
        except ValueError:
            print("Escolha um valor numérico entre 1-100")
            continue

        #2. Input é um valor entre 1 e 100(inclusivo)?
        if opcao_escolhida < 0 or opcao_escolhida > 100: 
            print("Você digitou uma opção inválida, por favor digite um número entre 0 e 99.")
            continue

        #3. Já jogou naquele espaço?
        if grid[opcao_escolhida] == 1 or grid[opcao_escolhida] == 2:
            if human_player:
                print("Você ja jogou aqui, por favor escolha outro local para jogar.")
            continue
        return opcao_escolhida

#Coloca os barquinhos no tabuleiro do jogador.
def set_boats(grid, human_player=True):
    contador = 0
    if human_player:
        print("Escolha onde colocar os seus 3 barcos:")
        print_grid(grid)
    while True:
        sentido = direction(human_player)
        barco = input("Digite a posição da ponta do barco.\n") if human_player else randint(0, 99)
        try:
            barco = int(barco)
        except ValueError:
            print("Escolha um valor numérico entre 0-99")
            continue      
        if type(barco) == int and barco >= 0 and barco < 100:
            if (sentido == 1 and grid[barco] == "B" or grid[barco + 1] == "B" or grid[barco + 2] == "B") or\
            (sentido == 2 and grid[barco] == "B" or grid[barco + 10] == "B" or grid[barco + 20] == "B"):
                if human_player:
                    print("Você já escolheu essa posição, por favor tente outra posição para colocar o barco.")
            else:
                if barco % 10 >= 8 and sentido == 1 or barco // 10 >= 8 and sentido == 2:
                    if human_player:
                        print('Você digitou uma opção inválida para o barco, por favor digite uma opção que não termine com os números 8 ou 9.')
                else:
                    grid[barco] = "B"
                    grid[barco + 1*(sentido == 1) + 10*(sentido == 2)] = "B"
                    grid[barco + 2*(sentido == 1) + 20*(sentido == 2)] = "B"
                    contador += 1
                    if human_player:
                        print_grid(grid, True)              
            if contador == 3:
                    print()
                    break
        else:
            print("Você não digitou uma opção válida, por favor digite uma opção válida entre 0 e 99.")

#Direção do barco do jogador na vertical ou horizontal.
def direction(human_player = True):
    while True:
        boat_direction = input("Escolha a direção do barco. 1 - Horizontal | 2 - Vertical.\n") if human_player else randint(1, 2)
        try:
            boat_direction = int(boat_direction)
        except ValueError:
            print("Escolha um valor numérico entre 0-99")
            continue
        if boat_direction == 1:
            if human_player:
                print("Barco na horizontal escolhido!")
            return boat_direction
        elif boat_direction == 2:
            if human_player:
                print("Barco na vertical escolhido!")
            return boat_direction
        else:
            print("Você digitou uma opção inválida, tente novamente com 1 - Horizontal ou 2 - Vertical!")

#Se a jogada foi no barco ou na água.
def boat_or_water(grid, valid_move):   
        if grid[valid_move] == 0:
            movimento = 1
            return movimento
        elif grid[valid_move] == "B":
            movimento = 2
            return movimento

#Se o jogo acabou.
def its_over(grid, current_player):
    counter = 0
    for i in grid:
        if i == 2:
            counter += 1
    if counter == 9:
        print(f"FIM DE JOGO, o jogador {current_player} VENCEU!!!")
        return True

#O nome do jogador
def ask_name():
    name = input("Digite o seu nome: ")
    return name
#######################################################################################################################################################

#CODIGO DO PC

#PROGRAMA PRINCIPAL
PC = "PC"
nome = ask_name()
set_boats(grid_pc, human_player= False)
print_grid(grid_pc, True)
print("GRID JOGADOR")
set_boats(grid_jogador)
print_grid(grid_jogador, True)

while True:
    print("===========NOVO TURNO=============")
    #Jogador 
    print("Printando o grid do PC")
    print_grid(grid_pc)
    print()
    print("Printando o grid do jogador")
    print_grid(grid_jogador, True)
    print()
    valid_move = ask_move(grid_pc)
    play_result = boat_or_water(grid_pc, valid_move)
    grid_pc[valid_move] = play_result
    print_grid(grid_pc)
    finish = its_over(grid_pc, nome)
    if finish == True:
        break
    
    #PC
    valid_move = ask_move(grid_jogador, human_player=False)
    play_result = boat_or_water(grid_jogador, valid_move)
    grid_jogador[valid_move] = play_result
    print(valid_move)
    print("Printando o grid do JOGADOR")
    print_grid(grid_jogador, True)
    print()
    finish = its_over(grid_jogador, PC)
    if finish == True:
        break
