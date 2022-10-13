
# config das divisões:
div = 39 * '=' + '\n'

# home

i = 0

while i == 0:
        print('\n' + div)
        print('    Bem vindo à calculadora geral!\n    Escolha uma das opções abaixo:')

        print("""

        1 - Soma
        2 - Multiplicação
        3 - Divisão
        4 - Potência

        """)
        
        i = int(input('        > '))

        print('\n' + div)

                # laço lista
        while i == 1:
                print('        Você escolheu a opção de soma!')
                print('        Digite a quantidade de números que deseja somar:\n')
                repetsoma = int(input('       > '))
                
                print('\n\nDigite os números a serem somados:\n')
                while i <= repetsoma:
                        numsoma = float(input('       > '))
                        numsoma = numsoma + numsoma
                        i = i + 1
                        
                print('\nO resultado da soma é', numsoma)
                input('\n>>Aperte enter para continuar<<')
        
        i = 0
                # end laço lista

# end home


