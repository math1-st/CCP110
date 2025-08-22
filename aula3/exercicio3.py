print("Cálculo da soma de dias, horas, minutos e segundos em apenas segundos.")

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite o tempo em horas: "))
minutos = int(input("Digite o tempo em minutos: "))
segundos = int(input("Digite o tempo em segundos: "))

calculo = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos

print(f"Resultado: {calculo} segundos")