# Customer_Segmentation_P416

Overview
The objective of this project is to perform customer segmentation using various clustering methods and evaluate these models to select the most appropriate one. The project is structured into several steps:

Exploratory Data Analysis (EDA): The first step involves EDA, data cleaning, preprocessing, visualization, transformation, and encoding to understand the data and gain insights.
Clustering Techniques: Different clustering techniques are applied to group customers with similar patterns or information:
Hierarchical Clustering with Single Linkage
Hierarchical Clustering with Complete Linkage
Agglomerative Clustering
K-Means Clustering
DBSCAN Clustering
After evaluating the clustering models using silhouette scores, K-Means clustering was chosen as the best-performing model.
Predictive Model Building: A predictive model is built to classify new customers into appropriate clusters based on new feature values. After testing various classification algorithms, a simple logistic regression algorithm was selected for this task.
Model Saving and Pipeline Creation: The chosen model is saved, and a pipeline is created to pass newly entered customer data through the model. The pipeline includes a column transformer for feature transformation.
Deployment: The final step involves deploying the model using Streamlit to create an interactive web application (app.py).
