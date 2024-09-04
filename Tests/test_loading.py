import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import pandas as pd
from Linearmodel.loading import load_data

def test_load_data():
    df = load_data('eCO2mix_RTE_Annuel-Definitif_2020.csv')
    assert not df.empty
    assert 'Datetime' in df.columns
