a = 1
b = 0

try:
   c = a / b
   print(c)

except ZeroDivisionError:
    print("Não se divide por zero!")
finally:
    print("Conta realizada ou não.")