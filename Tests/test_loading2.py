import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import pandas as pd
from Carboncalc.loading2 import load_carbon_data, enrich_carbon_data, save_combined_data

def test_load_carbon_data():
    df = load_carbon_data('basecarbone_sample.csv', separator=';')
    assert not df.empty
    assert 'Nom base français' in df.columns

def test_enrich_carbon_data():
    df_combined = enrich_carbon_data('basecarbone_sample.csv', 'basecarbone-v17-fr.csv')
    assert not df_combined.empty
    assert 'Nom base français' in df_combined.columns
    assert 'Total poste non décomposé' in df_combined.columns

def test_save_combined_data(tmpdir):
    df_combined = enrich_carbon_data('basecarbone_sample.csv', 'basecarbone-v17-fr.csv')
    file_path = tmpdir.join('basecarbone_combined.csv')
    save_combined_data(df_combined, file_path)
    assert file_path.check()