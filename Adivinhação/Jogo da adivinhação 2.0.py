from random import randint
computer = randint(0, 10)
print("\033[1mOlá humano! Sou seu computador.... Vamos jogar?")
print("Acabei de pensar em um número de 0 a 10. Consegue adivinhar?")
certo = False
somaJogadas = 0
while not certo:
    player = int(input("Qual seu palpite?\033[m "))
    somaJogadas += 1
    if player == computer:
        certo = True
    if player > computer:
        print("\033[1;31mMenos... Tente novamente.\033[m")
    else:
        print("\033[1;31mMais... Tente novamente.\033[m")
print(f"\033[1;32mAcertou! Você precisou de apenas {somaJogadas} tentativas, Parabéns!!")
