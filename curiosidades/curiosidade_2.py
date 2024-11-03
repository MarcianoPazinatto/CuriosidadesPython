# Exemplo com while
tentativas = 3
numero_secreto = 42

while tentativas > 0:
    chute = int(input("Adivinhe o número: "))
    
    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    else:
        print("❌ Errado. Tente novamente.")
        
    tentativas -= 1
else:
    print("⏳ Suas tentativas acabaram! O número secreto era:", numero_secreto)

# Exemplo com for
numeros = [1, 2, 3, 4, 5]
procurado = 7

for numero in numeros:
    if numero == procurado:
        print(f"{procurado} encontrado!")
        break
else:
    print(f"{procurado} não está na lista.")
