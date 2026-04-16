while True:
    modo = input("Escolha o modo de jogo: \n 1. Player vs Player \n 2. Player vs Computador \n 3. Computador vs Computador \n 4. Digite sair para sair. \n ") 
    scoreP1 = 0
    scoreP2 = 0
    if modo == "4":
        break
    
    while modo == "1":
        p1 = input("Qual o nome do Jogador 1: ")
        p2 = input("Qual o nome do Jogador 2: ")
        modo1 = True
        while modo1 == True:
            escolhaP1 = input(f"{p1} quer jogar Pedra, Papel ou Tesoura? ")
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            escolhaP2 = input(f"{p2} quer jogar Pedra, Papel ou Tesoura? ")
            if escolhaP1 == "Pedra" and escolhaP2 == "Papel":
                scoreP2 += 1
                print(f"{p2} ganhou. \n O placar esta: {scoreP1} x {scoreP2}")
            elif escolhaP1 == "Pedra" and escolhaP2 == "Tesoura":
                scoreP1 += 1
                print(f"{p1} ganhou \n O placar esta: {scoreP1} x {scoreP2}")
            elif escolhaP1 == "Pedra" and escolhaP2 == "Pedra":
                print("O jogo empatou.")
            elif escolhaP1 == "Papel" and escolhaP2 == "Papel":
                print("O jogo empatou.")
            elif escolhaP1 == "Papel" and escolhaP2 == "Tesoura":
                scoreP2 += 1
                print(f"{p2} ganhou. \n O placar esta: {scoreP1} x {scoreP2}")
            elif escolhaP1 == "Papel" and escolhaP2 == "Pedra":
                scoreP1+=1
                print(f"{p1} ganhou. \n O placar esta: {scoreP1} x {scoreP2}")
            elif escolhaP1 == "Tesoura" and escolhaP2 == "Papel":
                scoreP1 += 1
                print(f"{p1} ganhou. \n O placar esta: {scoreP1} x {scoreP2}")
            elif escolhaP1 == "Tesoura" and escolhaP2 == "Pedra":
                scoreP2 +=1
                print(f"{p2} ganhou. \n O placar esta: {scoreP1} x {scoreP2}")
            else:
                print("O jogo empatou.")
            continuar = input("Voces desejam continuar jogando?(s/n)\n ")
    if continuar == "n":
        break
