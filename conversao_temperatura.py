# Início do programa de conversão de temperatura

def conversao():
    print('Programa de Conversão de Celsius para Fahrenheit ou Kelvin')
    celsius = float(input('Digite a Temperatura em Celsius: '))

    print('Opções de Conversão')
    print('[1] - Fahrenheit')
    print('[2] - Kelvin')

    opcao = input('Digite a opção que você deseja converter: ')

    if opcao == '1':
        fahrenheit = (celsius * 1.8) + 32
        print(f'A temperatura em Fahrenheit é igual a {fahrenheit:.2f}ºF')
    elif opcao == '2':
        kelvin = celsius + 273.15
        print(f'A temperatura em Kelvin é igual a {kelvin:.2f}K')
    else:
        print('Opção inválida')

conversao()

# Fim do programa