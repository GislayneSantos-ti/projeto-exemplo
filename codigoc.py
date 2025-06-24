import tkinter as tk

# Dados simulados
faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = round(lucro / faturamento, 2)

email_cliente = "qualquercoisaaleatorio@gmail.com"
email_maiusculo = email_cliente.upper()
email_minusculo = email_cliente.lower()
posicao_arroba = email_cliente.find("@")
tamanho_email = len(email_cliente)
caractere_5 = email_cliente[4]
caractere_menos4 = email_cliente[-4]
fatia_email = email_cliente[4:10]
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
servidor = email_cliente[posicao_arroba + 1:]

nome = "gislayne santos"
primeira_posicao = nome.find(" ")
primeiro_nome = nome[:primeira_posicao]
sobrenome = nome[primeira_posicao + 1:]
nome_cap = nome.capitalize()
nome_title = nome.title()

# Criação da janela
janela = tk.Tk()
janela.title("Informações da Empresa e Cliente")
janela.geometry("500x600")
janela.configure(bg="#f0f0f0")

# Função para exibir dados em labels
def mostrar_texto(texto):
    label = tk.Label(janela, text=texto, anchor="w", justify="left", bg="#f0f0f0", font=("Arial", 10))
    label.pack(fill="both", padx=10, pady=2)

# Mostrando os dados
mostrar_texto(f"Faturamento: R$ {faturamento}")
mostrar_texto(f"Custo: R$ {custo}")
mostrar_texto(f"Lucro: R$ {lucro}")
mostrar_texto(f"Margem de Lucro: {margem_lucro:.2%}")

mostrar_texto("")
mostrar_texto("E-mail em maiúsculo:")
mostrar_texto(email_maiusculo)

mostrar_texto("E-mail em minúsculo:")
mostrar_texto(email_minusculo)

mostrar_texto(f"Posição do @: {posicao_arroba}")
mostrar_texto(f"Tamanho do e-mail: {tamanho_email}")
mostrar_texto(f"5º caractere do e-mail: {caractere_5}")
mostrar_texto(f"4º caractere a partir do fim: {caractere_menos4}")
mostrar_texto(f"Fatia de 4 a 10: {fatia_email}")
mostrar_texto(f"Novo e-mail (trocando gmail por hotmail): {novo_email}")
mostrar_texto(f"Servidor do e-mail: {servidor}")

mostrar_texto("")
mostrar_texto(f"Nome original: {nome}")
mostrar_texto(f"Nome capitalizado: {nome_cap}")
mostrar_texto(f"Nome com título: {nome_title}")
mostrar_texto(f"Primeiro nome: {primeiro_nome}")
mostrar_texto(f"Sobrenome: {sobrenome}")

# Executar a janela
janela.mainloop()
