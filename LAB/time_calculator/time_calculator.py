h = int(input("Digite a hora inicial: "))
m = int(input("Digite o minuto inicial:"))
hf = int(input("Digite a hora final: "))
mf = int(input("Digite o minuto final: "))

if h == 23: 
    h = h + 1

horas = hf - h 
minutos = mf - m 

if horas == 0:
    horas = 24
else:
    if hf < h: 
        horas = 24 - (h - hf) 
    if mf < m: 
        minutos = 60 - (m - mf) 
    
print(f"O jogo durou {horas} hora(s) e {minutos} minutos(s)")