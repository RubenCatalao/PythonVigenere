#  ________      ___    ___      ________          ________  ________   ________          _______
# |\   __  \    |\  \  /  /|    |\   __  \        |\   __  \|\   ___  \|\   ___ \        |\  ___ \
# \ \  \|\ /_   \ \  \/  / /    \ \  \|\  \       \ \  \|\  \ \  \\ \  \ \  \_|\ \       \ \   __/|
#  \ \   __  \   \ \    / /      \ \   _  _\       \ \   __  \ \  \\ \  \ \  \ \\ \       \ \  \_|/__
#   \ \  \|\  \   \/  /  /        \ \  \\  \|       \ \  \ \  \ \  \\ \  \ \  \_\\ \       \ \  \_|\ \
#    \ \_______\__/  / /           \ \__\\ _\        \ \__\ \__\ \__\\ \__\ \_______\       \ \_______\
#     \|_______|\___/ /             \|__|\|__|        \|__|\|__|\|__| \|__|\|_______|        \|_______|
#              \|___|/

#Import des modules
import re
import sys
import argparse

#import depuis argparse de RawTextHelpFormatter
from argparse import RawTextHelpFormatter

# étape de chiffrement
def encrypt(text, key):
    universe = [c for c in (chr(i) for i in range(32, 127))]
    universe_length = len(universe)
    plain_text = text.read().strip()
    key_length = len(key)
    cipher_text = []
    key_text = key

    for i, l in enumerate(plain_text):
        if l not in universe:
            cipher_text.append(l)
        else:
            text_index = universe.index(l)
            k = key_text[i % key_length]
            key_index = universe.index(k)
            code = universe[(text_index + key_index) % universe_length]
            cipher_text.append(code)

    for i in re.finditer('\n', plain_text):
        cipher_text[i.start()] = '\n'

    return ''.join(cipher_text)

#étape de déchifremment
def decrypt(text, key):
    universe = [c for c in (chr(i) for i in range(32, 127))]
    universe_length = len(universe)
    plain_text = text.read().strip()
    key_length = len(key)
    cipher_text = []
    key_text = key

    for i, l in enumerate(plain_text):
        if l not in universe:
            cipher_text.append(l)
        else:
            text_index = universe.index(l)
            k = key_text[i % key_length]
            key_index = universe.index(k)
            code = universe[(text_index - key_index) % universe_length]
            cipher_text.append(code)

    for i in re.finditer('\n', plain_text):
        cipher_text[i.start()] = '\n'

    return ''.join(cipher_text)


def main():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description='Chiffrer ou déchifrer un text Vigenère',
                                     epilog='''
Et c'est comme ça qu'on exécute ce script. 
Vous avez plusieurs choix pour exécuter ce programme,
si vous voulez lire depuis STDIN ou depuis FILE et si vous voulez écrire sur STDOUT
ou dans un FICHIER. Ici je vais vous montrer quelques exemples, comment utiliser correctement ce Script. 
Quand vous voulez décrypter un texte chiffré, vous pouvez exécuter l'exemple suivant :

Ceci décryptera et écrira le texte chiffré sur STDOUT et lira le texte en clair sur STDIN :

python main.py -d -k <key> -o -i <infile>

Ceci va crypter et écrire le texte chiffré sur STDOUT et lire le texte en clair sur FILE :

python main.py -e -k <key> -o - -i <infile>

Ceci va décrypter et écrire le texte chiffré dans le fichier et lire le texte en clair dans le fichier:

python main.py -d -k <key> -o <outfile> -i <infile>

                                     ''')


    parser.add_argument('-d, --decrypt', dest='decrypt', action='store_true',
                        help='pour décrypter le texte chiffré donné')
    parser.add_argument('-c, --crypt', dest='encrypt', action='store_true',
                        help='pour crypter le texte brut donné')
    parser.add_argument('-k, --key', required=True, dest='key',
                        help='définir la clé comme argument, ceci est requis')
    parser.add_argument('-i, --in', metavar='INPUT', nargs='?', dest='input', type=argparse.FileType('r'),
                        default=sys.stdin, help='chaîne de caractères depuis stdin ou depuis un fichier')
    parser.add_argument('-o, --out',  metavar='OUTPUT', nargs='?', dest='output', type=argparse.FileType('w'),
                        default=sys.stdout, help='résultat par défaut stdout ou spécifier un fichier')

    args = parser.parse_args()

    if args.encrypt:
        value = encrypt(args.input, args.key)
        args.output.write(value)
    elif args.decrypt:
        value = decrypt(args.input, args.key)
        args.output.write(value)


if __name__ == '__main__':
    main()




