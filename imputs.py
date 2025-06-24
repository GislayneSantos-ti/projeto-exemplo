nome = input("digite aqui seu nome:")
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

