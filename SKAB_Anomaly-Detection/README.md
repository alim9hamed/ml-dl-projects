### **Project Overview**
The primary objective of this project was to detect collective anomalies in sensor data using various anomaly detection techniques. The data was sourced from the **SKAB (Skoltech Anomaly Benchmark)**, a benchmark dataset designed for industrial settings.

---

### **Key Features**
1. **Dataset Handling**
   - Data loaded from multiple sensor datasets (anomaly-free, experimental data, valve-specific data).
   - Comprehensive preprocessing, including timestamp formatting and handling imbalanced classes using SMOTE.

2. **Exploratory Data Analysis (EDA)**
   - Distribution analysis of anomalies using scatterplots and feature correlations visualized through heatmaps.
   - Insights on feature imbalances and their implications for model performance.

3. **Modeling Techniques**
   - **Traditional ML Models**:
     - Isolation Forest
     - Local Outlier Factor
     - One-Class SVM
     - XGBoost
   - **Deep Learning Models**:
     - RNN (Recurrent Neural Networks)
     - LSTM (Long Short-Term Memory) with skip connections for enhanced learning.

4. **Model Evaluation**
   - Custom evaluation function with metrics like confusion matrix, accuracy, and classification report.
   - Metrics applied across models and datasets to ensure robustness.

5. **Deployment**
   - Final model saved using `pickle` for reuse and deployment.
   - Tested on unseen valve-specific data for performance validation.

---


### **Key Libraries and Tools**
- **Python**: Core scripting.
- **Machine Learning**: Scikit-learn, XGBoost, Imbalanced-learn (SMOTE).
- **Deep Learning**: TensorFlow, Keras.
- **Visualization**: Matplotlib, Seaborn.
- **Data Handling**: Pandas, NumPy.

---

### **Project Challenges and Solutions**
1. **Imbalanced Data**:
   - Used SMOTE to balance anomaly classes.
2. **Correlation Handling**:
   - Addressed feature correlation issues identified in heatmaps.
3. **Generalization**:
   - Evaluated models on unseen valve datasets for robustness.

---

[**SKAB (Skoltech Anomaly Benchmark)**](https://github.com/waico/SKAB).
