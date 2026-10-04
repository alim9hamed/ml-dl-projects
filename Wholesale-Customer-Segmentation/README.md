# Mall Customer Segmentation using Hierarchical Clustering Algorithm

In this project, we will analyze a dataset containing information about mall customers and use hierarchical clustering algorithm to segment the customers into different groups based on their purchasing behavior. The dataset contains information about the customer's channel of purchase (i.e. through different retail outlets), region of residence, and the items they purchased in the mall.

## Data Preprocessing
The first step in the project is to preprocess the data by cleaning and transforming it. We will handle missing values, encode categorical variables, and scale the numerical variables.


### Scaling Numerical Variables
Numerical variables need to be scaled to a similar range before they can be used in the clustering algorithm. We will use standardization to scale the numerical variables to have zero mean and unit variance.

## Clustering using Hierarchical Clustering
After preprocessing the data, we can use the hierarchical clustering algorithm to segment the customers into different groups based on their purchasing behavior. The algorithm works by recursively splitting the data into smaller clusters based on the similarity between the data points.

### Distance Measure
The distance measure used in the hierarchical clustering algorithm is the Euclidean distance. This measure calculates the distance between two data points by taking the square root of the sum of the squared differences between their corresponding features.

### Linkage Criteria
The linkage criteria used in the hierarchical clustering algorithm is the single-linkage method. This method calculates the distance between two clusters by taking the minimum distance between any two data points in the two clusters.

### Dendrogram
A dendrogram is a graphical representation of the hierarchical clustering result. It shows the similarity between the clusters and the number of data points in each cluster. We can use the dendrogram to determine the number of clusters and the appropriate clustering criteria.

## Conclusion
In this project, we analyzed a dataset containing information about mall customers and used hierarchical clustering algorithm to segment the customers into different groups based on their purchasing behavior. We preprocessed the data by cleaning and transforming it, and used one-hot encoding and standardization to encode and scale the numerical variables. We used the Euclidean distance and single-linkage method to calculate the distance between clusters and the linkage criteria to determine the appropriate clustering criteria. Finally, we created a dendrogram to visualize the clustering result.
