faturamento = 1200 # tipo int numero inteiro
custo = 750.32 # tipo float numero decimal
novas_vendas = 250
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1


lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento


print ("o faturamento foi de:" , faturamento)
print ("O custo foi de;" ,custo)
print ("O lucro foi de;" , lucro)
print ("a margem de lucro doi de;", round(margem_lucro,2))

mensagem = "o faturamento da loja foi de tanto"
email = "emailqualquer@gmail.com" #tipo string -> texto

teve_lucro = True # variavel tipo boolean

# Mod -> % o resto da divisão
tempo_contrato = 170 
tempo_anos = 170 / 12
print ("tempo em anos;", int(tempo_anos))
tempo_meses = 170 % 12
print("tempo em meses;", tempo_meses)
