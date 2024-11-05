# Exemplo com while
tentativas = 3
numero_secreto = 42

while tentativas > 0:
    chute = int(input("Adivinhe o número: "))
    
    if chute == numero_secreto:
        print("\n🎉 *Parabéns! Você acertou!* 🎉\n")
        break
    else:
        print("\n❌ *Errado. Tente novamente.* ❌\n")
        
    tentativas -= 1
else:
    print("\n⏳ *Suas tentativas acabaram! O número secreto era:*", numero_secreto)

# Exemplo com for
numeros = [1, 2, 3, 4, 5]
procurado = 5

for numero in numeros:
    if numero == procurado:
        print(f"\n{procurado} *encontrado!*\n")
        break
else:
    print(f"\n{procurado} *não está na lista.*\n")
