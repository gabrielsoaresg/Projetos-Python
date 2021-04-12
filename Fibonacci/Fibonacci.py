print("\033[1;35m-=\033[m" * 15)
print("\033[1mSequência de Fibonacci".center(30))
print("\033[1;35m-=\033[m" * 15)
n = (int(input("\033[1mQuantos termos deseja mostrar? \033[m")))
termo = 0
termoAnterior = 1
cont = 0
while cont <= n-1:
    cont += 1
    print(f"\033[1;36m{termo} -->\033[m", end=' ')
    soma = termo + termoAnterior
    termoAnterior = termo
    termo = soma
print("\033[1;31mFIM\033[m")
