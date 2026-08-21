print ('Bem vindo(a) , a nossa calculadora!')
print ('Para encerrar as operações digite "S"')

def calcular(num1,num2,operador):
        if operador == '+':
            return num1 +num2
        elif operador == '-':
            return num1-num2
        elif operador == '*':
            return num1*num2
        elif operador == '/':
            if num2 == 0:
                raise ValueError('Divisão por zero não é permitida.')
            return num1/num2
# while True:
#     print ('Escolha a operação desejada:')
#     print ('+ - Adição')
#     print ('- - Subtração')
#     print ('* - Multiplicação')
#     print ('/ - Divisão')

#     operador = input('Digite o operador: ')

#     if operador.lower() == 's':
#         print('Encerrando a calculadora ...')
#         break

#     if operador not in ['+','-','*','/']:
#         print ('Operador inválido. Tente novamente.')
#         continue

#     try:
#         num1 = float(input('Digite o primeiro número: '))
#         num2 = float(input('Digite o segundo número: '))
#     except ValueError:
#         print ('Erro: Por favor, digite um número válido.')
#         continue

#     try:
#         resultado = calcular(num1,num2,operador)
#         print (f'resultado: {resultado}')
#     except ValueError as erro:
#         print(f'Erro: {erro}')
#     continue
       