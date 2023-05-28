# QUESTÃO 2

nome_do_lojista = "Samuel Cavalcanti Rodrigues"
ru = 4492243

print('Bem vindo a Lanchonete do {}, nos localizamos no centro no número {}'.format(
    nome_do_lojista, ru))

# Achei importante mostrar o catálogo de código para o usuário, se não fica difícil escolher o lanche, então coloquei ele aqui
print('Aqui está o nosso catálogo de código para os produtos:')
catalogo = """100	Cachorro-Quente	9,00
101	Cachorro-Quente Duplo	11,00
102	X-Egg	12,00
103	X-Salada	13,00
104	X-Bacon	14,00
105	X-Tudo	17,00
200	Refrigerante Lata	5,00
201	Chá Gelado	4,00
"""
# Usei o método split para splitar baseado na quebra de linha
linhas = catalogo.split('\n')

# e um loop para iterar um print a cada linha
for linha in linhas:
    print(linha)

# Iniciando a variável que vai controlar o preço total
valor_total = 0

# Iniciando a variável que vai controlar a continuação do programa
continuar = 'sim'

while (continuar == 'sim'):
    # Capturando a entrada para o produto escolhido e convertendo ele para inteiro, a partir daqui a ideia é de acordo com o código adicionar um valor na variável que controla o  preço total e imprimir qual lanche ele pegou, se ele continuar vai ter que inserir um novo código que será adicionado também a variável de preço, no fim quando ele escolher não, vai imprimir o preço total da variável e sair do loop finalizando o programa:
    produto_escolhido = int(input(
        'Qual o código do produto que você deseja? Se não desejar nada é só digitar o número zero: '))
    if (produto_escolhido == 100):
        print("Seu cachorro quente foi adicionado ao carrinho")
        valor_total = valor_total + 9.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 101):
        print("Seu cachorro quente duplo foi adicionado ao carrinho")
        valor_total = valor_total + 11.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 102):
        print("Seu X-Egg foi adicionado ao carrinho")
        valor_total = valor_total + 12.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 103):
        print("Seu X-Salada foi adicionado ao carrinho")
        valor_total = valor_total + 13.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 104):
        print("Seu X-Bacon foi adicionado ao carrinho")
        valor_total = valor_total + 14.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 105):
        print("Seu X-Tudo foi adicionado ao carrinho")
        valor_total = valor_total + 17.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 200):
        print("Seu Refrigerante Lata foi adicionado ao carrinho")
        valor_total = valor_total + 5.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 201):
        print("Seu Chá Gelado foi adicionado ao carrinho")
        valor_total = valor_total + 4.00
        continuar = input(
            'Gostaria de pedir mais alguma coisa? Digite sim ou não: ').lower()
        if (continuar == 'não'):
            print('O valor total da sua compra foi de {:.2f}, muito obrigado por comprar com a gente, volte sempre!'.format(
                valor_total))
    elif (produto_escolhido == 0):
        break
    else:
        print('Opção inválida')
        continue
