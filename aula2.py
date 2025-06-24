faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "qualquercoisaaleatorio@gmail.com"

# letra maiúscula
email_cliente = email_cliente.upper()
print(email_cliente)

# letra minúscula
email_cliente = email_cliente.lower()
print(email_cliente)

# posição do caractere "@"
print(email_cliente.find("@"))

# tamanho do texto
print(len(email_cliente))

# pegar um caractere específico
print(email_cliente[4])       # 5ª letra
print(email_cliente[-4])      # 4ª letra de trás pra frente

# pegar um pedaço do texto
print(email_cliente[4:10])    # da posição 4 até a 9

# trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

# trabalhar com nomes
nome = "gislayne santos"
print(nome.capitalize())  # Primeira letra maiúscula
print(nome.title())       # Primeira letra de cada palavra maiúscula

# pegar servidor do e-mail
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

# pegar primeiro nome e sobrenome
primeira_posicao = nome.find(" ")
primeiro_nome = nome[:primeira_posicao]
sobrenome = nome[primeira_posicao + 1:]

print(primeiro_nome)
print(sobrenome)

# casos especiais - formatações numéricas em texto
margem_lucro = lucro / faturamento
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}, Margem: {margem_lucro:%}")
