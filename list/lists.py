# ===============================
# EXEMPLOS DE LISTAS EM PYTHON
# ===============================

print("=== CRIANDO UMA LISTA ===")

# Uma lista guarda vários valores em uma variável
numeros = [10, 20, 30, 40]

print(numeros)


print("\n=== ACESSANDO ITENS DA LISTA ===")

# Listas começam no índice 0
print("Primeiro número:", numeros[0])
print("Segundo número:", numeros[1])


print("\n=== ADICIONANDO ITENS NA LISTA ===")

numeros.append(50)  # adiciona no final
print(numeros)


print("\n=== REMOVENDO ITENS DA LISTA ===")

numeros.remove(20)  # remove o valor 20
print(numeros)


print("\n=== TAMANHO DA LISTA ===")

print("Quantidade de itens:", len(numeros))


print("\n=== PERCORRENDO LISTA COM FOR ===")

for numero in numeros:
    print("Número:", numero)


print("\n=== LISTA DE STRINGS ===")

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print("Fruta:", fruta)


print("\n=== VERIFICAR SE ITEM EXISTE NA LISTA ===")

if "banana" in frutas:
    print("Banana está na lista!")
else:
    print("Banana não está na lista.")


print("\n=== LISTA VAZIA E WHILE ===")

valores = []

while len(valores) < 3:
    valor = input("Digite um valor: ")
    valores.append(valor)

print("Valores digitados:", valores)
