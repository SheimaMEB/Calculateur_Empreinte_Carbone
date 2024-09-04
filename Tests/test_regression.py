import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import numpy as np
from Linearmodel.regression import OrdinaryLeastSquares

def test_ols_fit():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    model = OrdinaryLeastSquares(intercept=True)
    model.fit(X, y)
    coeffs = model.get_coeffs()
    assert len(coeffs) == 3  
    assert np.allclose(coeffs, [3, 1, 2])

def test_ols_predict():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    model = OrdinaryLeastSquares(intercept=True)
    model.fit(X, y)
    X_test = np.array([[3, 5], [1, 2]])
    y_pred = model.predict(X_test)
    assert len(y_pred) == 2
    assert np.allclose(y_pred, [16, 8])

def test_determination_coefficient():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    model = OrdinaryLeastSquares(intercept=True)
    model.fit(X, y)
    r_squared = model.determination_coefficient(X, y)
    assert r_squared == 1.0
