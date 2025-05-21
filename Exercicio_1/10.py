'''Crie uma função que receba um número como argumento e retorne o quadrado desse número. Depois, chame essa função passando um número digitado pelo usuário.'''

# Define a função que retorna o quadrado do número
def quadrado(numero):
    return numero ** 2

# Solicita um número ao usuário
numero_usuario = float(input("Digite um número: "))

# Chama a função e exibe o resultado
resultado = quadrado(numero_usuario)
print(f"O quadrado de {numero_usuario} é {resultado}.")