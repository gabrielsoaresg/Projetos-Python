from random import randint
from time import sleep
print("\033[1;34m*-\033[m" * 15)
print("\033[1mVAMOS JOGAR PAR OU ÍMPAR\033[m".center(38))
print("\033[1;34m*-\033[m" * 15)
contVit = 0
while True:
    player = int(input("Diga um número: "))
    computador = randint(0, 11)
    escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    somaNum = player + computador
    print("Analisando...")
    sleep(2)
    if escolha == "P" and somaNum % 2 == 0:
        contVit += 1
        print("=" * 60)
        print(f"Você jogou {player} e o computador {computador}. Totalizando {somaNum}: DEU PAR")
        print("=" * 60)
        print("VOCÊ GANHOU")
        print("Vamos jogar novamente....")
        print("-=" * 25)
    if escolha == "P" and somaNum % 2 != 0:
        print("=" * 60)
        print(f"Você jogou {player} e o computador {computador}. Totalizando {somaNum}: DEU ÍMPAR")
        print("=" * 60)
        print("VOCÊ PERDEU")
        print("-=" * 25)
        break
    if escolha == "I" and somaNum != 0:
        contVit += 1
        print("=" * 60)
        print(f"Você jogou {player} e o computador {computador}. Totalizando {somaNum}: DEU ÍMPAR")
        print("=" * 60)
        print("VOCÊ GANHOU")
        print("Vamos jogar novamente....")
        print("-=" * 25)
    if escolha == "I" and somaNum % 2 == 0:
        print("=" * 60)
        print(f"Você jogou {player} e o computador {computador}. Totalizando {somaNum}: DEU PAR")
        print("=" * 60)
        print("VOCÊ PERDEU")
        print("-=" * 25)
        break
print(f"GAME OVER! Você venceu {contVit} vezes.")
