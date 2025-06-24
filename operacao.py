faturamento = 100
custo = 700 

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1      # multiplicar
lucro = faturamento - custo - imposto    # subtrair

print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)

restituição = imposto * 0.1
print(restituição)

# Mod resto da divisão
# 10 % 3
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")
