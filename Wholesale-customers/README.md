# Wholesale Customer Project: Exploring Customer Segmentation using DBSCAN Algorithm

## Introduction
In today's business landscape, understanding customer behavior and segmenting them based on their characteristics is crucial for targeted marketing and personalized services. The Wholesale Customers dataset, available in the UCI Machine Learning Repository, offers valuable insights into the spending patterns of clients in the wholesale distribution industry. In this article, we will explore the dataset and apply the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to identify customer segments based on their annual spending habits.

## Dataset Overview
The Wholesale Customers dataset consists of annual spending in monetary units (m.u.) on various product categories by wholesale distributor clients. The dataset contains the following variables:

1. FRESH: Annual spending on fresh products.
2. MILK: Annual spending on milk products.
3. GROCERY: Annual spending on grocery products.
4. FROZEN: Annual spending on frozen products.
5. DETERGENTS_PAPER: Annual spending on detergents and paper products.
6. DELICATESSEN: Annual spending on delicatessen products.
7. CHANNEL: Customers' channel, either Horeca (Hotel/Restaurant/Café) or Retail.
8. REGION: Customers' region, including Lisbon, Oporto, or other.

## Additional Variable Information
To gain a better understanding of the dataset, let's dive into the additional variable information:

1. FRESH: Represents the annual spending on fresh products. It is a continuous variable.
2. MILK: Represents the annual spending on milk products. It is a continuous variable.
3. GROCERY: Represents the annual spending on grocery products. It is a continuous variable.
4. FROZEN: Represents the annual spending on frozen products. It is a continuous variable.
5. DETERGENTS_PAPER: Represents the annual spending on detergents and paper products. It is a continuous variable.
6. DELICATESSEN: Represents the annual spending on delicatessen products. It is a continuous variable.
7. CHANNEL: Represents the customers' channel, either Horeca (Hotel/Restaurant/Café) or Retail. It is a nominal variable.
8. REGION: Represents the customers' region, including Lisbon, Oporto, or other. It is a nominal variable.

## Descriptive Statistics
To gain insights into the dataset's distribution and central tendencies, let's examine the descriptive statistics:

- FRESH:
  - Minimum: 3 m.u.
  - Maximum: 112,151 m.u.
  - Mean: 12,000.30 m.u.
  - Standard Deviation: 12,647.329 m.u.

- MILK:
  - Minimum: 55 m.u.
  - Maximum: 73,498 m.u.
  - Mean: 5,796.27 m.u.
  - Standard Deviation: 7,380.377 m.u.

- GROCERY:
  - Minimum: 3 m.u.
  - Maximum: 92,780 m.u.
  - Mean: 7,951.28 m.u.
  - Standard Deviation: 9,503.163 m.u.

- FROZEN:
  - Minimum: 25 m.u.
  - Maximum: 60,869 m.u.
  - Mean: 3,071.93 m.u.
  - Standard Deviation: 4,854.673 m.u.

- DETERGENTS_PAPER:
  - Minimum: 3 m.u.
  - Maximum: 40,827 m.u.
  - Mean: 2,881.49 m.u.
  - Standard Deviation: 4,767.854 m.u.

- DELICATESSEN:
  - Minimum: 3 m.u.
  - Maximum: 47,943 m.u.
  - Mean: 1,524.87 m.u.
  - Standard Deviation: 2,820.106 m.u.

The dataset also provides information on the frequency of customers in each region and channel:

- REGION:
  - Lisbon: 77 customers
  - Oporto: 47 customers
  - Other Region: 316 customers
  - Total: 440 customers

- CHANNEL:
  - Horeca: 298 customers
  - Retail: 142 customers
  - Total: 440 customers

## Applying DBSCAN Algorithm for Customer Segmentation
To perform customer segmentation based on their spending habits, we can utilize the DBSCAN algorithm. DBSCAN is a density-based clustering algorithm that groups together data points based on their density within the feature space. It is particularly useful for identifying clusters of varying shapes and sizes.

By applying DBSCAN to the Wholesale Customers dataset, we can uncover distinct customer segments characterized by their annual spending patterns. The algorithm will group together customers who exhibit similar spending behavior while identifying any outliers or noise.

## Conclusion
The Wholesale Customers dataset provides valuable information about the annual spending habits of wholesale distributor clientsand allows us to gain insights into customer segmentation. By utilizing the DBSCAN algorithm, we can identify distinct customer segments based on their spending patterns. This information can be used by businesses to tailor their marketing strategies, optimize product offerings, and provide personalized services to different customer groups.

It's important to note that the dataset contains additional variables such as FRESH, MILK, GROCERY, FROZEN, DETERGENTS_PAPER, DELICATESSEN, CHANNEL, and REGION. These variables provide further context and help understand the customers' spending behavior in different product categories, channels, and regions.

In conclusion, the Wholesale Customers project, combined with the DBSCAN algorithm, offers a powerful approach to customer segmentation in the wholesale distribution industry. By leveraging the dataset's valuable insights and applying advanced clustering techniques, businesses can make informed decisions to enhance customer satisfaction and drive growth.

References:
- [UCI Machine Learning Repository - Wholesale customers](https://archive.ics.uci.edu/ml/datasets/wholesale+customers)
