faturamento = 1000
custo = 700

lucro = faturamento - custo

print(f"faturamento: {faturamento}], Custo: {custo}, Lucro: {lucro}")
print("faturamento:" + str(faturamento) + ", custo:" + str(custo) + ", Lucro:" + str(lucro))


email = "EMAILfalso@gmail.com"

print(email.lower()) # deixar o email em letra minuscula
print(email.find("@"))   # procurar a posição do aroba (ou a posição que eu declarar pra ele encontra)

# essa codigo serve para encontrar, filtrar o email ( serve para o casos em que na empresa se precisa achar o email de alguem, como se alguem tivesse muitos emails cadastrados, filtro com esse codigo e caho pra quem quero mandar emaill)
posicao = email.find("@") # ele ta diznedo que a posicao e apartir do aroba(aroba foi a posição marcada no comando find) no email.
servidor = email[posicao+1:]  # aqui ele ta dizendo para mostrar a partir da posição (find) o email, mas quando eu ponho o +1 to falando pra ele mostrar apartir da proxima letra do aroba, depois da marcacao find (@)
print(servidor) # aqui ele vai mostra em mensagem no executando o email apartir da posicao que eu pedi (uma letra depois do @ (onde declarei que seria o find)


# tamanho de um texto len
tamanho = len(email)
print(tamanho)


#trocar pedaço do texto replace
email_trocado = email.replace("gmail.com", "hotmail.com") # aqui eu faço o comando para ele alterar o pedaço do texto.
print(email_trocado)


nome = "gislayne santos"
print(nome.capitalize()) # capitalize pega a primeira letra da palavra em deixa em maiusculo
print(nome.title()) # o Title coloca toda primeira letra na frase em maiusculo

# especiais
margem = lucro / faturamento   # aqui ta declarando que o margem é o lucro dividido por faturamento e o resultado e a margem
print(f"faturamento: R${faturamento:.2f}, Custo: {custo}, Lucro: {lucro}")  # aqui  esse .2f (. seria para o 1000 do faturamento aparecer com ponto e o 2 mostrar as duas casas decimais e o f de float indicando que ficaria decimal 1000.00 e nao 1000) 
print(f"Margem: {margem:.1%}")  # o f aqui serve pra dizer que o resultado vai ser float. com (.1%) vai mostrar com uma casa decimal, exemplo 30.0% e nao 0.3


#Exercicios abaixo
nome = "Gislayne Silva"
email = "emailfalso2@gmail.com"

# descubra servidor do email
posicao = email.find("@") # ele ta diznedo que a posicao e apartir do aroba(aroba foi a posição marcada no comando find) no email.
servidor = email[posicao+1:]  # aqui ele ta dizendo para mostrar a partir da posição (find) o email, mas quando eu ponho o +1 to falando pra ele mostrar apartir da proxima letra do aroba, depois da marcacao find (@)
print(servidor) 


#pegar o 1º nome do usuario
posicao = nome.find("G") # find serve para encontrar o caractere. marquei para encontrar o G
primeiro_nome = nome[posicao:8]   # aqui disse para me dar 8 caractere GISLAYNE, mas antes pedi pra calcular o valor POSIÇÃO que marquei acima no find (G)
print("Primeiro nome:", primeiro_nome) # aqui falei pra ele mostrar em texto primeiro nome e o resultado encontrado depois da virgula sendo GISLAYNE





# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o email tal
print("Usuario", primeiro_nome, "cadastrado com sucesso com o email", email)



# contrua uma mensagem: enviamos um link de confirmacap para o email email***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"

print(mensagem)


