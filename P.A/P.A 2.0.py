print("\033[1;35m=-=\033[m" * 10)
print("\033[1mGerador de P.A".center(32))
print("\033[1;35m=-=\033[m" * 10)
n = int(input("Primeiro Termo: "))
r = int(input("Razão da P.A: "))
i = 1
total = 0
novoT = 10
somaT = 0
while novoT != 0:
    total += novoT
    somaT += novoT
    while i <= total:
        print(f"{n} -->", end=' ')
        n += r
        i += 1
    print("PAUSA", end=' ')
    novoT = int(input("\nQuantos termos a mais deseja mostrar? "))
print(f"Fim! foram mostrados {somaT} termos!")