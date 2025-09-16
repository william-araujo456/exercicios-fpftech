# Início do programa de caixa eletrônico

def caixa_eletronico():

    saldo = 5000

    while True:
        print('===== CAIXA ELETRÔNICO - MAZE BANK =====')
        print('SEJA BEM-VINDO(A), O QUE VOCÊ QUER FAZER?')
        print('[1] - SAQUE')
        print('[2] - DEPÓSITO')
        print('[3] - CONSULTAR SALDO')
        print('[4] - SAIR')

        opcao = int(input('\nESCOLHA UMA OPÇÃO: '))

        match opcao:

            case 1:
                saque = float(input('\nDIGITE O VALOR QUE DESEJA SACAR: R$'))

                if saque <= 5000:
                    saldo -= saque
                    print(f'SAQUE DE R${saque} FEITO COM SUCESSO!')
                    print(f'SALDO RESTANTE: R${saldo}')

                else:
                    print('SALDO INSUFICIENTE PARA SAQUE!')

            case 2:
                deposito = float(input('\nDIGITE O VALOR QUE DESEJA DEPOSITAR: R$'))
                saldo += deposito
                print(f'DEPÓSITO DE R${deposito} FEITO COM SUCESSO!')
                print(f'SALDO RESTANTE: R${saldo}')

            case 3:
                print(f'SEU SALDO ATUAL É DE R${saldo}')

            case 4:
                print(f'\nFINALIZANDO PROGRAMA, OBRIGADO POR UTILIZAR O MAZE BANK!')
                break

            case _:
                print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!\n')

# Chama a função
caixa_eletronico()

# Fim do programa