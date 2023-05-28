# QUESTÃO 1

nome_do_lojista = "Samuel Cavalcanti Rodrigues"
ru = 4492243

print('Bem vindo a Loja do {}, nos localizamos na Avenida Rio Branco no número {}'.format(
    nome_do_lojista, ru))
# Capturando a entrada do preço do produto e convertendo para float
valor_do_produto = float(input('Insira o valor do produto:'))
# Capturando entrada da quantidade de produtos e convertendo ela para inteiro
quantidade_comprada = int(input('Insira a quantidade de produtos:'))

# Testando a partir da quantidade de produtos comprados quanto de desconto o cliente terá e qual mensagem ele vai receber
if (quantidade_comprada < 10 and quantidade_comprada > 0):
    preco_total = valor_do_produto * quantidade_comprada
    print('O valor total da compra é de {:.2f}'.format(preco_total))
elif (quantidade_comprada >= 10 and quantidade_comprada < 100):
    preco_total = valor_do_produto * quantidade_comprada
    print('O valor total da compra é de {:.2f}'.format(preco_total))
    porcentagem = 5
    desconto = (preco_total / 100) * porcentagem
    preco_total = preco_total - desconto
    # Aqui eu tive que usar o raw string só porque %d poderia dar problema, tirei isso dos meus estudos de regex, espero que não seja errado usar agora
    print(r'Você recebeu {}% de desconto, valor total da compra com desconto é de {:.2f}'.format(
        porcentagem, preco_total))
elif (quantidade_comprada >= 100 and quantidade_comprada < 1000):
    preco_total = valor_do_produto * quantidade_comprada
    print('O valor total da compra é de {:.2f}'.format(preco_total))
    porcentagem = 10
    desconto = (preco_total / 100) * porcentagem
    preco_total = preco_total - desconto
    print(r'Você recebeu {}% de desconto, valor total da compra com desconto é de {:.2f}'.format(
        porcentagem, preco_total))
elif (quantidade_comprada >= 1000):
    preco_total = valor_do_produto * quantidade_comprada
    print('O valor total da compra é de {:.2f}'.format(preco_total))
    porcentagem = 15
    desconto = (preco_total / 100) * porcentagem
    preco_total = preco_total - desconto
    print(r'Você recebeu {}% de desconto, valor total da compra com desconto é de {:.2f}'.format(
        porcentagem, preco_total))
else:
    # Tentativa de evitar os erros que conseguir pensar
    print('o número que você digitou para quantidade não é um número válido, por favor não use números negativos ou zero')
