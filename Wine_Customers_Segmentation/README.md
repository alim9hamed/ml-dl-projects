# Wine Customers Segmentation Project

## 1. Importing Data

To kick off the project, I imported the wine dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/109/wine).

## 2. Data Preprocessing

I started by checking for any duplicated data points and removed them from the dataset. Then, I split the data into features and the target variable. To handle outliers and bring the features to a comparable scale, I applied feature scaling using StandardScaler.

## 3. Dimensionality Reduction using PCA

Since the wine dataset contains multiple features, I employed Principal Component Analysis (PCA) for dimensionality reduction. PCA helped me identify the most significant components that explain the majority of the dataset's variance. To visualize the importance of each principal component, I created a scree plot, which provided insights into the variance explained by each component.

## 4. Scatterplot for Training Data

After reducing the dimensionality, I created a scatterplot using the selected principal components. This visualization allowed me to observe patterns and clusters within the training data. It provided valuable insights into the potential segmentation of wine customers based on their attributes.

## 5. Building and Testing Model using Logistic Regression

For the wine customer segmentation, I chose to utilize the logistic regression model. Logistic regression is a powerful algorithm for classification tasks. I built and trained the logistic regression model using the training dataset. By iteratively optimizing the model's parameters, I achieved a well-performing classifier.

## 6. Prediction

With the trained model, I made predictions on new, unseen data to assign wine customers to their respective segments. This enabled personalized marketing strategies and tailored recommendations based on individual customer preferences.

## 7. Evaluation of Model

To evaluate the model's performance, I employed various evaluation metrics such as accuracy, precision, and recall. These metrics provided insights into how well the model classified customers into their appropriate segments. I ensured the model's effectiveness by comparing its predictions with the actual customer segments.

I'm proud of the outcomes achieved in this project, as it enabled a deeper understanding of customer segmentation in the wine industry. The insights obtained can guide winemakers and marketers in tailoring their products and strategies to different customer segments, resulting in better customer satisfaction and increased sales.

If you're interested in learning more about this project or discussing wine customer segmentation, feel free to reach out.
