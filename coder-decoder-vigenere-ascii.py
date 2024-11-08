# João Davi
# Computer Systems Security
# UFRGS

# ====================== IMPORTS ======================
import os
from unicodedata import normalize

# ====================== FUNÇÕES AUXILIARES ======================

# Função auxiliar para expandir a palavra-chave até o tamanho do texto
def expandir_palavra_chave(texto, palavra_chave):
    # Inicializa a variável (como string) que será usada para a palavra-chave expandida
    palavra_chave_expandida = ""
    # Índice para acompanhar a posição atual na palavra-chave
    indice_palavra_chave = 0
    
    # Loop para repetir a palavra-chave, até que ela tenha o mesmo tamanho do texto
    for _ in range(len(texto)):
        # Adiciona a letra atual da palavra-chave na palavra-chave expandida
        palavra_chave_expandida += palavra_chave[indice_palavra_chave]
        # Incrementa o índice da palavra-chave e reinicia ao início dela, se necessário
        indice_palavra_chave = (indice_palavra_chave + 1) % len(palavra_chave)
        
    return palavra_chave_expandida

# ====================== FUNÇÕES PRINCIPAIS ======================

# Função principal que codifica o texto claro usando a Cifra de Vigenère
def coder_vigerene(texto_claro, palavra_chave):
    # Inicializa uma variável (como string) para armazenar o texto cifrado
    texto_cifrado = ""
    
    # Expande a palavra-chave até que ela tenha o mesmo comprimento que o texto
    palavra_chave_repetida = expandir_palavra_chave(texto_claro, palavra_chave)
    
    # Loop que percorre cada caractere do texto claro
    for i in range(len(texto_claro)):
        # ord(): função do Python que pega o valor ASCII da letra e subtrai o valor ASCII de "A" para obter um índice entre 0 e 25 (26 letras do alfabeto regular)
        indice_texto = ord(texto_claro[i]) - ord("A")
        indice_palavra_chave = ord(palavra_chave_repetida[i]) - ord("A")
        
        # Cifra o texto aplicando o índice da palavra-chave, e usa o mód 26 (índice entre 0 e 25))
        indice_cifrado = (indice_texto + indice_palavra_chave) % 26
        # chr(): função do Python que converte o índice numérico de volta para uma letra maiúscula
        letra_cifrada = chr(indice_cifrado + ord("A"))
        
        # Adiciona a letra cifrada ao texto cifrado
        texto_cifrado += letra_cifrada
        
    return texto_cifrado

# Função para decodificar uma mensagem cifrada usando a Cifra de Vigenère
def decoder_vigerene(texto_cifrado, palavra_chave):
    # Inicializa uma variável (como string) para armazenar o texto decifrado
    texto_decifrado = ""
    
    # Expande a palavra-chave para que tenha o mesmo comprimento que o texto cifrado
    palavra_chave_repetida = expandir_palavra_chave(texto_cifrado, palavra_chave)
    
    # Loop que percorre cada caractere do texto cifrado
    for i in range(len(texto_cifrado)):
        # Converte a letra em seu índice ASCII, subtraindo o índice ASCII da palavra-chave para "reverter" a cifra e obter a palavra original
        indice_texto = ord(texto_cifrado[i]) - ord("A")
        indice_palavra_chave = ord(palavra_chave_repetida[i]) - ord("A")
        
        # Decifra o texto cifrado aplicando a subtração e usa o mód 26 (índice entre 0 e 25)
        indice_decifrado = (indice_texto - indice_palavra_chave + 26) % 26
        letra_decifrada = chr(indice_decifrado + ord("A"))
        
        # Adiciona a letra decifrada ao texto decifrado
        texto_decifrado += letra_decifrada
        
    return texto_decifrado

# Limpando a tela para que seja realizada a cifragem e a decifragem da Cifra de Vigenère
os.system("cls" if os.name == "nt" else "clear")

# Loop para que seja realizada mais de uma requisição de cifragem no código, caso desejado
loop = True
while(loop):
    # Inserindo o texto que será cifrado
    texto_claro = input("\nDigite o texto que deseja cifrar: ")
    # Inserindo a palavra-palavra-chave da cifra de Vigenére
    palavra_chave = input("Digite a palavra-chave (que seja menor que o texto): ")

    # Retira os caracteres especiais ou letras com acento do texto claro e da palavra-chave
    texto_claro = normalize("NFKD", texto_claro).encode("ASCII", "ignore").decode("ASCII")
    palavra_chave = normalize("NFKD", palavra_chave).encode("ASCII", "ignore").decode("ASCII")

    # Transforma o texto claro e a palavra-chave em letras maiúsculas
    texto_claro = texto_claro.upper()
    palavra_chave = palavra_chave.upper()

    # Imprime na tela o texto claro
    print("Texto claro:\t\t", texto_claro)

    # Codifica o texto claro usando a função de Cifra de Vigenère
    texto_cifrado = coder_vigerene(texto_claro, palavra_chave)
    print("Texto Cifrado:\t\t", texto_cifrado)

    # Decodifica o texto cifrado usando a função inversa da Cifra de Vigenère
    texto_decifrado = decoder_vigerene(texto_cifrado, palavra_chave)
    print("Texto Decifrado:\t\t", texto_decifrado)

    # Loop para verificar se deseja codificar outra palavra usando Cifra de Vigenère
    loop = input("Continuar (s/n)? ").lower() == "s"

# Encerra o código
print("Código encerrado!")