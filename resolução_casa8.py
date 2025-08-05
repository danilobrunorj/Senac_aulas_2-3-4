'''
8.	Faça um Programa que pergunte quanto você ganha por hora e 
o número de horas trabalhadas no mês. Calcule e mostre o total do seu 
salário no referido mês.
'''
ganho_por_hora = float ( input( "digite quanto você ganha por hora: "))
horas_trabalhadas_por_mes = float ( input( "digite quantas horas você trabalha por mês: "))
salario = (ganho_por_hora * horas_trabalhadas_por_mes)
print ("seu salário é:" ,salario)