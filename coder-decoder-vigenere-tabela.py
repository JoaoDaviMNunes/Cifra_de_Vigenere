# João Davi
# Computer Systems Security
# UFRGS

# ====================== IMPORTS ======================
import os
from unicodedata import normalize

# ====================== FUNÇÕES AUXILIARES ======================
def cria_tabela_vigenere(alfabeto):
    # Inicializa a matriz para que carrega matriz da Cifra de Vigenère
    tabela_vigenere = [["" for _ in range(len(alfabeto))] for _ in range(len(alfabeto))]

    # Loop para criar a tabela contendo as letras, organizadas de acordo com a cifra de Vigenère aponta
    for i in range(len(alfabeto)):
        # A linha da tabela receberá o estado atual da lista do alfabeto
        tabela_vigenere[i] = alfabeto
        # O alfabeto recebe um shift (deslocamento) à esquerda
        alfabeto = alfabeto[1:] + [alfabeto[0]]

    return tabela_vigenere

# Função auxiliar para expandir a palavra-chave até o tamanho do texto_claro
def expandir_palavra_chave(texto_claro, palavra_chave):
    # Inicializa a variável (como string) que será usada para a palavra-chave expandida
    palavra_chave_expandida = ""
    # Índice para acompanhar a posição atual na palavra-chave
    indice_palavra_chave = 0
    
    # Loop para repetir a palavra-chave, até que ela tenha o mesmo tamanho do texto_claro
    for _ in range(len(texto_claro)):
        # Adiciona a letra atual da palavra-chave na palavra-chave expandida
        palavra_chave_expandida += palavra_chave[indice_palavra_chave]
        # Incrementa o índice da palavra-chave e reinicia ao início dela, se necessário
        indice_palavra_chave = (indice_palavra_chave + 1) % len(palavra_chave)
        
    return palavra_chave_expandida

# ====================== FUNÇÕES PRINCIPAIS ======================

# Função principal que codifica o texto claro usando a Cifra de Vigenère
def coder_vigerene(texto_claro, palavra_chave, tabela_vigenere):
    # Inicializa uma variável (como string) para armazenar o texto cifrado
    texto_cifrado = ["" for _ in range(len(texto_claro))]
   
    # Expande a palavra-chave até que ela tenha o mesmo comprimento que o texto claro
    palavra_chave_repetida = expandir_palavra_chave(texto_claro, palavra_chave)

    # CODIFICAR AQUI
    for i in range(len(texto_claro)):
        # Função para achar a posição da letra do texto claro no alfabeto
        linha_texto = alfabeto.index(texto_claro[i])
        # Função para achar a posição da letra da palavra-chave no alfabeto
        coluna_palavra_chave = alfabeto.index(palavra_chave_repetida[i])
        # Adiciona a letra cifrada ao texto cifrado
        texto_cifrado[i] = tabela_vigenere[linha_texto][coluna_palavra_chave]
    
    texto_cifrado_final = "".join(texto_cifrado)
    return texto_cifrado_final

# Função para decodificar uma mensagem cifrada usando a Cifra de Vigenère
def decoder_vigerene(texto_cifrado, palavra_chave, tabela_vigenere):
    # Inicializa uma variável (como string) para armazenar o texto decifrado
    texto_decifrado = ["" for _ in range(len(texto_cifrado))]

    # Expande a palavra-chave até que ela tenha o mesmo comprimento que o texto cifrado
    palavra_chave_repetida = expandir_palavra_chave(texto_cifrado, palavra_chave)
    
    for i in range(len(texto_cifrado)):
        indice_palavra_chave = alfabeto.index(palavra_chave_repetida[i])
        indice_tabela_vigenere = tabela_vigenere[indice_palavra_chave].index(texto_cifrado[i])
        texto_decifrado[i] = alfabeto[indice_tabela_vigenere]
    
    texto_decifrado = "".join(texto_decifrado)
    return texto_decifrado

# MAIN

# Inicializando a variável que vai carregar os valores do alfabeto regular
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Limpando a tela para que seja realizada a cifragem e a decifragem da Cifra de Vigenère
os.system("cls" if os.name == "nt" else "clear")

# Criando tabela da Cifra de Vigenère, com base no alfabeto regular
tabela_vigenere = cria_tabela_vigenere(alfabeto)

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
    texto_cifrado = coder_vigerene(texto_claro, palavra_chave, tabela_vigenere)
    print("Texto Cifrado:\t\t", texto_cifrado)

    # Decodifica o texto cifrado usando a função inversa da Cifra de Vigenère
    texto_decifrado = decoder_vigerene(texto_cifrado, palavra_chave, tabela_vigenere)
    print("Texto Decifrado:\t\t", texto_decifrado)

    # Loop para verificar se deseja codificar outra palavra usando Cifra de Vigenère
    loop = input("Continuar (s/n)? ").lower() == "s"

# Encerra o código
print("Código encerrado!")