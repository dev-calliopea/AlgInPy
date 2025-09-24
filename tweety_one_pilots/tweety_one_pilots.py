import json
from collections import Counter

def extract_hashtags(data, start_timestamp=None, end_timestamp=None):
    '''
    Extrait les hashtags à partir des données de tweets.

    Arguments :
    data : dict - Les données de tweets au format JSON.
    start_timestamp : int - Timestamp de début de la période de temps (en secondes).
    end_timestamp : int - Timestamp de fin de la période de temps (en secondes).

    Retour :
    list - Liste des hashtags les plus fréquents.
    
    '''
    # Initialisation de la liste des hashtags
    hashtags = []

    # Parcours des tweets dans les données
    for tweet in data['tweets']:
        # Vérifie si le tweet est dans la période de temps spécifiée
        if start_timestamp and tweet['timestamp'] < start_timestamp:
            continue
        if end_timestamp and tweet['timestamp'] > end_timestamp:
            continue
        # Ajoute les hashtags du tweet à la liste des hashtags
        hashtags.extend(tweet['hashtags'])

    # Comptage des occurrences des hashtags
    hashtag_counter = Counter(hashtags)

    # Calcul du nombre total de hashtags dans les données
    total_hashtags = sum(len(tweet['hashtags']) for tweet in data['tweets'])

    # Pourcentage minimal de récurrence requis pour un hashtag
    required_percentage = data['percentage_threshold']

    # Extraction des hashtags dont la fréquence est supérieure ou égale au seuil requis
    frequent_hashtags = [tag for tag, count in hashtag_counter.items() if (count / total_hashtags) * 100 >= required_percentage]

    # Tri des hashtags par fréquence
    frequent_hashtags.sort(key=lambda x: hashtag_counter[x], reverse=True)

    return frequent_hashtags

def main(file_path, start_timestamp=None, end_timestamp=None):
    """
    Fonction principale pour l'analyse des hashtags à partir du fichier JSON.

    Arguments :
    file_path : str - Chemin du fichier JSON contenant les données de tweets.
    start_timestamp : str - Timestamp de début de la période de temps (en secondes).
    end_timestamp : str - Timestamp de fin de la période de temps (en secondes).
    """

    # Chargement des données JSON à partir du fichier
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Conversion des timestamps en entiers
    if start_timestamp is not None:
        start_timestamp = int(start_timestamp)
    if end_timestamp is not None:
        end_timestamp = int(end_timestamp)

    # Extraction des hashtags
    frequent_hashtags = extract_hashtags(data, start_timestamp, end_timestamp)

    # Affichage des hashtags les plus fréquents au format JSON
    print(json.dumps(frequent_hashtags, indent=2))

if __name__ == "__main__":
    import sys

    # Vérification des arguments en ligne de commande
    if len(sys.argv) < 2:
        sys.exit(1)
    
    # Récupération des chemins et timestamps
    file_path = sys.argv[1]
    start_timestamp = None
    end_timestamp = None
    if len(sys.argv) >= 4:
        start_timestamp = sys.argv[2]
        end_timestamp = sys.argv[3]

    # Appel de la fonction principale
    main(file_path, start_timestamp, end_timestamp)
