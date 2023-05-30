# QUESTÃO 4

nome_do_lojista = "Samuel Cavalcanti Rodrigues"
ru = 4492243

print('Bem vindo ao estoque do {}, nos localizamos próximo a rua Halfeld no número {}'.format(
    nome_do_lojista, ru))

lista_de_pecas = []
peca_criada = 0


def cadastrarPeca(codigo):
    global peca_criada
    print("Você escolheu cadastrar uma peça")
    nome_da_peca = input("Qual o nome da peça? ")
    fabricante = input("Qual o fabricante da peça? ")
    valor_da_peca = float(input("Qual o valor da peça? "))
    peca = {
        "Código": codigo,
        "Nome": nome_da_peca,
        "Fabricante": fabricante,
        "Valor": valor_da_peca
    }
    lista_de_pecas.append(peca)
    peca_criada = peca_criada + 1


def consultarPeca():
    while True:
        tipo_de_consulta = int(input("""Escolha uma das opções desejadas:
        1 - Consultar todas as peças
        2 - Cosultar Peças por código
        3 - Consultar peças por fabricante
        4 - Retornar: """))

        if (tipo_de_consulta == 1):
            for dicionario in lista_de_pecas:
                print("=========================")
                print(dicionario)
        elif (tipo_de_consulta == 2):
            codigo_ver = int(
                input("Qual o código do produto que gostaria de ver? "))
            for dicionario in lista_de_pecas:
                if (dicionario.get("Código") == codigo_ver):
                    print(dicionario)
        elif (tipo_de_consulta == 3):
            codigo_fab = input(
                "Qual o nome do fabricante que gostaria de ver? ")
            for dicionario in lista_de_pecas:
                if (dicionario.get("Fabricante") == codigo_fab):
                    print(dicionario)
        elif (tipo_de_consulta == 4):
            break


def removerPeca():
    codigo_de_remocao = int(
        input("Qual o código do produto que deseja remover? "))
    for dicionario in lista_de_pecas:
        if (dicionario.get("Código") == codigo_de_remocao):
            lista_de_pecas.remove(dicionario)
            print("Essa peça foi removida com sucesso!")


while (True):
    numero_escolhido = int(input("""Escolha uma das opções desejadas:
    1 - Cadastrar Peças
    2 - Cosultar Peças
    3 - Remover Peças
    4 - Sair: """))
    if (numero_escolhido == 1):
        cadastrarPeca(peca_criada)
    elif (numero_escolhido == 2):
        consultarPeca()
    elif (numero_escolhido == 3):
        removerPeca()
    elif (numero_escolhido == 4):
        print("Volte sempre")
        break
    else:
        print("Por favor digite uma opção válida")
