
a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Não é um triângulo")

elif a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else: 
    print("Escaleno")
  