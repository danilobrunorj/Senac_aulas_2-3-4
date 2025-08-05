'''
16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total.

'''
area_pintada =float(input("Qual tamanho em m² da área a ser pintada: "))
litros_necessários = (area_pintada/3)
latas = int(-(-litros_necessários / 18 // 1))
preco_galao = latas * 80
print(f'Quantidade de lata(s):{latas}, e o valor total gasto R$: {preco_galao:.2f} ')