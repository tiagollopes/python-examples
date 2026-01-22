# =========================================================
# print com f-string em Python
# =========================================================
# f-strings permitem interpolar variáveis dentro de strings
# de forma simples, legível e moderna (Python 3.6+).
# =========================================================

# Variáveis básicas
name = "Ana"
age = 25
salary = 4500.50
is_student = True


# ---------------------------------------------------------
# Exemplo básico de f-string
# ---------------------------------------------------------
print(f"Nome: {name}")
print(f"Idade: {age}")


# ---------------------------------------------------------
# f-string com múltiplas variáveis
# ---------------------------------------------------------
print(f"{name} tem {age} anos e recebe {salary} reais.")


# ---------------------------------------------------------
# f-string com expressões
# ---------------------------------------------------------
print(f"Salário com aumento de 10%: {salary * 1.10}")


# ---------------------------------------------------------
# Formatação de números
# ---------------------------------------------------------
print(f"Salário formatado: R$ {salary:.2f}")


# ---------------------------------------------------------
# f-string com texto condicional
# ---------------------------------------------------------
status = "estudante" if is_student else "não estudante"
print(f"{name} é {status}.")


# ---------------------------------------------------------
# f-string com datas
# ---------------------------------------------------------
from datetime import date

today = date.today()
print(f"Data de hoje: {today:%d/%m/%Y}")
