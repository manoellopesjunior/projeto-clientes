from crud import criar_tabela, inserir_cliente, listar_clientes

criar_tabela()

while True:
    print('\n1 - Cadastrar cliente')
    print('2- Listar clientes')
    print('0 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        nome = input('Nome: ')
        email = input('Email: ')
        idade = input('Idade: ')
        inserir_cliente(nome, email, idade)
        print('Cliente cadastrado!')
        
    elif opcao == '2':
        clientes = listar_clientes()
        for c in clientes:
            print(c)

    elif opcao == '0':
        break

    else:
        print('Opção inválida!')
        