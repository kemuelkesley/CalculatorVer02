import math

print("="*30)
print("Criador kemuel kesley.")
print("="*30)
print()
print("Calculadora ver. 2.0")
print("="*30)
print("[1]  Somar")
print("="*30)
print("[2]  Subtrair")
print("="*30)
print("[3]  Multiplicar")
print("="*30)
print("[4]  Dividir")
print("="*30)
print("[5]  Resto da divisão")
print("="*30)
print("[6]  Potência")
print("="*30)
print("[7]  Raiz Quadrada")
print("="*30)
print()

enter = int(input("Escolha uma opção:"))
print()
if(enter == 1):
    print("Somar :")
    n1 = int(input("Informe o Número para SOMAR :"))
    n2 = int(input("Informe o Número para SOMAR :"))
    print("%d + %d = %d"% (n1,n2,n1+n2))
elif(enter == 2):
    n1 = int(input("Informe o Número para SUBTRAIR :"))
    n2 = int(input("Informe o Número para SUBTRAIR :"))
    print("%d - %d = %d"% (n1,n2,n1-n2))
elif(enter == 3):
    n1 = int(input("Informe o Número para MULTIPLICAR :"))
    n2 = int(input("Informe o Número para MULTIPLICAR :"))
    print("%d * %d = %d"% (n1,n2,n1*n2))
elif(enter == 4):
    n1 = int(input("Informe o Número para DIVIDIR :"))
    n2 = int(input("Informe o Número para DIVIDIR :"))
    print("%d / %d = %d"% (n1,n2,n1/n2))    
elif(enter == 5):
    n1 = int(input("Informe o Número para Resto da Divião :"))
    n2 = int(input("Informe o Número para Resto da Divisão :"))
    print("%d // %d = %d"% (n1,n2,n1%n2))
elif(enter == 6):
    n1 = int(input("Informe o Número para Potênciação :"))
    n2 = int(input("Informe o Número para Potênciação :"))
    print("%d ** %d = %d"% (n1,n2,n1**n2))
elif(enter == 7):
    n1 = int(input("Informe o Número para Raiz Quadrada :"))
    calc =  n1
    raiz = math.sqrt(n1)
    print("Resultado: %.1d"%raiz)
else:
    print("opcão invalida, informe os números de 1 a 7.")
