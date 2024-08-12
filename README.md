# Customer Segmentation Project

## Overview
This project focuses on customer segmentation using various clustering methods. The main goal is to analyze customer data, group similar customers together, and build a predictive model that can classify new customers into these groups. 

### Key Steps:
1. **Exploratory Data Analysis (EDA):** Conducted EDA, data cleaning, preprocessing, visualization, transformation, and encoding to understand the data and gain insights.
2. **Clustering Techniques:** Applied different clustering methods to segment customers:
   - **Hierarchical Clustering with Single Linkage**
   - **Hierarchical Clustering with Complete Linkage**
   - **Agglomerative Clustering**
   - **K-Means Clustering** (Chosen for its superior silhouette score)
   - **DBSCAN Clustering**
3. **Predictive Modeling:** Built a logistic regression model to classify new customers into clusters based on their feature values.
4. **Model Saving and Pipeline Creation:** Developed a pipeline using the `ColumnTransformer` class to preprocess new customer data before passing it to the model.
5. **Deployment:** Deployed the model using Streamlit, creating an interactive web application for customer segmentation.

## Project Structure
