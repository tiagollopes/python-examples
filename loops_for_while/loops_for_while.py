# ===============================
# EXEMPLOS DE LOOP FOR E WHILE
# ===============================

print("=== EXEMPLO DE FOR ===")

# O loop FOR é usado quando sabemos
# quantas vezes queremos repetir algo

for numero in range(1, 6):
    print("Número:", numero)

# range(1, 6) significa:
# começa em 1 e vai até 5 (o 6 não entra)


print("\n=== EXEMPLO DE FOR COM LISTA ===")

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print("Fruta:", fruta)


print("\n=== EXEMPLO DE WHILE ===")

# O loop WHILE é usado quando queremos
# repetir algo ENQUANTO uma condição for verdadeira

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador = contador + 1
    # se não aumentar o contador, o loop fica infinito


print("\n=== EXEMPLO DE WHILE COM CONDIÇÃO ===")

senha = ""

while senha != "1234":
    senha = input("Digite a senha correta: ")

print("Senha correta! Acesso liberado.")
