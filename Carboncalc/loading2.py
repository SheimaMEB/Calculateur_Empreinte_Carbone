"""
Module: loading2.py

Description:
Ce module fournit des fonctions pour charger, enrichir et sauvegarder des données de la base carbone en utilisant Pandas. 
Il permet de combiner des données de deux fichiers CSV en incluant uniquement certaines catégories spécifiques et de sauvegarder 
le DataFrame combiné dans un nouveau fichier CSV.

Utilisation:
Ce module peut être utilisé pour charger des données de la base carbone, enrichir ces données avec des catégories spécifiques 
à partir d'un autre fichier, et sauvegarder le DataFrame combiné. Les fonctions peuvent être appelées individuellement ou le script 
peut être exécuté directement pour réaliser toutes ces étapes.

Fonctions:
- load_carbon_data(file_path, separator): Charge les données de la base carbone à partir d'un fichier CSV en spécifiant le séparateur.
- enrich_carbon_data(base_sample_path, base_full_path): Enrichit les données d'un fichier CSV avec des données supplémentaires d'un autre fichier CSV.
- save_combined_data(df, output_path): Sauvegarde le DataFrame combiné dans un fichier CSV.

Exécution directe:
Le script peut être exécuté directement pour charger, enrichir et sauvegarder les données de la base carbone.
"""

import pandas as pd

def load_carbon_data(file_path, separator):
    """
    Charge les données de la base carbone à partir d'un fichier CSV en utilisant Pandas,
    en spécifiant correctement le séparateur.

    Paramètres :
    - file_path : str, chemin vers le fichier CSV
    - separator : str, séparateur utilisé dans le fichier CSV

    Retourne :
    - DataFrame contenant les données chargées
    """
    df = pd.read_csv(file_path, sep=separator, na_values=['', ' '])
    return df

def enrich_carbon_data(base_sample_path, base_full_path):
    """
    Enrichit les données de basecarbone_sample.csv avec des données supplémentaires de basecarbone-v17-fr.csv,
    en incluant uniquement certaines catégories spécifiques.

    Paramètres :
    - base_sample_path : str, chemin vers le fichier CSV de basecarbone_sample.csv
    - base_full_path : str, chemin vers le fichier CSV de basecarbone-v17-fr.csv

    Retourne :
    - DataFrame enrichi combinant les informations des deux fichiers
    """
    df_sample = load_carbon_data(base_sample_path, separator=';')
    df_full = load_carbon_data(base_full_path, separator=',')
    
    # Catégories spécifiques à inclure de la base v17
    inclusions_v17 = [
        "Viande de boeuf", "Fromage", "Légumes (ou fruits)", "Bus", "Tablette", "Smartphone", 
        "Télévision", "Ordinateur", "Imprimante"
    ]
    
    df_v17_filtered = df_full[df_full['Nom base français'].isin(inclusions_v17)]
    
    # Colonnes à conserver
    columns_needed = [
        "Identifiant de l'élément",
        "Nom base français",
        "Unité français",
        "Total poste non décomposé",
        "Nom attribut français"
    ]
    
    df_v17_filtered = df_v17_filtered[columns_needed]
    
    # Combiner les DataFrames et supprimer les doublons en se basant sur les colonnes spécifiques
    df_combined = pd.concat([df_sample, df_v17_filtered]).drop_duplicates(subset=["Identifiant de l'élément", "Nom base français"]).reset_index(drop=True)
    
    return df_combined

def save_combined_data(df, output_path):
    """
    Sauvegarde le DataFrame combiné dans un fichier CSV.

    Paramètres :
    - df : DataFrame, le DataFrame combiné à sauvegarder
    - output_path : str, chemin vers le fichier CSV de sortie
    """
    df.to_csv(output_path, sep=';', index=False)

if __name__ == "__main__":
    # Chemins des fichiers d'entrée
    base_sample_path = 'basecarbone_sample.csv'
    base_full_path = 'basecarbone-v17-fr.csv'
    
    # Enrichir les données
    df_combined = enrich_carbon_data(base_sample_path, base_full_path)
    
    # Chemin du fichier de sortie
    output_path = 'basecarbone_combined.csv'
    
    # Sauvegarder les données combinées
    save_combined_data(df_combined, output_path)
    
    print(f"Données combinées et sauvegardées dans {output_path}")
