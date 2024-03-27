# Loss Accuracy Deviation in Dropout by Rayleigh Quotient Exploration

## Introduction

This script is designed for conducting an in-depth evaluation and analysis of a neural network model trained on the MNIST dataset. The primary focus is to analyze the effect of dropout on neurons with different alignments measured by the Rayleigh Quotient. It includes steps for model loading, dropout experimentation, prediction testing, and visualization of results through confusion matrices and confidence assessments.

## Execution Steps

1. **Model Loading**
   - Loads a trained model from a specified path.

2. **Autoreload Setup**
   - Ensures that any updates in the module functions are automatically reloaded.

3. **Dynamic Path Adjustment**
   - Modifies the system path to import custom modules necessary for further analysis.

4. **Importing Analysis Functions**
   - Imports functions for testing the model, performing progressive dropout, and analyzing the dropout effects.

5. **Checkpoint Loading**
   - Loads model weights from a checkpoint for accurate model evaluation.

6. **Model Testing and Alignment Analysis**
   - Tests the loaded model on a dataset and calculates alignment metrics.

7. **Dropout Analysis**
   - Performs dropout analysis by selectively dropping out neurons based on their alignment (high, random, low) and evaluates the model's performance.

8. **Weight Access and Visualization**
   - Accesses model weights for analysis and visualizes the model's predictions, accuracies, and losses.

9. **Confidence and Confusion Matrix Calculation**
   - Calculates and visualizes a confusion matrix.
   - Analyzes the confidence of the model's predictions.

10. **Results Visualization**
    - Uses `matplotlib` and `seaborn` to plot confusion matrices and confidence levels.
    - Presents the data in tabular form using `tabulate` for clarity.

## Outputs

- A series of print statements and visualizations that provide insights into the model's performance, including accuracy, average loss, and prediction confidence levels.
- Confusion matrices that illustrate the model's prediction capabilities across different classes.
- A heatmap of average confidences for predictions, viewing of the model's certainty in its classifications.
- Matrices filtered by confidence, and confidence heatmaps filtered by the number of observations in each cell
- Analysis of the prediction behavior of different checkpoints to test if the model collapses to predicting certain values of if this behavior as it dropouts nodes is random

## Usage Notes

- Before executing the script, ensure that the paths to the model checkpoint (`checkpoint_path`) and the results file (`results_path`) are correctly set to the locations where your model's data is stored.

