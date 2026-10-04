# ML & DL Projects

A collection of my Machine Learning, Deep Learning, NLP and Computer Vision projects, all in one place. Each project lives in its own folder with its own README, notebook(s) and code. Commit history of every project was preserved.

**Author:** Ali Mohamed · [Kaggle](https://www.kaggle.com/alimohamed01) · [Email](mailto:alimohamed.fcai@gmail.com)

## Contents

- [Computer Vision](#computer-vision)
- [Natural Language Processing](#natural-language-processing)
- [Time Series & Anomaly Detection](#time-series--anomaly-detection)
- [Supervised ML: Regression](#supervised-ml-regression)
- [Supervised ML: Classification](#supervised-ml-classification)
- [Unsupervised ML: Clustering](#unsupervised-ml-clustering)
- [Data Analysis & Internship Work](#data-analysis--internship-work)

---

## Computer Vision

### [Flower Classification](./Flower_Classification)
Image classifier for flower types using transfer learning.
- Xception pretrained on ImageNet with custom Global-Average-Pooling and softmax layers
- Data augmentation (flip, rotation, contrast)
- TF Flowers dataset loaded through TensorFlow Datasets

### [Handwritten Digit Recognition](./HandWritten_Digit_Recognition)
CNN that recognizes handwritten digits.
- MNIST dataset (70,000 images)
- Convolution and max-pooling layers, Adam optimizer, sparse categorical cross-entropy
- Predictions visualized on sample images

### [German Traffic Sign Recognition](./german_traffic_signs)
CNN that classifies traffic signs, relevant to autonomous driving.
- GTSRB dataset, 43 classes
- LeNet-inspired architecture with data augmentation
- 83.40% test accuracy

---

## Natural Language Processing

### [NERbert: Fine-tuning BERT for NER](./NERbert)
Colab notebook showing how to fine-tune BERT for Named Entity Recognition.
- Tokenization and data formatting for BERT input
- Training, evaluation and model saving
- Easy to customize: entity types, hyperparameters, dataset

### [Named Entity Recognition (GMB)](./Named_Entity_Recognition)
NER model trained on the Groningen Meaning Bank dataset.
- Text preprocessing: token indexing and padding
- Model built with TensorFlow / Keras
- Inference pipeline with side-by-side comparison against spaCy

### [Spam Email Classification](./spam_emails_naive_bayes)
Spam detector using Naive Bayes.
- Text vectorization with CountVectorizer
- EDA, training and evaluation
- 98.84% accuracy

---

## Time Series & Anomaly Detection

### [SKAB Anomaly Detection](./SKAB_Anomaly-Detection)
Detects collective anomalies in industrial sensor data (Skoltech Anomaly Benchmark).
- Classical models: Isolation Forest, Local Outlier Factor, One-Class SVM, XGBoost
- Deep learning models: RNN and LSTM with skip connections
- Class imbalance handled with SMOTE
- Final model saved with pickle and tested on unseen valve data

---

## Supervised ML: Regression

### [California House Prices](./California_House_Prices)
End-to-end regression project from *Hands-on Machine Learning* (Chapter 2).
- EDA, preprocessing pipeline, one-hot encoding
- Compares Linear Regression, Decision Tree, Random Forest and XGBoost
- Best model: XGBRegressor (score 0.844, MAE 29,000)

### [Salary Prediction (Linear Regression)](./Linear-Regression-Salary-Model)
Predicts salary from years of experience using simple linear regression.

### [Start-ups Profit Prediction (MLR)](./start-ups_mlr)
Predicts start-up profit with Multiple Linear Regression.
- Pairplot and correlation heatmap for EDA
- One-hot encoding of the "State" feature
- Train/test split and model evaluation

---

## Supervised ML: Classification

### [Titanic Survival Prediction](./Titanic-ML-Model-Classification)
Predicts passenger survival with Logistic Regression.
- Detailed walkthrough of every dataset variable
- Feature engineering, model building, evaluation and prediction stages

### [Titanic Platform (Web App)](./titanic_platform)
Web application built around the Titanic survival model.
- Survival probability prediction from user input (class, gender, age)
- Pages for Prediction, Dashboard, About and Team
- Flask, Streamlit, scikit-learn and MySQL

### [Diabetes Prediction](./Diabetes-Patients)
Predicts whether a patient has diabetes from health indicators.
- Compares Logistic Regression, Random Forest, Decision Tree, XGBoost and SVC
- Hyperparameter tuning with Grid Search
- Logistic Regression selected for deployment

### [Breast Cancer Detection (SVC)](./breast_cancer_svc)
Classifies tumors as malignant or benign with a Support Vector Classifier.
- scikit-learn breast cancer dataset
- EDA with count plots, scatter plots, heatmaps and pair plots
- Evaluation with accuracy, precision, recall, F1 and confusion matrix

### [College Admission (Logistic Regression)](./admittance_lg)
Predicts college admission from SAT scores.
- Feature scaling with StandardScaler
- Plot of the fitted logistic curve
- Predictions for new instances

### [Facebook Ads Click Prediction](./facebook_ads_lg)
Predicts whether a customer clicks on an ad using Logistic Regression.
- Dataset statistics and EDA
- Train/test split with scaling
- Accuracy and confusion matrix

### [Social Network Ads: KNN](./social_network_ads_knn)
Purchase prediction from social network ads using K-Nearest Neighbors.
- Outlier handling and scaling
- Search for the optimal value of K

### [Social Network Ads: SVM](./social_network_ads_svm)
Same task solved with a Support Vector Classifier.
- Seaborn scatter plots for EDA
- Evaluation with accuracy score, confusion matrix and classification report

### [Social Network Ads: Random Forest](./social_network_ads_dt_random_forest)
Same task solved with Random Forest.
- Ensemble of decision trees
- Evaluation with standard classification metrics

---

## Unsupervised ML: Clustering

### [Mall Customer Segmentation (K-Means)](./Mall-Customer-Segmentation-Project)
Segments mall customers by age, gender, income and spending score.
- Optimal number of clusters via elbow method / silhouette analysis
- Interpretation of the resulting customer segments

### [Wholesale Customers (DBSCAN)](./Wholesale-customers)
Segments wholesale clients by annual spending on product categories (UCI dataset).
- Descriptive statistics for fresh, milk, grocery, frozen, detergents and delicatessen spending
- Density-based clustering with DBSCAN to find customer groups

### [Wholesale Customers (Hierarchical Clustering)](./Wholesale-Customer-Segmentation)
Customer segmentation with hierarchical clustering.
- Standardization of numerical features
- Euclidean distance with single linkage
- Dendrogram to choose the number of clusters

### [Wine Customers Segmentation](./Wine_Customers_Segmentation)
Wine dataset (UCI) classified into customer segments.
- Duplicate removal and feature scaling
- PCA for dimensionality reduction with a scree plot
- Logistic Regression on the reduced features

---

## Data Analysis & Internship Work

### [Amazon Sales Analysis (Power BI)](./Amazon-Sales)
Decision Support Systems course project analyzing Amazon sales data.
- Sales trends by month and by day of the quarter
- Average price per product and top 10 sales deviations
- Best sellers and business recommendations (promotions, targeted advertising)

### [Movie Revenue Optimization (TMDb)](./TMDb-movie-data)
Analyzes how genre, budget and popularity affect movie revenue.
- Adventure, action and animation genres bring the highest revenue
- Budget vs. revenue and audience popularity analysis
- Recommendations for studios

### [The Sparks Foundation Internship Tasks](./the-sparks-foundation-tasks)
Tasks completed during a 1-month remote Data Science & Business Analytics internship (January 2023).
- Task 1: supervised ML, predict student scores from study hours (linear regression)
- Task 2: unsupervised ML, find the optimal number of clusters on the Iris dataset
