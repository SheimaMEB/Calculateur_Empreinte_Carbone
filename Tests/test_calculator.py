import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import pandas as pd
from Carboncalc.calculator import collect_user_data, calculate_emissions, display_results, visualize_results

def test_collect_user_data(monkeypatch):
    categories = {
        'Transports': ['Avion'],
        'Logement': ['Fioul domestique'],
        'Alimentation': ['Viande de boeuf'],
        'Électronique': ['Tablette']
    }

    inputs = iter(['1000', '200', '10', '1'])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    user_data = collect_user_data(categories)
    
    assert user_data['Transports']['Avion'] == 1000.0
    assert user_data['Logement']['Fioul domestique'] == 200.0
    assert user_data['Alimentation']['Viande de boeuf'] == 10.0
    assert user_data['Électronique']['Tablette'] == 1.0

def test_calculate_emissions():
    user_data = {
        'Transports': {'Avion': 1000},
        'Logement': {'Fioul domestique': 200},
        'Alimentation': {'Viande de boeuf': 10},
        'Électronique': {'Tablette': 1}
    }
    carbon_data = pd.DataFrame({
        'Nom base français': ['Avion', 'Fioul domestique', 'Viande de boeuf', 'Tablette'],
        'Unité français': ['km', 'litres', 'kg', 'unité'],
        'Total poste non décomposé': [0.2, 2.5, 15, 8]
    })

    emissions = calculate_emissions(user_data, carbon_data)
    
    assert emissions['Transports']['Avion'] == 200.0
    assert emissions['Logement']['Fioul domestique'] == 6000.0
    assert emissions['Alimentation']['Viande de boeuf'] == 1800.0
    assert emissions['Électronique']['Tablette'] == 8.0

def test_display_results(capsys):
    emissions = {
        'Transports': {'Avion': 200.0},
        'Logement': {'Fioul domestique': 6000.0},
        'Alimentation': {'Viande de boeuf': 1800.0},
        'Électronique': {'Tablette': 8.0}
    }
    
    display_results(emissions)
    
    captured = capsys.readouterr()
    assert "Total des émissions de CO2 : 8008.00 kg CO2" in captured.out
    assert "Bravo ! Vous êtes en dessous de la moyenne, continuez ainsi." in captured.out

def test_visualize_results(tmpdir):
    emissions = {
        'Transports': {'Avion': 200.0},
        'Logement': {'Fioul domestique': 6000.0},
        'Alimentation': {'Viande de boeuf': 1800.0},
        'Électronique': {'Tablette': 8.0}
    }
    
    file_name = tmpdir.join('emissions_par_categorie.png')
    visualize_results(emissions, file_path=str(file_name))
    assert file_name.check()
