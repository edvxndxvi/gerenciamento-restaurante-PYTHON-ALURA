import os #Importando biblioteca Python

def exibir_nome_programa():
    print("""
Sabor Express
    """)
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")
def finalizar_app():
    os.system("cls") # Limpando o CMD
    print("Finalizando programa...")
def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    match opcao_escolhida:
        case 1:
            print("Cadastrar Restaurante")
        case 2:
            print("Listar  Restaurante")
        case 3:
            print("Ativar Restaurante")
        case 4:
            finalizar_app()
        case _:
            print("Opção inválida!")

# Definindo este arquivo como o principal do programa
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ ==  '__main__':
    main()