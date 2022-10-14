
# config das divisões:2
div = 39 * '=' + '\n'

# inicio do app
# laço do app

#variaveis
i = 0
rescalc = 0

while i == 0:
        print('\n' + div)

        print('Bem vindo à calculadora geral!\nEscolha uma das opções abaixo:')

        # opções de calculo
        print("""

        1 - Soma
        2 - Multiplicação
        3 - Potência
        4 - Divisão

        """)

        # usuário escolhe a opção
        # variavel do tipo char para passar pelo if
        i = input('        > ')
        
        # caso o usuário digite um número errado
        # atualizar conforme o número de opções aumentar
        if i != '1' and i != '2' and i != '3' and i != '4':
                print('\n\nOpção inválida!\n')
                
                input('>> Aperte enter para continuar <<')
                
                i = 0

        # transforma a variavel para número inteiro
        i = int(i)

        print('\n' + div)

        # laço soma
        while i == 1:
                # reseta o laço
                i = 0
                
                print('Você escolheu a opção de soma!')

                print('Digite a quantidade de números que deseja somar:\n')

                # pergunta ao usuário quantos números serão somados
                repetelaco = int(input('       > ')) 

                print('\n\nDigite os números a serem somados:\n')

                while i < repetelaco:
                        # pede pro usuário digitar os números
                        numsoma = float(input('       > '))
                        
                        # soma os números
                        rescalc = rescalc + numsoma # soma os números

                        # adiciona 1 ao laço que para de acordo com a quantidade de números que o usuário quis somar
                        i = i + 1

                #mostra o resultado
                print('\nO resultado da soma é', rescalc)
                
                # reseta o resultado
                rescalc = 0

                # input para pausar o laço para que o usuário leia as informações antes de continuar
                input('\n>> Aperte enter para continuar <<')
                
                # reseta o laço para que o usuário volte para o início
                i = 0

        # end laço soma
        # ===================================================
        # incio laço multiplicação

        while i == 2:
                # reseta o laço
                i = 0
                
                print('Você escolheu multiplicação!\n')

                print('Digite a quantidade de números que deseja multiplicar:\n')

                # pergunta ao usuário quantas números quer multiplicar
                repetelaco = int(input('       > '))

                print('\n\nDigite os números à serem multiplicados:')

                rescalc = 1 # se a variavel de resultado estiver em 0 o resultado sempre será 0

                while i < repetelaco:
                        
                        # pede pro usuário digitas os numeros
                        nummulti = float(input('        > '))

                        # multiplica os números
                        rescalc = rescalc * nummulti
                        
                        # adiciona 1 até chegar a quantidade de vezes que o usuário quis repetir
                        i = i + 1
                        
                #mostra o resultado
                print('\nO resultado da multiplicação é:', rescalc)
                
                # reseta o resultado
                rescalc = 0
                
                input('\n>> Aperte enter para continuar <<')
                
                # reseta o laço para que o usuário volte para o início
                i = 0
        # end laço multiplicação
        # ===============================================
# end laço do app
# end app

