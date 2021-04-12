print("=-=" * 10)
print("BANCO GSG".center(30))
print("=-=" * 10)
somaCed = 0
ced = 50
saque = (int(input("Qual valor deseja sacar? ")))
while True:
    if saque >= ced:
        saque -= ced
        somaCed += 1
    else:
        if somaCed > 0:
            print(f"Total de {somaCed} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        somaCed = 0
        if saque == 0:
            break
print("=-=" * 10)
print("OBRIGADO POR UTILIZAR O BACNO GSG! VOLTE SEMPRE")
