import random

contagem = 0
pontosJogador = 0
pontosComputador = 0
jogador = []


while contagem <= 4:
    print()
    jogador = input("Digite pedra, papel ou tesoura:  ").lower()
    computador = random.choice(["pedra",
                   "tesoura",
                   "papel",]
                 )

    if jogador == "pedra" and computador == "tesoura":
        pontosJogador = pontosJogador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == "pedra" and computador == "papel":
        pontosComputador = pontosComputador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == "tesoura" and computador == "papel":
        pontosJogador = pontosJogador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == "tesoura" and computador == "pedra":
        pontosComputador = pontosComputador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == "papel" and computador == "pedra":
        pontosJogador = pontosJogador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == "papel" and computador == "tesoura":
        pontosComputador = pontosComputador + 1
        contagem = contagem + 1
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")

    elif jogador == computador:
        print()
        print(f"E M P A T E, JOGUE NOVAMENTE")
        print()
        print(f"Jogadas: {contagem}")
        print(f"Computador: {computador}, {pontosComputador} ponto(s)")
        print(f"Jogador: {pontosJogador} ponto(s)")                          
  
print()                  
print ("F I M  D E  J O G O")
print()           