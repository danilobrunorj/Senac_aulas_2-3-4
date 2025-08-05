#imc
# imc = peso / altura ** 2
# imc =  peso / (altura * altura)
# se colocar parentese ele dá preferência de cálculo)



nome = 'Lucas'

altura = 1.71
peso = 80

#processamento
imc = peso / altura**2

print (nome, "tem", altura, "de altura,", "pesa", peso, "kg", ", e seu imc é =",imc)

#f-strings
print(f'{nome} tem {altura} pesa {peso} e seu imc é {imc:.2f}')