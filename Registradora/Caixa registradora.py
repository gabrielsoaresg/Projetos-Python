print("\033[1m=-=" * 15)
print("\033[1;32mLojas Tabajara\033[m". center(51))
print("=-=\033[m" * 15)
cont = 1
somaP = 0
while True:
    p = float(input(f"Produto {cont}: R$ "))
    cont += 1
    somaP += p
    if p == 0:
        break
print(f"\033[1;32mTotal: R${somaP:.2f}\033[m")
pagamento = float(input("\033[1mDinheiro: R$ \033[m"))
while pagamento < somaP:
    pagamento = float(input("\033[1mDinheiro: R$ \033[m"))
troco = pagamento - somaP
if pagamento != somaP:
    print(f"\033[1;34mTroco: R$ {troco:.2f}\033[m")
elif troco == 0:
    print("\033[1;31mNão há volta!")
