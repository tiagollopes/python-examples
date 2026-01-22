# =========================================================
# Estruturas condicionais em Python
# =========================================================
# Este script demonstra:
# - if
# - elif
# - else
# - operadores relacionais e lógicos
# - if ternário
# =========================================================

# Variáveis de exemplo
age = 20
salary = 4500.00
is_student = True
has_ticket = False


# ---------------------------------------------------------
# if simples
# ---------------------------------------------------------
if age >= 18:
    print("Pessoa maior de idade")


# ---------------------------------------------------------
# if / else
# ---------------------------------------------------------
if age < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


# ---------------------------------------------------------
# if / elif / else
# ---------------------------------------------------------
if age < 13:
    print("Criança")
elif age < 18:
    print("Adolescente")
elif age < 60:
    print("Adulto")
else:
    print("Idoso")


# ---------------------------------------------------------
# if com operadores lógicos
# ---------------------------------------------------------
if age >= 18 and has_ticket:
    print("Pode entrar no evento")
else:
    print("Não pode entrar no evento")


if is_student or age < 18:
    print("Tem direito a desconto")
else:
    print("Não tem desconto")


if not has_ticket:
    print("Usuário não possui ingresso")


# ---------------------------------------------------------
# Condições combinadas
# ---------------------------------------------------------
if (age >= 18 and has_ticket) or is_student:
    print("Acesso liberado")
else:
    print("Acesso negado")


# ---------------------------------------------------------
# if ternário (condicional em uma linha)
# ---------------------------------------------------------
status = "aprovado" if salary >= 4000 else "reprovado"
print(f"Status financeiro: {status}")
