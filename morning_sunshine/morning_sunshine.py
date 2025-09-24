import json
import math
import sys

def calculate_profit(data):
    total_profit = 0
    max_height = 0
    
    # Parcours des données JSON du dernier au premier élément
    for building in data[::-1]:
        height = building["height"]
        floor_layout = building["floor_layout"]
        
        # Calcul de la différence de hauteur par rapport au plus haut bâtiment déjà parcouru
        difference = max(0, height - max_height)
            
        # Calcul du profit pour le bâtiment actuel
        for floor in floor_layout:
            if "E" in floor["orientations"]:
                monthly_rent = floor["monthly_rent"]
                total_profit += math.ceil(monthly_rent * 0.05 )* difference * 12
        
        # Mettre à jour la hauteur maximale des bâtiments déjà parcourus
        max_height = max(max_height, height)
    
    return total_profit

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 morning_sunshine.py 'json_data'")
        sys.exit(1)

    # Charger les données JSON directement depuis l'argument
    json_data = sys.argv[1]

    try:
        # Charger les données JSON
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la lecture des données JSON : {e}")
        sys.exit(1)

    # Calculer le profit
    profit = calculate_profit(data)

    # Afficher le résultat
    print(json.dumps(profit))
