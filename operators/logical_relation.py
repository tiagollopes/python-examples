# =========================================================
# Operadores Relacionais e Lógicos em Python
# =========================================================
# Este script demonstra:
# - operadores relacionais (comparação)
# - operadores lógicos (and, or, not)
# - exemplos simples e combinados
# =========================================================

# Variáveis de exemplo
age = 20
salary = 4500.00
is_student = True
has_ticket = False


# ---------------------------------------------------------
# Operadores Relacionais
# ---------------------------------------------------------
print("=== Operadores Relacionais ===")

print(age == 20)     # igual
print(age != 18)     # diferente
print(age > 18)      # maior que
print(age < 30)      # menor que
print(age >= 21)     # maior ou igual
print(age <= 20)     # menor ou igual


# ---------------------------------------------------------
# Operadores Lógicos
# ---------------------------------------------------------
print("\n=== Operadores Lógicos ===")

# AND -> todas as condições precisam ser verdadeiras
if age >= 18 and has_ticket:
    print("Pode entrar no evento")
else:
    print("Não pode entrar no evento")


# OR -> pelo menos uma condição precisa ser verdadeira
if is_student or age < 18:
    print("Tem direito a desconto")
else:
    print("Não tem desconto")


# NOT -> inverte o valor lógico
if not has_ticket:
    print("Usuário não possui ingresso")


# ---------------------------------------------------------
# Operadores combinados (relacionais + lógicos)
# ---------------------------------------------------------
print("\n=== Operadores Combinados ===")

if (age >= 18 and has_ticket) or is_student:
    print("Acesso liberado")
else:
    print("Acesso negado")


# ---------------------------------------------------------
# Comparações com strings
# ---------------------------------------------------------
print("\n=== Comparações com Strings ===")

name = "Ana"

print(name == "Ana")       # igualdade
print(name != "Maria")    # diferença
print(name > "Abel")      # comparação alfabética


# ---------------------------------------------------------
# Comparações com números float
# ---------------------------------------------------------
print("\n=== Comparações com Float ===")

price = 19.99

if price <= 20.0:
    print("Preço acessível")
else:
    print("Preço caro")
