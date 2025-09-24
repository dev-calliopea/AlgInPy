# Groupe de bizzar_


## Analyse du Contexte :

Le problème à résoudre consiste à déterminer le profit potentiel qu'un promoteur immobilier peut réaliser en augmentant
de 5% le loyer des appartements orientés vers l'est, pour l'année à venir.

Les données sont fournies au format JSON et comprennent des informations sur la hauteur de chaque bâtiment, ainsi que
l'agencement des étages, comprenant le loyer mensuel de chaque appartement et les directions vers lesquelles ils sont
orientés.

La principale chose à garder à l'esprit est que si un bâtiment est plus court que ceux derrière lui, il pourrait bloquer
la lumière du soleil pour les étages inférieurs des bâtiments derrière lui. C'est comme être à l'arrière d'un cinéma et
ne pas pouvoir voir l'écran parce que quelqu'un de plus grand est assis devant vous.


## Résumé de l'Approche :

Dès le départ le plan était assez simple. Nous allons regarder les bâtiments un par un, mais en commençant par le
dernier de la liste et en remontant jusqu'au premier. Pour chaque bâtiment, nous allons calculer combien d'argent nous pourrions gagner en
augmentant les loyers des appartements orientés vers l'est. Nous allons aussi tenir compte du fait que les bâtiments
plus petits pourraient cacher une partie du soleil aux bâtiments plus grands derrière eux.

Nous avons donc implementer un premier algorithme qui renvoi bien la reponse attendu dans l'exercice avec les données
JSON en exemple. Mais nous nous sommes vite rendu compte qu'il faut penser plus en général et envisager
le cas où il y'a plusieurs(plus de deux) batiments dans le fichier JSON avec des tailles differentes et aligné en
desordre.
Nous avions donc rédigé une deuxieme version avec le calcul de profit de la manière suivante :

Calcul du profit:

Pour chaque bâtiment, on compare sa hauteur avec la hauteur maximale des bâtiments déjà parcourus (max_height). Si la
hauteur du bâtiment est supérieure à max_height, cela signifie qu'il peut potentiellement cacher le soleil à un bâtiment
situé derrière lui, donc on doit calculer le profit pour cet étage.
On calcule la différence entre la hauteur du bâtiment actuel et la hauteur maximale des bâtiments déjà parcourus, ce qui
représente le nombre d'étages qui peuvent potentiellement être éclairés par le soleil.
Pour chaque étage du bâtiment orienté vers l'est, on ajoute au profit total le résultat de la formule
math.ceil(monthly_rent * 0.05 * difference), où monthly_rent est le loyer mensuel de l'appartement et difference est la
différence calculée précédemment.

Mise à jour de la hauteur maximale :
La hauteur maximale des bâtiments déjà parcourus est mise à jour en comparant la hauteur actuelle du bâtiment avec la
hauteur maximale.

Multiplication par 12 :

Une fois que tous les bâtiments ont été parcourus, le profit total est multiplié par 12 pour obtenir le profit annuel
total.

Traitement des données d'entrée :

Ensuite, le script vérifie si des arguments ont été fournis en ligne de commande. Si un fichier JSON contenant les
données d'entrée est spécifié, il est chargé et passé à la fonction calculate_profit.

Affichage du résultat :

Enfin, le résultat du profit annuel total est affiché au format JSON à l'aide de json.dumps.


## Justification de la Solution :

Nous avons retenu cette solution car elle offre une approche efficace pour calculer le profit potentiel en tenant compte
des contraintes spécifiques du problème. En parcourant les bâtiments du dernier au premier, nous avons pu ajuster le
calcul du profit en fonction de la hauteur des bâtiments déjà parcourus, ce qui nous a permis de prendre en compte
l'ombre projetée par les bâtiments plus petits sur les bâtiments plus grands. Cette approche nous a semblé la plus
appropriée pour répondre au problème posé.


## Complexité Algorithmique et Performance :

La complexité algorithmique de notre solution dépend principalement de la taille du fichier JSON contenant les données
des bâtiments. En parcourant les bâtiments du dernier au premier, nous avons une complexité linéaire O(n), où n est le
nombre total de bâtiments. Le calcul du profit pour chaque bâtiment nécessite une itération sur les étages de ce
bâtiment, ce qui contribue à la complexité totale.

Pour améliorer les performances, nous pourrions envisager d'optimiser le calcul du profit en utilisant des structures de
données plus efficaces ou en parallélisant le traitement des bâtiments. Cependant, dans la plupart des cas, la solution
actuelle offre une performance satisfaisante compte tenu de la taille typique des ensembles de données immobiliers.
