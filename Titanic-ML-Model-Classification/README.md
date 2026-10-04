
<img src="https://i.ytimg.com/vi/g6viRUTuGhg/maxresdefault.jpg" alt="titanic" width="1200" height="200">

# Titanic Survival Prediction Project using Logistic Regression Algorithm

In this article, we will explore a fascinating project involving the prediction of survival on the Titanic using the classification logistic regression algorithm. The dataset used in this project consists of various variables that provide information about the passengers on board. The goal is to analyze the data and build a model that can accurately predict whether a passenger survived the sinking of the Titanic or not. Let's dive into the stages of this project and the significance of each variable.

## Dataset Variables

1. **Survived**: This field indicates whether or not the passenger survived the sinking of the Titanic. A value of 1 indicates that the passenger survived, while a value of 0 indicates that they did not.

2. **Pclass**: This field indicates the class of the passenger. A value of 1 indicates the first class, a value of 2 indicates the second class, and a value of 3 indicates the third class.

3. **Name**: This field contains the name of the passenger.

4. **Sex**: This field indicates the gender of the passenger. A value of "male" indicates that the passenger is male, while a value of "female" indicates that the passenger is female.

5. **Age**: This field contains the age of the passenger.

6. **SibSp**: This field indicates the number of siblings and spouses aboard the Titanic.

7. **Parch**: This field indicates the number of parents and children aboard the Titanic.

8. **Ticket**: This field contains the ticket number of the passenger.

9. **Fare**: This field contains the fare paid by the passenger.

10. **Cabin**: This field contains the cabin number of the passenger.

11. **Embarked**: This field indicates the port where the passenger boarded the Titanic. A value of "C" indicates that the passenger boarded in Cherbourg, a value of "Q" indicates that the passenger boarded in Queenstown, and a value of "S" indicates that the passenger boarded in Southampton.

## Stages of the Project

### 1. Data Collection and Preparation
The first stage involved collecting the Titanic dataset, ensuring it contained the necessary variables mentioned above. The dataset was carefully curated to ensure data accuracy and completeness. Any missing values or inconsistencies were addressed through data cleaning and preprocessing techniques.

### 2. Exploratory Data Analysis (EDA)
During the EDA stage, a comprehensive analysis of the dataset was conducted. This included data visualization, statistical summaries, and correlations between variables. Exploring the data helped identify patterns, trends, and relationships that could influence the survival prediction process.

### 3. Feature Engineering
Feature engineering involved selecting and transforming the most relevant variables for the logistic regression model. This stage helped improve the model's accuracy by creating new features or modifying existing ones to capture meaningful information. For example, extracting titles from passenger names or creating age groups from the "Age" variable.

### 4. Model Building and Training
In this stage, the logistic regression algorithm was applied to build a predictive model. The dataset was split into training and testing sets to evaluate the model's performance. The logistic regression algorithm calculated the probabilities of survival for each passenger based on the selected features.

### 5. Model Evaluation
The trained model was evaluated using various evaluation metrics such as accuracy, precision, recall, and F1-score. Cross-validation techniques were employed to ensure the model's robustness and generalizability. The evaluation results provided insights into the model's performance and helped identify areas for improvement.

### 6. Prediction and Deployment
Once the model was deemed satisfactory, it was used to make predictions on new, unseen data. The model's predictions were then deployed for practical use, such as predicting survival probabilities for passengers in real-world scenarios.

## Conclusion
The Titanic survival prediction project using the logistic regression algorithm demonstrates the power of data analysis and machine learning techniques in understanding historical events. By analyzing various passenger variables, we can build models that accurately predict survival probabilities. This project showcases the stages involved in data collection, preprocessing, model building, evaluation, and prediction.
