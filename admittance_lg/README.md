# Admittance Logistic Regression Project

This repository contains a project focused on predicting college admission using logistic regression. Logistic regression is a popular machine learning algorithm used for binary classification tasks, making it suitable for predicting whether a student will be admitted to a college or not. In this article, we will discuss the different levels of the project, including creating and inspecting the dataset, splitting and preprocessing the data, data exploration, model training and predicting, predicting new instances, and plotting the logistic model. Let's dive in!

### Creating & Inspecting Dataset
To start the project, we create a dataset that includes relevant features such as SAT scores and admission outcomes (admitted or not admitted). The dataset typically consists of these features for a set of students. After creating the dataset, we can inspect it using the `describe` function to gain insights into the data's statistical properties, such as mean, standard deviation, minimum, maximum, and quartiles.

### Splitting & Preprocessing Data
Next, we split the dataset into training and testing sets. This division allows us to evaluate the performance of our logistic regression model on unseen data. Additionally, we preprocess the data by scaling it using the `StandardScaler` to ensure that all features are on a similar scale. Scaling is necessary to avoid features with larger values dominating the model's training process.

### Data Exploration
Exploratory data analysis (EDA) is an essential step in understanding the dataset and gaining insights into the relationships between different features. In this project, we can plot a scatter plot between SAT scores and admission outcomes to visualize the relationship between these two variables. This plot can help us identify any patterns or trends in the data and determine if there is a correlation between SAT scores and admission.

### Model Training & Predicting
Now, we can train our logistic regression model using the training data. Logistic regression finds the best-fitting line that separates the admitted and not admitted classes based on the provided features. Once the model is trained, we can make predictions on the testing data to evaluate how well our model generalizes to unseen instances.

### Predicting New Instances
Apart from evaluating the model's performance on the testing data, we can also use it to predict the admission outcome for new instances. By providing the model with new SAT scores and high school GPAs, we can obtain predictions on whether a student is likely to be admitted or not.

### Plotting Logistic Model
To visualize the logistic regression model, we can plot the decision boundary that separates the admitted and not admitted classes. This boundary is determined by the coefficients learned during the model training process. Plotting the logistic model provides a visual representation of how the model distinguishes between the two admission outcomes based on the given features.

By following the levels outlined above, you can create a logistic regression model to predict college admission based on SAT scores and other relevant features. Feel free to explore the code and modify it to fit your specific needs. Good luck with your admission prediction project!
