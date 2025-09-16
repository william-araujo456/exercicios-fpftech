# Início do programa de cadastro de cliente

def cadastrar_cliente():

    print('Cadastro de Cliente')

    nome = input('Digite o seu nome: ') # Inserir seu nome
    cpf = input('Digite o seu CPF: ') # Inserir CPF (ex: 111.222.333-44)
    email = input('Digite o seu e-mail: ') # Inserir E-mail

    print('\nCliente cadastrado com sucesso!') # Exibe a mensagem de cadastro efetuado

    # Exibe os dados do cliente
    print('\nDados do Cliente: ')
    print(f'Nome: {nome}')
    print(f'CPF: {cpf}')
    print(f'E-mail: {email}')

# Chama a função
cadastrar_cliente()

# Fim do programa
