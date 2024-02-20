import os

restaurantes = [{"nome": "Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Pizza Suprema", "categoria": "Pizza", "ativo": True},
                {"nome": "Cantina", "categoria": "Italiano", "ativo": False}]


def exibir_nome_do_programa():
    print("""
𝓼𝓪𝓫𝓸𝓻-𝓮𝔁𝓹𝓻𝓮𝓼𝓼
""")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. listar restaurante")
    print("3. aternar estado do restaurante")
    print("4. sair restaurante\n")


def finalizar_app():
    exibir_subtitulo("Finalizar o app")

    print("Finalizando o app\n")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def Cadastrar_novo_restaurante():
    """Essa função é responsavel por cadastrar um novo restaurante"""

    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")

    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}

    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()
    main()


def listar_restaurante():
    exibir_subtitulo("Listando os restaurantes")

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        if restaurante["ativo"]:
            ativo = "ativado"
        else:
            ativo = "desativado"

        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]

            if restaurante["ativo"]:
                print(f"O restaurante {nome_restaurante} foi ativado com sucesso")
            else:
                print(f"O restaurante {nome_restaurante} foi desativado com sucesso")

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            Cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()