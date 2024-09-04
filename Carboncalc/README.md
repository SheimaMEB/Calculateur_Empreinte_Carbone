# Carboncalc

## Description

`Carboncalc` est un package Python conçu pour calculer l'empreinte carbone annuelle d'une personne en fonction des données qu'elle fournit, et permet de visualiser ces résultats sur un graphique.

## Installation

Pour installer ce package, utilisez `pip` :

```bash
pip install Carboncalc/dist/Carboncalc-0.1.tar.gz


## Exemple d'utilisation 

from Carboncalc.loading2 import enrich_carbon_data, save_combined_data
from Carboncalc.calculator import collect_user_data, calculate_emissions, display_results, visualize_results

# Enrichir les données carbone
df_combined = enrich_carbon_data('path/to/basecarbone_sample.csv', 'path/to/basecarbone-v17-fr.csv')
save_combined_data(df_combined, 'path/to/output_combined.csv')

# Définir les catégories de consommation
categories = {
    'Transports': ['Avion', 'Métro', 'RER', 'TGV', 'Voiture particulière', 'Bus'],
    'Logement': ['Fioul domestique', 'Gaz naturel', 'Electricité'],
    'Alimentation': ['Repas (végétarien)', 'Repas (moyen)', 'Viande de boeuf', 'Légumes (ou fruits)'],
    'Électronique': ['Tablette', 'Smartphone', 'Télévision', 'Ordinateur', 'Imprimante']
}

# Collecter les données de consommation de l'utilisateur
user_data = collect_user_data(categories)

# Calculer les émissions de CO2
emissions = calculate_emissions(user_data, df_combined)

# Afficher les résultats
display_results(emissions)

# Visualiser les résultats
visualize_results(emissions)


## Fonctionnalités

###loading2.py

    -load_carbon_data(file_path, separator): Charge les données de la base carbone à partir dun fichier CSV.
    -enrich_carbon_data(base_sample_path, base_full_path): Enrichit les données de basecarbone_sample.csv avec des données supplémentaires de basecarbone-v17-fr.csv.
    -save_combined_data(df, output_path): Sauvegarde le DataFrame combiné dans un fichier CSV.

###calculator.py

    -collect_user_data(categories): Collecte les données de consommation de lutilisateur pour différentes catégories.
    -calculate_emissions(user_data, carbon_data): Calcule les émissions de CO2 basées sur les données de consommation de lutilisateur.
    -display_results(emissions): Affiche les résultats des émissions de CO2 calculées.
    -visualize_results(emissions): Visualise les résultats des émissions de CO2 calculées sous forme de graphique et sauvegarde limage.

###__init__.py

Le fichier __init__.py permet de traiter le dossier Carboncalc comme un package. Il importe les fonctions nécessaires des modules loading2 et calculator.

###setup.py

Le fichier setup.py est utilisé pour créer le package. Il inclut les informations nécessaires pour linstallation, telles que les dépendances et les métadonnées du package.

    
## Tests 

Pour exécuter les tests unitaires, utilisez pytest : pytest Tests/ #Commande à éxecuter sur le terminal


Sheïma MEBARKA.

