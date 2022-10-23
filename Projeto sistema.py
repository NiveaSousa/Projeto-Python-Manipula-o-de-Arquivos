#Projeto da disciplina de Logica de programação II

import json

#Função Ler Arquivo
def lerArquivo(ler=True, nomeArquivo='projetoModuloII.json'):
    if ler:
        with open('projetoModuloII.json', 'r',  encoding="utf-8" ) as projeto:
            dados = json.load(projeto)
        return dados

dados1 = lerArquivo()        

#Função para encerrar o programa e salvar o arquivo

def encerrarPrograma(arquivo, nomeArquivo='projetoModuloII.json'):
    with open('projetoModuloII.json', 'w', encoding='utf-8') as projeto:
        json.dump(arquivo, projeto)
        
#Função Adicionar usuário

def addUsuario(**usuario):
        nome = input('Insira nome:\n')
        telefone = input('Insira telefone:\n')
        endereco = input('Insira endereço:\n')        
        while nome == "":
            nome = input('Nome obrigatório, insira:\n')
        usuario = {"Status": False, "Nome": nome, "Telefone": telefone, "Endere\u00e7o": endereco}
        if usuario in dados1.values():
            posicao = list(dados1.values()).index(usuario)
            dados1[str(posicao+1)]["Status"] = True
            return(f'Usuário existente, cadastro reativado')
        else: 
            id = len(dados1) +1
            dados1[id] = usuario
            dados1[id]['Status'] = True 
            outro_usuario = int(input('Usuário cadastrado. Deseja inserir mais um?\n1- Sim \n2- Não\n'))
            if outro_usuario == 1:
                addUsuario()
            else:
                encerrarPrograma(dados1)
        
#Função Excluir um usuário 

def excluirUsuario(usuario):
    while usuario not in dados1.keys():
        usuario = input('Usuário não encontrado!\nInsira um ID de usuário válido:\n')        
    else:
        if dados1[usuario]['Status'] == True:
            dados1[usuario]['Status'] = False
            print('Cadastro cancelado!')      
        else: 
            print('Cadastro já cancelado anteriormente ou inexistente.') 
    
#Função para editar/atualizar usuários

def editUsuario(dados1, ids):
    for usuario in ids:
        u_validos = True
        while u_validos:
            if usuario in dados1:
                print(f"ID: {usuario}")
                opcao = '0'
                while opcao != 4:  
                    print('Qual informação deseja alterar?:\n1 - Nome\n2 - Telefone\n3 - Endereço\n4 - Voltar\n')
                    opcao = input('\nDigite a sua opcao: \n')
                    try:
                        opcao = int(opcao)
                    except:
                        opcao = int(input('Digite número válido:\n'))

                    if opcao == 1:
                        nome = input('Digite o novo nome: ')
                        dados1[usuario].update({'Nome': nome})
                        print('Dados alterados com sucesso!\n')
                        
                    elif opcao == 2:
                        telefone = input('Digite o novo telefone: ')
                        dados1[usuario].update({'Telefone': telefone})
                        print('Dados alterados com sucesso!\n')
                        
                    elif opcao == 3:
                        endereco = input('Digite o novo telefone: ')
                        dados1[usuario].update({'Endere\u00e7o': endereco})
                        print('Dados alterados com sucesso!\n')
                    else:
                        break    
                u_validos = False 
            else:
                print(f"ID {usuario} não encontrado! \n")
                usuario = input('Insira um ID do usuário válido: ') 

#Função para exibir alguns usuários(Informações de um usuário)

def exibirAlgunsUsuarios(dados1, ids):
    for usuario in ids:
        u_validos = True
        while u_validos:
            if usuario in dados1:
                if dados1[usuario]['Status'] == True:
                    print(f"Nome: {dados1[usuario]['Nome']}\nTelefone: {dados1[usuario]['Telefone']}\nEndereço: {dados1[usuario]['Endereço']}\n")
                else:
                    print(f"Usuário do ID {usuario} foi excluído. \n")
                u_validos = False
            else:
                print(f"ID {usuario} não encontrado! \n")
                usuario = input('Insira um ID do usuário válido: ')     

#Função Informações de todos os usuários

def exibirTodosUsuarios():
    for chave, valor in dados1.items():
        if valor['Status'] == True:
            print(f"\nID: {chave}\nNome: {valor['Nome']}\nTelefone: {valor['Telefone']}\nEndereço: {valor['Endereço']}")

# Menu iterativo
    
opcao = '0'
while opcao != 6:

    print('\nBoas vindas ao nosso sistema:\n1 - Inserir usuário\n2 - Excluir usuário\n3 - Atualizar usuário\n4 - Informações de um usuário\n5 - Informações de todos os usuários\n6 - Sair')
    opcao = input('\nDigite a sua opcao: \n')
    try:
        opcao = int(opcao)
    except:
        opcao = int(input('Digite número válido:\n'))

    if opcao == 1:
        print(addUsuario())

    elif opcao == 2:
        print(f"Escolha qual usuário deseja excluir:")
        print(exibirTodosUsuarios())
        usuario = input('Insira o ID do usuário:\n')
        excluirUsuario(usuario)
     
    elif opcao == 3:
        print(f"Escolha qual usuário deseja atualizar:")
        print(exibirTodosUsuarios())
        ids = input('Insira o ID do usuário: ').split(',')
        editUsuario(dados1, ids)

    elif opcao == 4:
        ids = input('Insira o ID do usuário: ').split(',')
        exibirAlgunsUsuarios(dados1, ids)

    elif opcao == 5:
        print(f"Esses são todos os usuários ativos no sistema:")
        exibirTodosUsuarios()

    else:
        encerrarPrograma(dados1)
        print('Alterações salvas, obrigado por acessar nosso sistema!')
        break