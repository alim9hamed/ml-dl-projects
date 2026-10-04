# Facebook Ads Project Using Logistic Regression

This repository contains a project focused on analyzing Facebook ads data using logistic regression. Logistic regression is a popular machine learning algorithm used for binary classification tasks, making it suitable for predicting whether a customer will click on a Facebook ad or not. In this article, we will discuss the different stages of the project, including importing libraries, loading datasets, extracting features, conducting data exploration, data splitting and preprocessing, and model training and prediction. Let's dive in!

### Importing Libraries
To start the project, we need to import the necessary libraries that provide the tools and functions required for data analysis and modeling.

### Importing Datasets and Extracting Features
Next, we import the Facebook ads dataset that contains information about customers and whether they clicked on an ad. The dataset typically includes features like names, emails, country, time spent on the site, salary, and the target variable indicating whether a customer clicked on the ad or not. By loading the dataset, we can extract the relevant features and the target variable.

### Statistical Data
Before diving into exploratory data analysis, let's take a look at some statistical information about the dataset:

- Total Number of Customers: 499
- Number of Customers who Clicked on the Ad: 250
- Percentage of Customers who Clicked: 50.10%
- Number of Customers who Did Not Click: 249
- Percentage of Customers who Did Not Click: 49.90%

These statistics provide a basic overview of the dataset and the balance between the two classes (clicked and not clicked) that we will be predicting.

### Data Exploration
Exploratory data analysis (EDA) is a crucial step in understanding the dataset and gaining insights into the relationships between different features. In this project, we use various visualization techniques to explore the Facebook ads data. Specifically, we create a scatter plot to analyze the relationship between time spent on the site, salaries, and whether a customer clicked on the ad. The scatter plot allows us to visually identify any patterns or trends in the data.

### Data Splitting and Preprocessing
Before training our logistic regression model, we need to split the data into training and testing sets. This helps us evaluate the performance of the model on unseen data. Additionally, we perform data preprocessing steps such as dropping irrelevant features like names, emails, and country. We also use the StandardScaler to handle outliers and scale the remaining features, ensuring that they are on a similar scale for accurate modeling.

### Model Training and Prediction
Now we can train our logistic regression model using the training data. Logistic regression fits a line that best separates the clicked and not clicked classes based on the provided features. Once the model is trained, we can make predictions on the testing data and evaluate the model's performance.

### Model Evaluation and Prediction
To evaluate the model, we calculate metrics such as accuracy and create a confusion matrix to visualize the model's predictions compared to the actual results. This allows us to assess the model's effectiveness in predicting whether a customer will click on a Facebook ad.

### Variables Used
The variables used in this project are as follows:

- Names: The names of the customers (dropped during preprocessing).
- Emails: The emails of the customers (dropped during preprocessing).
- Country: The country of the customers (dropped during preprocessing).
- Time Spent on Site: The amount of time a customer spends on the site.
- Salary: The salary of the customer.
- Clicked: The target variable indicating whether a customer clicked on the ad or not.

These variables are crucial in training our logistic regression model and predicting ad clicks.

By following the stages outlined above, you can analyze Facebook ads data using logistic regression and gain insights into the factors that influence ad clicks. Feel free to explore the code and modify it to fit your specific needs. Happy analyzing!
