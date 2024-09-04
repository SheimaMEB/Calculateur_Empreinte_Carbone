"""
Module: main2.py

Description:
Ce module exécute une série d'analyses pour calculer et visualiser les émissions de CO2 annuelles d'une personne en fonction des données de consommation fournies. 
Il utilise les fonctions définies dans les modules `loading2` et `calculator` pour charger, enrichir et combiner les données, collecter les données utilisateur, 
calculer les émissions de CO2, afficher les résultats, et visualiser les émissions sous forme de graphiques.

Utilisation:
Ce module peut être exécuté directement. Il charge et enrichit les données de la base carbone, collecte les données de consommation de l'utilisateur, 
calcule les émissions de CO2, affiche les résultats, et génère des visualisations.

Fonctions:
- main(): Fonction principale qui exécute toutes les étapes de l'analyse des données, du calcul des émissions de CO2 et de la visualisation des résultats.
"""

from Carboncalc.loading2 import enrich_carbon_data, save_combined_data
from Carboncalc.calculator import collect_user_data, calculate_emissions, display_results, visualize_results

def main():
    base_sample_path = 'basecarbone_sample.csv'
    base_full_path = 'basecarbone-v17-fr.csv'
    output_path = 'basecarbone_combined.csv'
    
    # Enrichir les données
    df_combined = enrich_carbon_data(base_sample_path, base_full_path)
    
    # Sauvegarder les données combinées
    save_combined_data(df_combined, output_path)
    
    # Définir les catégories
    categories = {
        'Transports': ['Avion', 'Métro', 'RER', 'TGV', 'Voiture particulière', 'Bus'],
        'Logement': ['Fioul domestique', 'Gaz naturel', 'Electricité'],
        'Alimentation': ['Repas (végétarien)', 'Repas (moyen)', 'Viande de boeuf', 'Légumes (ou fruits)'],
        'Électronique': ['Tablette', 'Smartphone', 'Télévision', 'Ordinateur', 'Imprimante']
    }
    
    # Collecter les données de consommation de l'utilisateur
    user_data = collect_user_data(categories)
    
    # Calculer les émissions de CO2 basées sur les données de l'utilisateur
    emissions = calculate_emissions(user_data, df_combined)
    
    # Afficher les résultats
    display_results(emissions)
    
    # Visualiser les résultats
    visualize_results(emissions)

if __name__ == "__main__":
    main()
