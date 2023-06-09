
# Programa de aprovação de empréstimo bancário para compra de uma casa

# Dados do cliente que deseja financiar
renda_anual = float(input("Digite sua renda anual: "))
pontuacao_credito = int(input("Digite sua pontuação de crédito: "))

# ritérios para aprovação
renda_minima = 30000.0
pontuacao_minima = 700

# Verificar dados e dar a resposta
if renda_anual >= renda_minima and pontuacao_credito >= pontuacao_minima:
    print("Parabéns! Você é elegível para um empréstimo bancário.")
else:
    print("Desculpe, você não atende aos critérios para um empréstimo bancário.")