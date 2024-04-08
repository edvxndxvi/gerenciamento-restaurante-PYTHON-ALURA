import os #Importando biblioteca Python

restaurantes = []

def exibir_nome_programa():
    print("""
------------------------------------------
              SABOR EXPRESS
------------------------------------------
    """)

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls") # Limpando o CMD
    print("Finalizando programa...")

def exibir_subtitulo(texto):
    os.system("cls")
    print(f"""
-----------------------------------------------------
  SABOR EXPRESS - {texto}
-----------------------------------------------------
    """)

def voltar_ao_menu():
    input("\nDigite qualquer tecla para voltar ao menu principal")
    main()

def opcao_invalida():
    print("Opção inválida")
    voltar_ao_menu()

def cadastrar_restaurante():
    exibir_subtitulo("CADASTRAR RESTAURANTES")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite qual categoria do restaurante {nome_restaurante}: ")
    dados_restaurantes = {"nome":nome_restaurante, "categoria":categoria_restaurante, "ativo":False}
    restaurantes.append(dados_restaurantes)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("LISTAR RESTAURANTES")
    if(not restaurantes):
        print("Nenhum restaurante cadastrado no momento.")
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante["nome"]
            categoria_restaurante = restaurante["categoria"]
            ativo_restaurante = restaurante["ativo"]
            print(f" - {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}")

    voltar_ao_menu()

def alternar_estado():
    exibir_subtitulo("ALTERANDO ESTADO DE RESTAURANTES")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado. Verifique se está digitando corretamente o nome do restaurante")

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

# Definindo este arquivo como o principal do programa
def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ ==  '__main__':
    main()