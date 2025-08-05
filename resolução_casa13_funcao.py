'''
13.	Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
•	Para homens: (72.7*h) - 58
•	Para mulheres:  
'''

def calcular_peso_ideal(sexo, h):
    if sexo.lower() == "h" :
        print((72.7*h) - 58)
    elif sexo.lower() == "m": 
        print((62.1*h) - 44.7)
    else :
        print ("você não digitou uma letra valida")
calcular_peso_ideal("m",1.85)
