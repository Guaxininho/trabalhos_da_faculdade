# QUESTÃO 3

nome_do_lojista = "Samuel Cavalcanti Rodrigues"
ru = 4492243

print('Bem vindo a transportadora do {}, nos localizamos próximo ao mercado municipal no número {}'.format(
    nome_do_lojista, ru))


def dimensoesObjeto():
    while True:
        try:
            altura = int(
                input("Por favor digite a altura do seu produto em cm: "))
            comprimento = int(input(
                "Por favor digite o comprimento do seu produto em cm: "))
            largura = int(
                input("Por favor digite a largura do seu produto em cm: "))

            volume = altura * largura * comprimento
            if (volume < 1000):
                return 10
            elif (1000 <= volume and volume < 10000):
                return 20
            elif (10000 <= volume and volume < 30000):
                return 30
            elif (30000 <= volume and volume < 100000):
                return 50
            elif (volume >= 100000):
                print(
                    "Não aceitamos levar um conteúdo dessa dimensão, por favor escolha uma dimensão menor")
        except:
            print("Os campos foram preenchidos de forma incorreta")


def pesoObjeto():
    while True:
        try:
            peso = float(
                input("Por favor digite o peso do seu produto em kg: "))

            if (peso <= 0.1):
                return 1
            elif (peso > 0.1 and peso < 1):
                return 1.5
            elif (peso >= 1 and peso < 10):
                return 2
            elif (peso >= 10 and peso < 30):
                return 3
            else:
                print(
                    "Não aceitamos levar um conteúdo que seja tão pesado, por favor escolha um peso menor")
        except:
            print("Os campos foram preenchidos de forma incorreta")


def rotaObjeto():
    while True:
        try:
            rota = input("Por favor digite a rota do seu produto: ")
            if (rota == "RJ"):
                return 1
            elif (rota == "ES"):
                return 1.2
            elif (rota == "MG"):
                return 1.5
            else:
                print(
                    "Não levamos mercadoria para esse lugar, só trabalhamos atualmente com minas, rio e espírito santo")
        except:
            print(
                "Por favor digite uma opção válida, nossas opções são: RJ, ES ou MG")


preco_por_dimensao = dimensoesObjeto()
multiplicador_por_peso = pesoObjeto()
multiplicador_por_rota = rotaObjeto()
total_a_pagar = preco_por_dimensao * \
    multiplicador_por_peso * multiplicador_por_rota

print("Total a pagar: {} (dimensão: {} * peso: {} * rota {})".format(total_a_pagar,
      preco_por_dimensao, multiplicador_por_peso, multiplicador_por_rota))

