#String

# title() ==> Primeiro caracter de cada palavra maiúsculo
nome = 'o auto da compadecida'
print(nome.title())

# upper() ==> Toda a frase em letras maiúsculas
nome = 'o auto da compadecida'
print(nome.upper())

# lower() ==> Toda frase em letras minúsculas
nome = 'O Auto da Compadecida'
print(nome.lower())

# Concatenação de variáveis e método title()
fist_name = "astrogildo"
last_name = "gusmão"
full_name = fist_name + ' ' + last_name
print ('Olá, ' + full_name.title() + '!')

#Quebra de linha (\n) e espaço em branco (\t)

print("Languagens:\n\tPython\n\tC\n\tJavaScript")

#REMOVER ESPAÇOS
# strip() ==> Remove espaço em branco no início e no final da string

linguagem_favorita = '   python    '
print('**'+linguagem_favorita.strip()+'**')

# rstrip() ==> Remove espaço em branco à direita string

linguagem_favorita = '   python    '
print('**'+linguagem_favorita.rstrip()+'**')

# lstrip() ==> Remove espaço em branco à esquerda string

linguagem_favorita = '   python    '
print('**'+linguagem_favorita.lstrip()+'**')

print(2 + 3)