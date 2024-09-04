import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import pandas as pd
from Linearmodel.statistics import calculate_mean, calculate_std, calculate_correlation, calculate_median, calculate_variance, calculate_mode, calculate_weighted_mode, summary, find_highly_correlated_variables

def test_calculate_mean():
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
    mean = calculate_mean(data, 'col1')
    assert mean == 3.0

def test_calculate_std():
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
    std = calculate_std(data, 'col1')
    assert std == pytest.approx(1.414, 0.001)

def test_calculate_correlation():
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    correlation = calculate_correlation(data, 'col1', 'col2')
    assert correlation['Correlation'] == 1.0

def test_calculate_median():
    data = pd.DataFrame({'col1': [1, 3, 2, 5, 4]})
    median = calculate_median(data, 'col1')
    assert median == 3.0

def test_calculate_variance():
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
    variance = calculate_variance(data, 'col1')
    assert variance == 2.0

def test_calculate_mode():
    data = pd.DataFrame({'col1': [1, 2, 2, 3, 4]})
    mode = calculate_mode(data, 'col1')
    assert mode == 2

def test_calculate_weighted_mode():
    data = pd.DataFrame({'col1': [1, 1, 2, 2, 2, 3, 4]})
    weighted_mode = calculate_weighted_mode(data, 'col1')
    assert weighted_mode == 2

def test_summary():
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [5, 6, 7, 8, 9]})
    summary_dict = summary(data)
    assert 'col1' in summary_dict
    assert 'col2' in summary_dict

def test_find_highly_correlated_variables():
    data = pd.DataFrame({'target': [1, 2, 3, 4, 5], 'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]})
    highly_correlated = find_highly_correlated_variables(data, 'target', threshold=0.9)
    assert 'col1' in highly_correlated
    assert 'col2' in highly_correlated  
