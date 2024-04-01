import os #Importando biblioteca Python

print("""
Sabor Express
    """)

print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))

def finalizar_app():
    os.system("cls")
    print("Finalizando programa...")

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