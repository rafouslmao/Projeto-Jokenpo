import random


print("Menu")
print("1. Jogador x Jogador")
print("2. Jogador x Computador")
print("3. Computador x Computador")

scoreP1 = 0
scoreP2 = 0
emp = 0
rod = 0
alt1 = ""
alt2 = ""
modo = int(input("Escolha um modo de jogo: "))
while modo > 3:
    print("Modo inválido")
    modo = int(input("Escolha um modo de jogo: "))
while True:    
    if modo == 1:
        p1 = input("Qual o nome do Jogador 1: ")
        p2 = input("Qual o nome do Jogador 2: ")
        while True:
            escolhaP1 = int(input(f"Para a rodada {rod+1}, {p1} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            escolhaP2 = int(input(f"Para a rodada {rod+1}, {p2} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
            if escolhaP1 == 1:
                alt1 = "Pedra"
            elif escolhaP1 == 2:
                alt1 = "Papel"
            elif escolhaP1 == 3:
                alt1 = "Tesoura"
            if escolhaP2 == 1:
                alt2 = "Pedra"
            elif escolhaP2 == 2:
                alt2 = "Papel"
            elif escolhaP2 == 3:
                alt2 = "Tesoura"
            while escolhaP1 > 3 or escolhaP2 > 3:
                print("Alternativa inválida.")
                escolhaP1 = int(input(f"Para a rodada {rod+1}, {p1} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                escolhaP2 = int(input(f"Para a rodada {rod+1}, {p2} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
                if escolhaP1 == 1:
                    alt1 = "Pedra"
                elif escolhaP1 == 2:
                    alt1 = "Papel"
                elif escolhaP1 == 3:
                    alt1 = "Tesoura"
                if escolhaP2 == 1:
                    alt2 = "Pedra"
                elif escolhaP2 == 2:
                    alt2 = "Papel"
                elif escolhaP2 == 3:
                    alt2 = "Tesoura"
            if escolhaP1 == 1 and escolhaP2 == 2:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 3:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod} \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 1:
                rod += 1
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 2:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 3:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 1:
                scoreP1+=1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 2:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 1:
                scoreP2 +=1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 3:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            continuar = input("Voces desejam continuar jogando?(s/n)\n")
            if continuar != "s":
                break
        break
    elif modo == 2:
        p1 = input("Qual o nome do jogador? ")
        p2 = "GOAT FalleN"
        while True:
            escolhaP1 = int(input(f"Para a rodada {rod+1}, {p1} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
            escolhaP2 = random.randint(1,3)
            if escolhaP1 == 1:
                alt1 = "Pedra"
            elif escolhaP1 == 2:
                alt1 = "Papel"
            elif escolhaP1 == 3:
                alt1 = "Tesoura"
            if escolhaP2 == 1:
                alt2 = "Pedra"
            elif escolhaP2 == 2:
                alt2 = "Papel"
            elif escolhaP2 == 3:
                alt2 = "Tesoura"
            print(f"\n\n{p2} escolheu {alt2}\n\n")
            while escolhaP1 > 3:
                print("Alternativa inválida.")
                escolhaP1 = int(input(f"Para a rodada {rod+1}, {p1} deseja jogar 1 (Pedra), 2 (Papel) ou 3 (Tesoura)? "))
                if escolhaP1 == 1:
                    alt1 = "Pedra"
                elif escolhaP1 == 2:
                    alt1 = "Papel"
                elif escolhaP1 == 3:
                    alt1 = "Tesoura"
                if escolhaP2 == 1:
                    alt2 = "Pedra"
                elif escolhaP2 == 2:
                    alt2 = "Papel"
                elif escolhaP2 == 3:
                    alt2 = "Tesoura"
                print(f"{p2} escolheu {alt2}")

            if escolhaP1 == 1 and escolhaP2 == 2:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 3:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod} \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 1:
                rod += 1
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 2:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 3:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 1:
                scoreP1+=1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 2:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 1:
                scoreP2 +=1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 3:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            continuar = input("Voce deseja continuar jogando?(s/n)\n")
            if continuar != "s":
                break
        break
    elif modo == 3:
        p1 = "GOAT FalleN"
        p2 = "BOT ZywOo"
        while True:
            escolhaP1 = random.randint(1,3)
            escolhaP2 = random.randint(1,3)
            if escolhaP1 == 1:
                alt1 = "Pedra"
            elif escolhaP1 == 2:
                alt1 = "Papel"
            elif escolhaP1 == 3:
                alt1 = "Tesoura"
            if escolhaP2 == 1:
                alt2 = "Pedra"
            elif escolhaP2 == 2:
                alt2 = "Papel"
            elif escolhaP2 == 3:
                alt2 = "Tesoura"
            print(f"\n{p1} escolheu {alt1}\n")
            print(f"\n{p2} escolheu {alt2}\n")
            if escolhaP1 == 1 and escolhaP2 == 2:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 3:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod} \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 1 and escolhaP2 == 1:
                rod += 1
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 2:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 3:
                scoreP2 += 1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 2 and escolhaP2 == 1:
                scoreP1+=1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 2:
                scoreP1 += 1
                rod += 1
                print(f"{p1} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 1:
                scoreP2 +=1
                rod += 1
                print(f"{p2} ganhou a rodada {rod}. \nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            elif escolhaP1 == 3 and escolhaP2 == 3:
                rod += 1 
                emp += 1
                print(f"A rodada {rod} empatou.\nO confronto foi: {alt1} x {alt2}.")
                if scoreP1 > scoreP2:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p1} está na frente!")
                elif scoreP2 > scoreP1:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\n{p2} está na frente!")
                else:
                    print(f"O placar esta: {scoreP1} x {scoreP2}\nEmpates: {emp}.\nO jogo está empatado!")
            continuar = input("Voce deseja continuar assistindo?(s/n)\n")
            if continuar != "s":
                break
        break
