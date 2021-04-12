class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 7
        self.volume = 10

    def power(self):
        if not self.ligada:
            self.ligada = True
        else:
            self.ligada = False

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1

    def aumenta_volume(self):
        self.volume += 1

    def diminui_volume(self):
        self.volume -= 1


televisao = Tv()
p = str(input("Deseja ligar a TV? [S/N] ")).upper().strip()
if p == "S":
    televisao.power()
    print("Televisão ligada")
    print(f"Canal: {televisao.canal}")
    print(f"Volume: {televisao.volume}")
    while True:
        c = str(input("Deseja mudar de canal? [+/-] "))
        v = str(input("Deseja aumentar ou diminuir o volume? [+/-] "))
        while c not in "+-":
            c = str(input("Deseja mudar de canal? [+/-] "))
        if c == "+":
            televisao.aumenta_canal()
            print(f"Canal: {televisao.canal}")
        elif c == "-":
            televisao.diminui_canal()
            print(f"Canal: {televisao.canal}")
        while v not in "+-":
            v = str(input("Deseja aumentar ou diminuir o volume? [+/-] "))
        if v == "+":
            televisao.aumenta_volume()
            print(f"Volume: {televisao.volume}")
        elif v == "-":
            televisao.diminui_volume()
            print(f"Volume: {televisao.volume}")
        esc = str(input("Deseja continuar? [S/N] ")).upper().strip()
        while esc not in "SN":
            esc = str(input("Deseja continuar? [S/N] ")).upper().strip()
        if esc == "N":
            break
else:
    quit()
