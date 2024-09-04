import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from Linearmodel.visualization import plot_multiple_histograms, plot_multiple_boxplots, plot_scatter, plot_heatmap, plot_predictions_vs_observations

def test_plot_multiple_histograms(tmpdir):
    data = pd.DataFrame({'col1': [1, 2, 2, 3, 4], 'col2': [5, 4, 4, 3, 2]})
    file_name = tmpdir.join('multiple_histograms.png')
    plot_multiple_histograms(data, ['col1', 'col2'], file_name)
    assert file_name.check()

def test_plot_multiple_boxplots(tmpdir):
    data = pd.DataFrame({'col1': [1, 2, 2, 3, 4], 'col2': [5, 4, 4, 3, 2]})
    file_name = tmpdir.join('multiple_boxplots.png')
    plot_multiple_boxplots(data, ['col1', 'col2'], file_name)
    assert file_name.check()

def test_plot_scatter(tmpdir):
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]})
    file_name = tmpdir.join('scatter_plot.png')
    plt.figure()
    plot_scatter(data, 'col1', 'col2')
    plt.savefig(file_name)
    assert file_name.check()

def test_plot_heatmap(tmpdir):
    data = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]})
    file_name = tmpdir.join('heatmap.png')
    plt.figure()
    plot_heatmap(data)
    plt.savefig(file_name)
    assert file_name.check()

def test_plot_predictions_vs_observations(tmpdir):
    y_true = [1, 2, 3, 4, 5]
    y_pred = [1.1, 1.9, 3.0, 4.1, 5.1]
    file_name = tmpdir.join('predictions_vs_observations.png')
    plot_predictions_vs_observations(y_true, y_pred, file_name)
    assert file_name.check()
