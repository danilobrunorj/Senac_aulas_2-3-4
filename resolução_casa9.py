'''
9.	Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
'''
grau_Farenheit = float(input("digite o grau em Farenheit: "))
graus_celcius = (5 * (grau_Farenheit-32) / 9)
print ("Graus Celcius é: ", graus_celcius)