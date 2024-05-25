#se for somar numeros, é mecessario que o tipo em input seja da mesma categoria, ou seja, ambos tem que sser "int" ou "float" se não irá dar erro

#Exercicio 1 - revendo dados
#numero1 = int(input('digite um numero: '))
#numero2 = int(input('digite um numero: '))
#soma = numero1 + numero2
#print (soma)

#dado = True
#print('dado')

#exercicio 2 - lista
#Obs.: a lista pode ser acessado qualquer dado tanto em sentido horário como em sentido anti-horário. Falando em lista é precisa usar colchetes "[]"

#lista = [2,36,3,6,4,9,32]
#print(lista [4])

#exercicio 3 - tupla é declara em parenteses mas sao acessadas em colchetes
#tupla1 = (1,2,3)
#tupla2 = ('a','b','c')
#print (tupla2)

#-----------------------------------------------------------------------
#aula2: veremos condicionais, loops, while, funções
#para acrescentar uma nova informação numa lista pode utilizar a função "append"
#lista = [2,36,3,6,4,9,32]
#lista.apppend(2)
#print(lista)

#exercicio 4: condicionais é uma forma de fazer o computador fazer escolhas. Para isso é necessario usar a função "IF"

#exemplo: if 'condição == True': faça isso

#n1 = 10
#n2 = 2
#if n1>n2:
    #print('10 é maior')
#else:
        #print('10 é menor')

#cidade = input('Digite sua cidade: ')
#resultado_cidade = "São Paulo"
#if cidade == resultado_cidade:
    #print("vá para o sul")
#else:
        #print("vá para o norte")

#Exercicios aula2 - 2A

#***1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.***
#numero = 5
#resultado_tipo = type (numero)
#print(resultado_tipo)
#calculadora = numero **2
#print(calculadora)


#***2 -Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.***
#nome = str(input ('Insira seu nome: '))
#sobrenome = str(input ('Insira seu sobrenome: '))
#print(nome, sobrenome)

 
#***3 -Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.***
#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite outro número: '))

#var1 = numero_1
#var2 = numero_2

#print (var1 , var2)


#***4 -Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.***
#texto = "Python"
#numero = 3
#print(texto, numero)

#***5 -Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.***
#frase = "Quero aprender linguagem Python"
#print (frase)
#digite = input ('digite seu nome: - ')
#print (frase, digite)


#***Exercício 1: Coletando Dados de Experimentos***

#*Você está conduzindo experimentos em um laboratório para analisar o desempenho
#de diferentes modelos de machine learning. Utilize o método append() para adicionar
#os resultados de cada experimento à sua lista de resultados.*

#resolução
#lista = [0, 10, 3, 5, 98, 3, 1]
#lista.append (45)
#print (lista)


#*Exercício 2: Analisando a Soma de Dados de Vendas*
#*Você está trabalhando com dados de vendas de uma loja online. Utilize o
#método sum() para calcular o total de vendas realizadas durante um período
#de tempo específico.*

#resolução
#vendas = [150, 220, 180, 210, 190]
#soma = sum(vendas)
#print (soma)


#*Exercício 3 : Identificando o Melhor Modelo de Machine Learning*

#*Você está comparando o desempenho de diferentes modelos de machine
#learning para um problema de classificação. Utilize o método max() para
#encontrar a precisão máxima alcançada pelos modelos.*

#resolução
#precisoes = [0.85, 0.92, 0.78, 0.88, 0.90]
#maximo = max(precisoes)
#print (maximo)


#*Exercício 4: Limpeza de Dados*

#*Você recebeu um conjunto de dados para análise, mas ele está cheio
#de valores nulos e duplicados. Utilize o método clear() para limpar o
#conjunto de dados antes de começar a análise.*

#resolução
#dados = [120, 130, None, 140, 120, 150, None]
#limpar = dados.clear()
#print (limpar)


#*Exercício 5: Copiando um Conjunto de Dados*

#*Você está trabalhando em um projeto de análise de dados em equipe e precisa
#compartilhar uma versão do conjunto de dados sem modificar o original.
#Utilize o método copy() para criar uma cópia do conjunto de dados.*

#resolução
#dados_originais = [35, 40, 45, 50, 55]
#copia = dados_originais.copy()
#print (copia)


#*Exercício 6 : Expandindo o Conjunto de Dados*

#*Durante a análise de dados, você percebe que precisa incluir mais amostras
#para obter resultados mais precisos. Utilize o método extend() para adicionar
#novas amostras ao conjunto de dados existente.*

#resolução
#amostras = [0.5, 0.6, 0.7]
#inclusao = amostras.extend([0.8, 0.9, 10.0, 10.1])
#print (amostras)


#*Exercício 7: Contando Valores Únicos*

#*Você está explorando um conjunto de dados e deseja contar quantos valores
#únicos existem em uma determinada coluna. Utilize o método count() para contar
#a frequência de cada valor na coluna.*

#resolução
#coluna = ["A", "B", "C", "A", "B", "D", "E"]
#count_valores_unicos = coluna.count("A")
#print (count_valores_unicos)


#*Exercício 8: Localizando um Registro no Conjunto de Dados*

#*Durante a análise de dados, você precisa encontrar a posição de um
#registro específico no conjunto de dados. Utilize o método index() para localizar
#o registro desejado.*

#resolução
#registros = ["ID-001", "ID-002", "ID-003", "ID-004"]
#posicao = registros.index("ID-003")
#print(posicao)


#*Exercício 9 : Inserindo Novos Dados no Conjunto*

#*Durante a análise de dados, você recebe novos registros que
#precisam ser adicionados ao conjunto de dados existente.
#Utilize o método insert() para inserir os novos registros na posição desejada.*

#resolução
#registros = ["ID-001", "ID-002", "ID-004", "ID-005"]
#adicao = registros.insert (1,"ID-007")
#print (registros)

#Criar um sistema de E-commerce
#print ('Olá! vamos iniciar sua compra, mas primeiro insira seus dados.')
#solicitar_senha = input('Sua Senha...' )
#solicitar_RG = input('Seu RG...' )
#solicitar_CPF = input('Seu CPF...' )
#solicitar_Email = input('Seu Email...' )

#print (solicitar_senha, solicitar_RG, solicitar_CPF, solicitar_Email)

#print ('Selecione seus produtos ... ')

#produtos = [['Arroz $10.00'], ['Feijão $5.00'], ['Óleo $6.10'], ['Pasta $1.45'], ['Shampoo $9,20'], ['Condicionador $10.01'], ['Batata $4.00 kg'], ['Cenoura $3.00 kg']]

#print (produtos)

#selecione_produtos = input ('>>')

#print ("Confirme seu pedido: ", selecione_produtos,
       #"Sim - Digite 1", "Não - Digite 2")

#confirmacao_compra = input (">>")

#if confirmacao_compra == "1":
   # print(f'''Obrigado por comprar conosco. Você será direcionado para a página de pagamento. 
         #''')
#else: 
    #print('Rever sua compra')
    #break

#confirmacao_pagamento = ['1 - Cartão de débito'], ['2 - Cartão de crédito'], ['3 - PIX']
#print (confirmacao_pagamento)
#inserir_pgto = input (">>")


#if confirmacao_pagamento == ['1 - Cartão de débito'] and ['2 - Cartão de crédito'] or ['3 - PIX']: 
   # print ('Sua compra foi finalizada. Em Breve você receberá em seu E-mail o código do pedido e o código de rastreio.')
    
#elif confirmacao_pagamento != ['1 - Cartão de débito'] and ['2 - Cartão de crédito'] or ['3 - PIX']:
   #print ('Insira um método de pagamento válido')
  
#else:
    #print ('Obrigado!')

#***Desafio:***

#Crie um sistema de Banco, onde o usuário pode digitar a senha apenas 3 x, após isso existirá o bloqueio do sistema.  

#saque (subtração)

#deposito(soma)

#visualizar o valor em conta (print())

entrar_conta = str(4789)
print ('Olá, insira sua senha')

for n in entrar_conta:
    acesso  = input('>>')
    if acesso  != entrar_conta:
       print('Negado')
       if n  == 0:
          print('Chances esgotadas') 
    else:
        print('Autorizado')
        break
    
print ('O que deseja fazer?')
input (">>")

deposit = 'Depósito'
saque = 'Saque'
valor_conta = (('Extrato')), (str(700.00))

print (deposit)
print (saque)
print (valor_conta)

if deposit:
    valor_dep = input ('digite valor de deposito')
    print ()
    sub = 700.00 - valor_dep
    print (sub)
else:
    print ('Finalizar')





    
        



    







