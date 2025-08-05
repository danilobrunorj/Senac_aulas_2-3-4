'''
17.	Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 
 Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços 
 em 3 situações:
•	comprar apenas latas de 18 litros;
•	comprar apenas galões de 3,6 litros;
•	misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''
area_pintada =float(input("Qual tamanho em m² da área a ser pintada: "))
litros_necessários = (area_pintada/6)
embalagens = input("Qtd de tinta, digite G para galão de 3,6l ou L para lata de 18l: ").lower()

galao = int(-(-litros_necessários / 3.6 // 1))
latas = int(-(-litros_necessários / 18 // 1))

preco_galao = galao * 80
preço_latas = latas * 25

if embalagens == "g":
    print (f"A qtd de tinta necessária é de {litros_necessários} L, e precisará de {galao} galões de tinta e custará R$: {preco_galao:.2f}. ")

elif embalagens == "l":
    print(f"A qtd de tinta necessária é de {litros_necessários} L, e precisará de {latas} latas de tinta e custará R$: {preço_latas:.2f}.")
else:
    print("Você não digitou uma letra válida")