"""
14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve 
pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um 
programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa c
om as mensagens adequadas.

"""
peso = float(input("digite o peso do peixe: "))

if peso <= 50:
    print(f' O peixe pesa {peso}kg, e a multa é: R$ 0' )
else:
    calculo_multa = (peso- 50)*4
    print(f' o peixe pesa {peso}kg, a multa a ser paga é: , R$:{calculo_multa:.2f}')