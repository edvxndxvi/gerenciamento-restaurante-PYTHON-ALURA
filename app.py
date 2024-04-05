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

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite qualquer tecla para voltar ao menu principal")
    main()

def cadastrar_restaurante():
    os.system("cls")
    print("""
------------------------------------------ 
SABOR EXPRESS - CADASTRAR RESTAURANTES
------------------------------------------ 
    """)
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O resutarante {nome_restaurante} foi cadastrado com sucesso!")
    input("\nDigite qualquer tecla para voltar ao menu principal")
    main()

def listar_restaurantes():
    os.system("cls")
    print("""
------------------------------------------ 
SABOR EXPRESS - LISTAR RESTAURANTES
------------------------------------------ 
    """)
    if(not restaurantes):
        print("Nenhum restaurante cadastrado no momento.")
    else:
        for restaurante in restaurantes:
            print(f".{restaurante}")

    input("\nDigite qualquer tecla para voltar ao menu principal")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar Restaurante")
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