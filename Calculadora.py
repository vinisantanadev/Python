
# config das divisões & outras estéticas
div = 39 * '=' + '\n'
userinput = 8 * ' '

# inicio do app
# laço do app

#variaveis
i = 1
rescalc = 0
operador = '='

        
print('\n' + div)

print('Bem vindo à calculadora')
print('Você sempre pode ver um tutorial de uso digitando help!\n')

# atualizar conforme as opções aumentam
while operador != '.' or operador != 'exit':

        # numero incial do usuário
        if operador == '=':
                calculo = float(input(userinput + 'num> '))
        
        # caso o usuário queira ver o tutorial
        if operador == 'h' or operador == 'help':
                print('\nComece digitando um número\nEm seguida digite o operador desejado\nComo * ou +, por exemplo\nDigite = para terminar a conta e exibir o resultado\nE o app faz o resto!\nDigite . para sair do app\n\n' + div)

                calculo = float(input(userinput + 'num> '))

        # input que vai decidir a conta do usuário 
        if operador == '=':
                operador = input(userinput + 'ope> ')

        # caso o usuário digite +
        while operador == '+':

                num = float(input(userinput + 'num> '))
                calculo = calculo + num
                operador = (input(userinput + 'ope> '))

        # caso o usuário digite -
        while operador == '-':
                num = float(input(userinput + 'num> '))
                calculo = calculo - num
                operador = (input(userinput + 'ope> '))

        # caso o usuário digite *
        while operador == '*':
                num = float(input(userinput + 'num> '))
                calculo = calculo * num
                operador = (input(userinput + 'ope> '))
        
        # caso o usuário digite **
        while operador == '**':
                num = float(input(userinput + 'num> '))
                calculo = calculo ** num
                operador = (input(userinput + 'ope> '))

        # caso o usuário digite /
        while operador == '/':
                num = float(input(userinput + 'num> '))
                calculo = calculo / num
                operador = (input(userinput + 'ope> '))
                
        # caso o usuário digite %
        while operador == '%':
                calculo = calculo % 2 # par ou impar
                if calculo == 0:
                        print('\n        Este número é par!')

                else:
                        print('\n        Este número é impar!')


                print('        -------------------\n')

                operador = (input(userinput + 'ope> '))

        # printa o resultado caso o usuário digite =
        while operador == '=':
                print('\n' + 7 * ' ', calculo)
                print('        -------------------\n')
                
                # continua a conta
                operador = (input(userinput + 'ope> '))
        
        # terminar o programa caso o usuário digite .
        if operador == '.' or operador == 'exit':
                break
print('\n' + div)

# end laço do app
# end app

