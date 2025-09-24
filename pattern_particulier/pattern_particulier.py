import argparse 
import json 

def create_kmp_table(pattern):
    m = len(pattern)
    pi = [0] * m  # Initialise une liste de 0 de la longueur du motif recherché 
    k = 0 

    for q in range(1, m):  # Parcours des caractères du motif à partir du deuxième

        while k > 0 and pattern[k] != pattern[q]:  # Tant que k > 0 et les caractères ne correspondent pas
            k = pi[k - 1]  # Réduire k en utilisant la valeur précédente de pi

        if pattern[k] == pattern[q]:  # Si les caractères correspondent
            k += 1  # Augmenter k
        pi[q] = k  # Stocker la valeur de k dans pi[q]

    return pi 

def kmp_search(pattern, text):
    if not pattern:  
        return list(range(len(text) + 1))  # Retourne une liste d'indices pour chaque caractère dans le texte
    
    n = len(text)
    m = len(pattern)
    pi = create_kmp_table(pattern) 
    q = 0  
    matches = [] 

    for i in range(n):  # Parcours des caractères du texte
        while q > 0 and pattern[q] != text[i]:  # Tant que q > 0 et les caractères ne correspondent pas
            q = pi[q - 1]  # Réduire q en utilisant la valeur précédente de pi

        if pattern[q] == text[i]:  # Si les caractères correspondent
            q += 1  # Augmenter q

        if q == m:  # Si q atteint la longueur du motif
            matches.append(i - m + 1)  # Ajouter l'indice de début de la correspondance à la liste des correspondances
            q = pi[q - 1]  # Réinitialiser q en utilisant la valeur précédente de pi
    return matches  

def search_in_file(pattern, filename):
    with open(filename, 'r') as file:  
        text = file.read()  
        matches = kmp_search(pattern, text) 
        return [{"file": filename, "pattern": pattern, "offset": match} for match in matches] 
        
def main():
    parser = argparse.ArgumentParser(description='Search for patterns in text files using Knuth-Morris-Pratt algorithm.') 
    parser.add_argument('-e', '--option_e', action='append', dest='patterns', help='e option args') 
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='Files to search in')  
    args = parser.parse_args()  #

    results = [] 
    for pattern in args.patterns:  
        for filename in args.files:  
            results.extend(search_in_file(pattern, filename)) 

    json_output = json.dumps(results)
    print(json_output)

if __name__ == "__main__":
    main()  
