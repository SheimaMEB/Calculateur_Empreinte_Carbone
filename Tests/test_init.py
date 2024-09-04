def Tests_imports():
    from Linearmodel.loading import load_data
    from Linearmodel.statistics import calculate_mean, calculate_std, calculate_correlation, calculate_median, calculate_variance, calculate_mode, calculate_weighted_mode, summary, find_highly_correlated_variables
    from Linearmodel.visualization import plot_multiple_boxplots, plot_scatter, plot_heatmap, plot_predictions_vs_observations, plot_multiple_histograms
    from Linearmodel.regression import OrdinaryLeastSquares
