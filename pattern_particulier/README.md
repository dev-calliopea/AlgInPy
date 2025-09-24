1. Analyse du problème : 
Résumé : Il s'agit de rechercher des chaînes de caractères précises dans un ou plusieurs fichiers textes. 

Input : Les chaînes de caractères à rechercher et les fichiers dans lesquels les rechecher sont passés en arguments du programme. Les motifs sont préfixés de l'option -e. Les chaînes de caractères à rechercher sont de type string et les fichiers sont au format texte (.txt) 

Output : Le résultat doit être affiché sur la sortie standard du terminal et doit être au format JSON. Le tableau d'objets représentant les occurences des motifs trouvés doit être de la forme suivante : [{"file": <filename>, "pattern": <pattern>, "offset": <index>}]. L'index représente la position du premier caractère de la chaîne trouvé dans le fichier texte. 

Contexte : Trouver une chaîne de caractère dans un texte. 

L'analyse du contexte du problème nous permet de comprendre que : 
- Il faut ouvrir et lire les fichiers textes 
- Prévenir d'arguments manquants, vides ou corrompus
- Retrouver une chaîne de caractère dans un texte  : rechercher la méthode la plus optimale pour retrouver un motif dans un texte 
- Récupérer la position de la chaîne de caractère trouvé dans le texte 
- Formatter la réponse 


2. Résolution du problème :
Une fois le problème analysé, j'ai recherché la ou les méthodes les plus optimales pour retrouver un motif dans un texte. 
Grâce à mes recherches, j'ai compris qu'il s'agissait d'algorithmes de recherche de sous-chaîne dont l'objectif est trouver une chaîne de caractère dans un texte. 

Solution intermédiaire : 
Après l'analyse des différents types d'algorithmes existants, j'ai choisi d'implémenter l'algorithme de Boyer-Moore, dont l'efficacité croît avec la taille du motif recherché. Après une erreur moulinette m'indiquant une défaillance de performance, j'ai dû faire davantage de recherches et j'ai finalement choisi l'implémentation de l'algorithme de Knuth-Morris-Pratt.

Principe : 
L'idée de départ de cet algorithme est d’éviter les comparaisons inutiles. Pour cela, l'algoritmhe propose un pré-traitement du motif avec une fonction annexe qui recherche le plus long préfixe du motif qui soit aussi un suffixe de ce motif. 

Dans ce contexte : 
Un préfixe d’un motif M est un motif u, différent de M, qui est un début de M. Par exemple, ’mo’ et ’m’ sont des préfixes de ’mot’, mais ’o’ n’est pas un préfixe de ’mot’ .
Un suffixe d’un motif M est un motif u, différent de M, qui est une fin de M. Par exemple, ’ot’ et ’t’ sont des suffixes de ’mot’, mais ’mot’ n’est pas un suffixe de ’mot’.

Une fois compris l'implémentation de la fonction annexe et de celle qui recherche le motif dans la texte grâce à la table de préfixe, il a fallut adapter l'algorithme pour s'adapter aux contraintes de l'exercice (ce qui avait déjà été fait à l'itération 1).


3. Évaluer la solution
Correction : Les résultats sont corrects, l'algorithme fonctionne avec une multitutes de données entrées différentes et la réponse formattée de la manière attendue.

Optimalité : L'algorithme KMP évite de recomparer des parties du texte qui ont déjà été examinées en utilisant la table de préfixe précalculée. Il utilise cette information pour sauter des positions dans le texte lorsqu'une correspondance partielle est trouvée, ce qui réduit considérablement le nombre total de comparaisons nécessaires.

Complexité temporelle : L'algorithme KMP a une complexité temporelle de O(n + m), où n est la longueur du texte et m est la longueur du motif. Cela signifie que le temps nécessaire pour rechercher un motif dans un texte est proportionnel à la somme des longueurs du texte et du motif, ce qui est très efficace, surtout lorsque le motif est beaucoup plus court que le texte.

Complexité spatialle : L'algorithme KMP est relativement simple car elle dépend principalement de la taille du motif et de la taille de la table de préfixe.
