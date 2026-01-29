from crud import (
    criar_tabela,
    inserir_cliente,
    listar_clientes,
    atualizar_cliente,
    excluir_cliente
    )

criar_tabela()

while True:
    print('\n1 - Cadastrar cliente')
    print('2 - Listar clientes')
    print('3 - Atualizar cliente')
    print('4 - Excluir cliente')
    print('0 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        nome = input('Nome: ')
        email = input('Email: ')
        idade = int(input('Idade: '))
        inserir_cliente(nome, email, idade)
        print('Cliente cadastrado!')
        
    elif opcao == '2':
        clientes = listar_clientes()
        for c in clientes:
            print(c)

    elif opcao == '3':
        id_cliente = int(input('ID do cliente a ser atualizado: '))
        nome = input('Novo nome: ')
        email = input('Novo email: ')
        idade = int(input('Nova idade: '))
        atualizar_cliente(id_cliente, nome, email, idade)
        print('Cliente atualizado!')

    elif opcao == '4':
        id_cliente = int(input('ID do cliente a ser excluído: '))
        excluir_cliente(id_cliente)
        print('Cliente excluído!')

    elif opcao == '0':
        break

    else:
        print('Opção inválida!')
        