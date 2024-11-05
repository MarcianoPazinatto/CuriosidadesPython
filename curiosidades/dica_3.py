class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Criamos duas instâncias da classe
pessoa1 = Pessoa("Ana")
pessoa2 = Pessoa("Carlos")

# Definindo um novo método que será exclusivo da instância 'pessoa1'
def saudar(self):
    return f"Olá, meu nome é {self.nome}!"

# Adicionando o método diretamente na instância 'pessoa1'
pessoa1.saudar = saudar.__get__(pessoa1)

print(pessoa1.saudar())  # Saída: Olá, meu nome é Ana!

# Se tentarmos usar 'saudar' em 'pessoa2', dá erro! 🛑
print(pessoa2.saudar())  
