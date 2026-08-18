print ('Bem vindo(a) , a nossa calculadora!')
print ('Para encerrar as operações digite "S"')

while True:
    print ('Escolha a operação desejada:')
    print ('+ - Adição')
    print ('- - Subtração')
    print ('* - Multiplicação')
    print ('/ - Divisão')

    operador = input('Digite a operação desejada:')
    if operador == 'S' or operador == 's':
        print ('Encerrando a calculadora...')
        break
    if operador not in ['+', '-', '*', '/']:
        print ('Operação inválida! Tente novamente.')
        continue
    if operador in ['+', '-', '*', '/']:

        try:
            num1 = float(input('primeiro número:'))
            num2 = float(input('segundo número:'))

            if operador == '+':
                resultado = num1 +num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print('Não é possível dividir por zero!')
                    continue
                resultado = num1 / num2
            print(f'O resultado da operação {num1} {operador} {num2} é: {resultado}')

        except ValueError:
            print('digite apenas números!')
            continue