'''
15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. 
Calcule e mostre o total do seu salário
no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
•	salário bruto.
•	quanto pagou ao INSS.
•	quanto pagou ao sindicato.
•	o salário líquido.
•	calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : 
R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

'''

salario_hora = float(input("digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(input("digite quantos horas você trabalhou no mês: "))
salario_bruto = (salario_hora*horas_trabalhadas_mes)
Ir =(salario_bruto*0.11)
Inss =(salario_bruto*0.08)
sindicato =(salario_bruto*0.05)
salario_liquido = (salario_bruto-Ir-Inss-sindicato)

print(f'Salário Bruto R$:{salario_bruto:.2f} IR(11%):{Ir:.2f}  INSS (8%): {Inss:.2f} sindicato (5%): {sindicato:.2f}, salário liquido:{salario_liquido:.2f}:')
