import argparse
import os
import json
import time

# Création de la table de saut pour déterminer le décalage à appliquer lorsqu'une mauvaise correspondance est trouvée entre le motif et le texte 
# @param string : le motif à recherche dans le texte 
# @return dictionnary : un dictionnaire avec pour clé les caractères du motif et pour valeur leurs indices 
# ! Les caractères du motif n'apparaissent qu'une seule fois car on cherche à connaître leur indice le plus à droite dans le motif 
def create_boyer_moore_table(pattern):
    table = {}

    # Parcourt du motif en partant de la fin jusqu'au début en décrémentant de 1 (pour obtenir la position la plus à droite pour chaque caractère du motif)
    for i in range(len(pattern) - 1, -1, -1):
        # A chaque iteration, la variable key vaut le caractère du motif 
        key = pattern[i]

        # Si le caractère du motif n'est pas encore présent dans le dictionnaire
        if key not in table:
            # Ajout du caractère dans le dictionnaire : le caractère du motif pour clé, l'indice du caractère pour valeur 
            table[key] = i

    return table


# Calcul du décalage à opérer lorsqu'une mauvaise correspondance est trouvée 
# @param dictionnary : pattern_dictionnary > la table de saut du motif
# @param int : pattern_index > indice du motif 
# @param string : text_character > caractère du texte pour lequel la comparaison a échoué
# @return int : le décalage à opérer 
def calculate_offset(pattern_dictionnary, pattern_index, text_character):
    # Si le caractère du texte pour lequel la comparaison a échoué est une clé de la table de saut du motif 
    if text_character in pattern_dictionnary.keys():
        # Retourne le décalage approprié 
        return pattern_index - pattern_dictionnary[text_character]
    
    # Sinon
    else:
        # Retourne le décalage approprié : on décale le motif d'un rang vers la droite du texte 
        return pattern_index + 1


def is_file_valid(filePath):
    # Check if file exists 
        if not os.path.exists(filePath):
            print(f"Le fichier {filePath} est manquant.")
            return False

        # with open(filePath, 'r') as file:
        #     data = file.read()

        #     # Check if empty 
        #     if not data:
        #         print(f"Le fichier {filePath} est vide.")
        #         return False

        return True

        
# Recherche du motif dans un texte : application de l'algorithme de Boyer-Moore 
# @param array of string : le ou les motifs recherchés
# @param arra of string : le ou les textes dans lesquels sont recherchés les motifs 
# @return array of objects : le tableau qui contient les objets des occurences trouvées 
def boyer_moore_search(patterns, file_paths, chunk_size=10000, timeout=60):
    # Initialisation de la réponse en dehors de la boucle
    response = []

    # Pour chaque motif recherché
    for pattern in patterns:
        # Pré-traitement du motif : création de sa table de saut (selon les calculs de l'algo Boyer-Moore)
        pattern_dictionary = create_boyer_moore_table(pattern)

        # Pour chaque fichier texte dans lequel rechercher le motif
        for file_path in file_paths:
            # Vérifie la validité du fichier texte 
            if not is_file_valid(file_path):
                continue  # Si le fichier n'est pas valide, on passe à la lecture du fichier suiviant

            # Ouverture du fichier en mode lecture
            with open(file_path, 'r') as file:
                # Lecture du fichier
                text = file.read()
            
            # Initialisation de l'indice du motif par rapport au texte
            i = 0
            start_time = time.time()

            # Parcourt du texte (de gauche à droite, jusqu'à la fin du texte)
            while i <= len(text) - len(pattern):
                # j vaut le dernier indice du motif
                j = len(pattern) - 1

                # Parcourt du motif en partant de la fin : tant que l'on n'a pas atteint la fin du motif et que les caractères comparés sont similaires 
                while j >= 0 and text[i + j] == pattern[j]:
                    # On continue de comparer les caractères en partant de la droite du motif : on décrémente l'indice du motif de 1
                    j -= 1

                # Si on atteint la fin du motif : le motif est présent dans le texte
                if j < 0:
                    # Ajout de l'information dans le tableau de réponses
                    response.append({"file": file_path, "pattern": pattern, "offset": i})
                    # Décalage du motif d'un rang vers la droite du texte : on incrémente l'indice du motif par rapport au texte de 1
                    i += 1

                # Sinon : les caractères comparés sont différents
                else:
                    # Calcul du décalage du motif à opérer par rapport au texte (selon l'algo Boyer-Moore)
                    offset = calculate_offset(pattern_dictionary, j, text[i + j])
                    # Décalage du motif vers la droite : on incrémente l'indice du motif par rapport au texte du décalage calculé
                    i += offset
                
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Le temps d'exécution a dépassé le délai de {timeout} secondes. Arrêt de la recherche.")
                    return response

                if i % chunk_size == 0:
                    temp_text = text[i - chunk_size:i]
                    with open("temp_chunk.txt", 'w') as temp_file:
                        temp_file.write(temp_text)

                    temp_response = boyer_moore_search([pattern], ["temp_chunk.txt"], timeout=timeout)

                    if temp_response is not None:  
                        response.extend(temp_response)
                    else:
                        return response  # Retourne une liste vide au lieu de None
         
    json_output = json.dumps(response)
    print(json_output)


def pattern_particulier():
    # Récupération des arguments passés au programme
    parser = argparse.ArgumentParser(description='search for a pattern in one or more files')
    parser.add_argument('-e', '--option_e', action='append', dest='patterns', help='e option args')
    parser.add_argument('files', type=str, nargs='+', help='filepaths')  # Utilisation de nargs='+'

    args = parser.parse_args()

    # Vérification des arguments avant de lancer le programme
    if args.patterns and args.files:
            boyer_moore_search(args.patterns, args.files)


pattern_particulier()