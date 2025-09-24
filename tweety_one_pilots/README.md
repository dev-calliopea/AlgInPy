Résumé : Le but est d'analyser des tweets postés sur une période donnée, et de les traiter afin d'extraire les hashtags qui reviennent le plus fréquemment.

Input -> - Un json contenant les données des tweets
         - Une période sous forme de deux timestamps

Output ->- Un tableau contenant les tweets avec le poucentage d'apparition recquis, du plus cité au moins cité.

Réfléxion : J'ai d'abord cherché si des algorithme liés au problème existaient, j'ai trouvé des articles sur l'algorithme d'analyse de frequence de mot.
Ensuite j'ai posé sur papier les différentes tâches a réaliser selon moi : 
    - Ouvrir et parcourir le Json
    - Identifier les hashtags
    - Compter les hashtags
    - Préparer le tableau de sortie
    - Diviser en plusieurs fonctions

J'ai ensuite réalisé un premier pseudo code sur papier, le voici : 

    Ouvrir le fichier JSON de données de tweets.

    Initialiser une liste vide pour stocker les hashtags.

    Pour chaque tweet dans le fichier JSON :
        * Extraire les hashtags du tweet.
        * Ajouter les hashtags à la liste des hashtags.

    Compter le nombre d'occurrences de chaque hashtag dans la liste.

    Trouver les hashtags les plus fréquents en sélectionnant ceux avec le plus grand nombre d'occurrences.

    Afficher la liste des hashtags les plus fréquents.

J'ai ensuite cherché si Python posséde un moyen de compter les occurences efficacement (librairie, classe ..etc), j'ai trouvé la classe 'Counter'.
J'ai implémenté une version 1 : 
        ;; import json
        ;; from collections import Counter

        ;; with open('data.json', 'r') as file:
        ;;     data = json.load(file)

        ;; hashtags = []

        ;; for tweet in data['tweets']:
        ;;     hashtags.extend(tweet['hashtags'])

        ;; hashtags_occurrences = Counter(hashtags)

        ;; most_common_hashtags = hashtags_occurrences.most_common(10)

        ;; for hashtag, count in most_common_hashtags:
        ;;     print(f"Hashtag: {hashtag}, Occurrences: {count}")

J'avais involontairement omis de m'occuper du pourcentage requis. 
J'ai donc travailler sur la formule qui permet de mettre dans la liste de sortie seulement les tweets avec le pourcentage d'apparition necessaire.
Voici le pseudo code final fruit de cette réfléxion : 

    Pour chaque hashtag et son compteur dans le dictionnaire de compteur_hashtags :
        Si (nombre_d'occurrences_du_hashtag / nombre_total_de_hashtags) * 100 est supérieur ou égal au pourcentage minimum requis :
            Ajouter le hashtag à la liste des hashtags_fréquents.

J'ai commencé à travailler sur la version 2 que je vous présente actullement avec les éléments cités ci dessus.
J'ai diviser mon code en deux fonctions distinctes : 
    - Une fonction qui est appellée dans la fonction principale. Elle sert a extraire et a retourner les hashtags les plus utilisés.
    - Une fonction principale pour ouvrir le fichier Json et le passer en argument de la fonction d'extraction pour afficher les résultats
Pour finir j'ai implémenté la gestion de "péridode donnée" en ajoutant deux paramétres a mes fonctions (début et fin de période), la période rstreint la sortie des hashtags fréquents.

Calcul de complexité de l'algorithme : 

tweets = nombre total de tweets
hashtags_par_tweet = nombre moyen de hashtags par tweet
hashtags_total = nombre total de hashtags
hashtags_frequents = nombre de hashtags fréquents extraits

O(tweets × hashtags_par_tweet + hashtags_total + hashtags_frequents²)
