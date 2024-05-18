# nome = "Ana"
# numero_inteiro = 10
# numero_real = 5.6
# dado_boleano = True

# #print() -> mostrar ou imprimir dados no console

# print(nome)
# print (numero_real)
# print (dado_boleano)

# print (type(nome))
# print (type(numero_inteiro))
# print (type(numero_real))
# print (type(dado_boleano))

# #concatenação == juntar textos, vaiáveis, resultados

# texto = type (nome)
# inteiro = type (numero_inteiro)
# real = type(numero_real)  
# boleano = type(dado_boleano)  

# print ('essa variavél ->', nome, "é da", texto)
# print ('essa variavél ->', numero_inteiro, "é da", inteiro)
# print ('essa variavél ->', numero_real, "é da", real)
# print ('essa variavél ->', dado_boleano, "é da", boleano)

# print (f'essa variavél ->, {nome}, é da, {texto}')
# print (f'essa variavél ->, {numero_inteiro}, é da, {inteiro}')
# print (f'essa variavél ->, {numero_real}, é da, {real}')
# print (f'essa variavél ->, {dado_boleano}, é da, {boleano}')



# #--------------------------------------------------------------------


# print(10//12)

# nome = input('Digite seu nome:')
# print(nome)

# numero1= int(input(">>"))
# numero2= int(input(">>"))

# cacular = numero1 / numero2
# print(cacular)


#atividade Calculadora

# print(10*2)
# print(30/3)



# Texto = "Calculadora Divisão"
# print (Texto)

# NumeroA = int(input("escreva:"))
# NumeroB = int(input("escreva:"))
# Calcula = NumeroA / NumeroB
# print(Calcula)

# texto = "Calculadora multiplicação"
# print (texto)

# numeroA = int(input("escreva:"))
# numeroB = int(input("escreva:"))
# calcula = numeroA * numeroB
# print(calcula)

# print(1+(2*3)-(30/3))

# list[10,15,3,1,5]

# indice = list[0]
# indice2 = list[1]

# print(indice + indice2)

# numeros = list(range(1,11))
# print(numeros)

# numeros = list(range(1,11))
# print(len(numeros))

# variavel = "incostitucionavel"
# lista2 = list(variavel)
# print(lista2)

# Lista3 = [252335,3365,248,12,23,6,117,3369,25,1,2,-1]
# organizar = sorted(Lista3)
# print(organizar)

# Lista4 = [252335,3365,248,12,23,6,117,3369,25,1,2,-1]
# organizar = reversed(Lista4)
# print(organizar)

Lista3 = [252335,3365,248,12,23,6,117,3369,25,1,2,-1]
#remover 
Lista3.pop(2)
print(Lista3)

tupla = (252,362,123,42,23,11,96)
sorted(tupla)
a,b,c,d,e,f,g = tupla
print(a,b,c,d,e,f,g)