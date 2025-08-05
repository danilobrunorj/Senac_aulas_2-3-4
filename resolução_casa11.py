'''
11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
•	o produto do dobro do primeiro com metade do segundo .
•	a soma do triplo do primeiro com o terceiro.
•	o terceiro elevado ao cubo.
'''
primeiro = int(input("digite o primeiro inteiro: "))
segundo = int(input("digite o segundo numero inteiro: "))
terceiro = float(input("digite um numero real: "))

produto = (primeiro*2) * (segundo/2)
soma = (primeiro*3)+segundo
cubo = (terceiro**3) 

print (produto)
print (soma)
print(cubo)