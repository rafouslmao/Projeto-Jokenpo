import random

scoreP1 = 0
scoreP2 = 0
emp = 0
rod = 0

print("Bem-vindo ao Jokenpô!")
print("\n")
print("Menu")
print("1 - Jogador x Jogador")
print("2 - Jogador x Computador")
print("3 - Computador x Computador")

modo = int(input("Escolha: "))

# Nomes
if modo == 1:
    print("\n")
    nome1 = input("Nome do Jogador 1: ")
    nome2 = input("Nome do Jogador 2: ")
elif modo == 2:
    nome1 = input("Nome do Jogador: ")
    nome2 = "Computador"
elif modo == 3:
    nome1 = "GOAT Fallen"
    nome2 = "BOT Zywoo"

while True:
    if modo == 1:
        print("\n")
        p1 = int(input(f"{nome1}, escolha 1(Pedra👊), 2(Papel🖐️ ), 3(Tesoura✂️ ): "))
        print("\n" * 20)
        p2 = int(input(f"{nome2}, escolha 1(Pedra👊), 2(Papel🖐️ ), 3(Tesoura✂️ ): "))
    elif modo == 2:
        print("\n")
        p1 = int(input(f"{nome1}, escolha 1(Pedra👊), 2(Papel🖐️ ), 3(Tesoura✂️ ): "))
        p2 = random.randint(1, 3)
    elif modo == 3:
        print("\n")
        p1 = random.randint(1, 3)
        p2 = random.randint(1, 3)
    else:
        print("Modo inválido!")
        break

    rod += 1

    if p1 == 1:
        alt1 = "Pedra 👊"
    elif p1 == 2:
        alt1 = "Papel 🖐️"
    else:
        alt1 = "Tesoura ✂️"

    if p2 == 1:
        alt2 = "Pedra 👊"
    elif p2 == 2:
        alt2 = "Papel 🖐️"
    else:
        alt2 = "Tesoura ✂️"

    print(f"{nome1}: {alt1} | {nome2}: {alt2}")

   
    if p1 == p2:
        emp += 1
        print("Empate!")
    elif (p1 == 1 and p2 == 3) or \
         (p1 == 2 and p2 == 1) or \
         (p1 == 3 and p2 == 2):
        scoreP1 += 1
        print(f"{nome1} venceu!")
    else:
        scoreP2 += 1
        print(f"{nome2} venceu!")

    print(f"Placar: {scoreP1} x {scoreP2} | Empates: {emp} | Rodadas: {rod}")

    if scoreP1 > scoreP2:
        print(f"{nome1} está na frente!")
        if scoreP1 - scoreP2 >= 3:
            print(f"{nome1} está amassando o {nome2}!")
    elif scoreP2 > scoreP1:
        print(f"{nome2} está na frente!")
        if scoreP2 - scoreP1 >= 3:
            print(f"{nome2} está amassando o {nome1}!")
    else:
        print("Está empatado!")

    if input("Continuar? (s/n): ").lower() != "s":
        break