Pour pouvoir utiliser le script 
Vous avez plusieurs choix pour exécuter ce Script,
si vous voulez lire depuis STDIN ou depuis FILE et si vous voulez écrire sur STDOUT
ou dans un FICHIER. Ici je vais vous montrer quelques exemples, comment utiliser correctement ce Script. 
Quand vous voulez décrypter un texte chiffré, vous pouvez exécuter l'exemple suivant :

Ceci décryptera et écrira le texte chiffré sur STDOUT et lira le texte en clair sur STDIN :

python main.py -d -k <key> -o -i <infile>

Ceci va crypter et écrire le texte chiffré sur STDOUT et lire le texte en clair sur FILE :

python main.py -e -k <key> -o - -i <infile>

Ceci va décrypter et écrire le texte chiffré dans le fichier et lire le texte en clair dans le fichier:

python main.py -d -k <key> -o <outfile> -i <infile>
