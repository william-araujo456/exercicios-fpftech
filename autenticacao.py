# Início do programa de autenticação de usuário

def autenticacao_usuario():
    usuario_correto = 'admin'
    senha_correta = '1234'
    tentativas = 0
    limite_tentativas = 3

    while tentativas < limite_tentativas:
        print('Login de Sistema')
        usuario = input('Digite o usuário: ')
        senha = input('Digite a senha: ')

        if usuario == usuario_correto and senha == senha_correta:
            print('Credenciais corretas!')
            menu_principal()
            return

        else:
            tentativas += 1
            print(f'Credenciais inválidas. Tentativa {tentativas} de {limite_tentativas}\n')

    print('Acesso bloqueado. Número máximo de tentativas excedido.')

def menu_principal():
    print('\nMenu Principal')
    print('[1] - Opção A')
    print('[2] - Opção B')
    print('[3] - Opção C')

autenticacao_usuario()

# Fim do programa
