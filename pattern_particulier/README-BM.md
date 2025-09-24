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

Après l'analyse des différents types d'algorithmes existants, j'ai choisi d'implémenter l'algorithme de Boyer-Moore, dont l'efficacité croît avec la taille du motif recherché. 

Principe : En parcourant le texte de gauche à droite, il s'agit de comparer les caractères du motif avec les caractères du texte en partant de la fin du motif (et non l'inverse).

Ainsi, tant que les caractères comparés sont similaires, on continue de les comparer, du dernier au premier caractère du motif. 
Dès que les caractères diffèrent, on calcule le décalage à opérer pour décaler le motif vers la droite du texte. 
    
Calcul du décalage : 
 1. Pour calculer le décalage, il faut d'abord créer un tableau qui répertorie pour chaque caractère du motif recherché son indice le plus à droite. 
    
    Par exemple, dans le motif "carla", la table serait la suivante : {"c": 0, "a": 4, "r" : 2, "l" : 3}
    -> L'algorithme de Boyer-Moore effectue un pré-traitement sur le motif pour optimiser la recherche en réduisant considérablement le nombre de comparaison grâce à ce tableau. 

 2. Ensuite, il s'agit de calculer le décalage 
    Si le caractère du texte pour lequel la comparaison a echoué figure dans le tableau de caractères du motif, alors : 
        décalage = indice du caractère du motif courant - indice du tableau 
    
    Sinon : 
        décalage = indice du caractère du motif courant + 1 


3. Évaluer la solution
Correction : Les résultats sont corrects, l'algorithme fonctionne avec une multitutes de données entrées différentes et la réponse formattée de la manière attendue.

Optimalité : L'algorithme de Boyer-Moore pré-traite le motif et non pas le texte  à l'inverse de certains algorithmes. Le coût d'exécution de l'algorithme de Boyer-Moore peut être sous-linéaire, c'est-à-dire qu'il n'a pas besoin de vérifier chacun des caractères du texte, mais peut au contraire sauter certains d'entre eux. En général, l'algorithme devient plus rapide lorsque la longueur de la sous-chaîne s'allonge. Cette efficacité provient du fait que, pour chaque tentative infructueuse de correspondance entre les deux chaînes (texte et sous-chaîne), il utilise les informations déduites de cet échec pour éliminer le plus grand nombre possible de positions à vérifier.

Complexité : La complexité globale du programme dépend principalement de la complexité de la recherche du motif dans le texte (O(nm)), où n est la longueur du texte et m est la longueur du motif. Les autres parties du code contribuent de manière négligeable à la complexité totale.

La complexité spatialle du programme est plutôt bien géreée car elle est principalement déterminée par la taille des motifs (surtout pour la table de saut) et est généralement relativement faible et indépendante de la taille des fichiers. La complexité temporelle, elle, est principalement déterminée par la recherche du motif dans le texte (O(nm)), où n est la longueur du texte et m est la longueur du motif. Les autres parties du code ont généralement une complexité temporelle linéaire ou constante par rapport à la taille de leurs entrées respectives.

Sensibilité aux données d'entrées :
L'algorithme prévient des risques de fichier manquant, vide ou corrompu.

