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

# Inserindo o texto que será cifrado
texto_cifrado = input("\nDigite o texto cifrado que deseja decifrar: ")
# Inserindo a palavra-palavra-chave da cifra de Vigenére
palavra_chave = input("Digite a palavra-chave: ")

# Retira os caracteres especiais ou letras com acento do texto claro e da palavra-chave
texto_cifrado = normalize("NFKD", texto_cifrado).encode("ASCII", "ignore").decode("ASCII")
palavra_chave = normalize("NFKD", palavra_chave).encode("ASCII", "ignore").decode("ASCII")

# Transforma o texto cifrado e a palavra-chave em letras maiúsculas
texto_cifrado = "".join(texto_cifrado.split())
texto_cifrado = texto_cifrado.upper()
palavra_chave = "".join(palavra_chave.split())
palavra_chave = palavra_chave.upper()

# Imprime na tela o texto cifrado
print("Texto Cifrado:\t\t", texto_cifrado)

# Decodifica o texto cifrado usando a função inversa da Cifra de Vigenère
texto_decifrado = decoder_vigerene(texto_cifrado, palavra_chave)
print("Texto Decifrado:\t\t", texto_decifrado)
