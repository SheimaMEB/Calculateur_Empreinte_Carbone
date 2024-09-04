"""
Module: calculator.py

Description:
Ce module fournit des fonctions pour collecter des données de consommation de l'utilisateur, calculer les émissions de CO2 
en fonction des facteurs d'émission, afficher les résultats, et visualiser les émissions sous forme de graphiques.

Utilisation:
Ce module peut être utilisé pour collecter des données de consommation, calculer les émissions de CO2, et visualiser les résultats 
en appelant les fonctions avec les paramètres appropriés. Le script peut également être exécuté directement pour tester les fonctions 
avec des données d'exemple.

Fonctions:
- collect_user_data(categories): Collecte les données de consommation de l'utilisateur pour différentes catégories et sous-catégories.
- calculate_emissions(user_data, carbon_data): Calcule les émissions de CO2 basées sur les données de consommation de l'utilisateur et les facteurs d'émission.
- display_results(emissions): Affiche les résultats des émissions de CO2 calculées.
- visualize_results(emissions): Visualise les résultats des émissions de CO2 calculées sous forme de graphique et sauvegarde l'image.

Exécution directe:
Le script peut être exécuté directement pour tester les fonctions avec des données d'exemple.
"""

import pandas as pd
import matplotlib.pyplot as plt

def collect_user_data(categories):
    """
    Collecte les données de consommation de l'utilisateur pour différentes catégories et sous-catégories.

    Paramètres :
    - categories : dict, dictionnaire contenant les catégories et sous-catégories de consommation

    Retourne :
    - dict, données de consommation de l'utilisateur
    """
    user_data = {}
    for category, subcategories in categories.items():
        print(f"\n{category} :")
        user_data[category] = {}
        for subcategory in subcategories:
            valid_input = False
            while not valid_input:
                try:
                    if subcategory == 'Avion':
                        question = f"Combien de km avez-vous parcouru en un an en avion ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory in ['Voiture particulière', 'Bus', 'Métro', 'RER', 'TGV']:
                        question = f"Combien de km avez-vous parcouru en un an en {subcategory.lower()} ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory == 'Fioul domestique':
                        question = f"Combien de Fioul consommez-vous par mois en litres ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory == 'Gaz naturel':
                        question = f"Combien de Gaz consommez-vous par mois en m3 ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory == 'Electricité':
                        question = f"Combien d’Electricité consommez-vous par mois en kWh ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory in ['Repas (végétarien)', 'Repas (moyen)']:
                        question = f"Combien mangez-vous de {subcategory.lower()} par semaine ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory == 'Viande de boeuf':
                        question = f"Combien de kg de viande de boeuf consommez-vous par mois ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory == 'Légumes (ou fruits)':
                        question = f"Combien de kg de légumes (ou fruits) consommez-vous par mois ? "
                        user_data[category][subcategory] = float(input(question))
                    elif subcategory in ['Tablette', 'Smartphone', 'Télévision', 'Ordinateur', 'Imprimante']:
                        question = f"Combien de {subcategory.lower()} possédez-vous chez vous ? "
                        user_data[category][subcategory] = float(input(question))
                    valid_input = True
                except ValueError:
                    print("Veuillez entrer une valeur correcte.")
    
    return user_data

def calculate_emissions(user_data, carbon_data):
    """
    Calcule les émissions de CO2 basées sur les données de consommation de l'utilisateur et les facteurs d'émission.

    Paramètres :
    - user_data : dict, données de consommation de l'utilisateur
    - carbon_data : DataFrame, données de la base carbone

    Retourne :
    - dict, émissions de CO2 par catégorie et sous-catégorie
    """
    emissions = {}
    for category, subcategories in user_data.items():
        emissions[category] = {}
        for subcategory, consumption in subcategories.items():
            if subcategory in carbon_data['Nom base français'].values:
                unit = carbon_data.loc[carbon_data['Nom base français'] == subcategory, 'Unité français'].values[0]
                factor = carbon_data.loc[carbon_data['Nom base français'] == subcategory, 'Total poste non décomposé'].values[0]
                
                # Conversion de la consommation en annuelle
                if subcategory in ['Avion', 'Voiture particulière', 'Bus', 'Métro', 'RER', 'TGV']:
                    annual_consumption = consumption  # déjà en valeurs annuelles
                elif subcategory in ['Fioul domestique', 'Gaz naturel', 'Electricité', 'Viande de boeuf', 'Légumes (ou fruits)']:
                    annual_consumption = consumption * 12  # par mois -> annuel
                elif subcategory in ['Repas (végétarien)', 'Repas (moyen)']:
                    average_weight_per_serving = 0.2  # Exemple : moyenne de 200g par repas
                    annual_consumption = consumption * 52 * average_weight_per_serving  # fois par semaine -> annuel
                elif subcategory in ['Tablette', 'Smartphone', 'Télévision', 'Ordinateur', 'Imprimante']:
                    annual_consumption = consumption  # nombre total d'appareils
                else:
                    annual_consumption = consumption  # usage annuel

                emissions[category][subcategory] = annual_consumption * factor
            else:
                emissions[category][subcategory] = 0  # Valeur par défaut

    return emissions

def display_results(emissions):
    """
    Affiche les résultats des émissions de CO2 calculées.

    Paramètres :
    - emissions : dict, émissions de CO2 par catégorie et sous-catégorie
    """
    print("\n--- Résultats des émissions de CO2 ---")
    total_emissions = 0
    for category, subcategories in emissions.items():
        category_emissions = sum(subcategories.values())
        total_emissions += category_emissions
        print(f"{category} : {category_emissions:.2f} kg CO2")
        for subcategory, emission in subcategories.items():
            print(f"  {subcategory} : {emission:.2f} kg CO2")
    print(f"\nTotal des émissions de CO2 : {total_emissions:.2f} kg CO2")
    
    # Comparer avec la moyenne
    moyenne_annuelle = 10000  # en kg de CO2
    if total_emissions <= moyenne_annuelle:
        print("Bravo ! Vous êtes en dessous de la moyenne, continuez ainsi.")
    else:
        print("Attention ! Vous dépassez la moyenne, vous devriez réduire votre consommation.")

def visualize_results(emissions, file_path='emissions_par_categorie_ameliore.png'):
    """
    Visualise les résultats des émissions de CO2 calculées sous forme de graphique et sauvegarde l'image.

    Paramètres :
    - emissions : dict, émissions de CO2 par catégorie et sous-catégorie
    - file_path : str, chemin vers le fichier pour sauvegarder l'image
    """
    categories = list(emissions.keys())
    total_emissions = [sum(subcategories.values()) for subcategories in emissions.values()]

    # Définir une liste de couleurs pour les différentes catégories
    colors = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'violet']

    plt.figure(figsize=(8, 7))  # Réduire la taille du graphique pour Jupyter
    bars = plt.bar(categories, total_emissions, color=colors[:len(categories)], edgecolor='black')
    plt.xlabel('Catégories', fontsize=14, fontweight='bold')
    plt.ylabel('Émissions de CO2 (kg)', fontsize=14, fontweight='bold')
    plt.title('Émissions de CO2 par catégorie', fontsize=16, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Ajouter les valeurs sur les barres avec un léger décalage pour éviter le chevauchement avec la grille
    for bar, emission in zip(bars, total_emissions):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 20, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(file_path, dpi=300)
    plt.show()
