# ============================================
# FICHA DE CADASTRO DO DESENVOLVEDOR
# ============================================

# Coleta dos dados do usuário
nome = input("Digite seu nome completo: Leticia Castro")


idade = int(input("Digite sua idade: 17"))
ano_inicio = int(input("Ano em que começou a estudar programação: 2025"))
linguagem = input("Linguagem de programação favorita: python ")
nota = float(input("Nota de satisfação com o curso (0 a 10): 10"))

# Processamento dos dados
anos_estudando = 2026 - ano_inicio

# Saída formatada
print("\n============================================")
print("         FICHA DO DESENVOLVEDOR")
print("============================================")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Anos estudando: {anos_estudando} ano(s)")
print(f"Linguagem fav.: {linguagem}")
print(f"Nota de satisfação: {nota}")
print("============================================")