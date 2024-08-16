# End to End Customer Segmentation Project

## Overview
This project is a part of my Data Science course at ExcelR Edtech Pvt. Ltd. Pune which focuses on customer segmentation using various clustering methods. The main goal is to analyze customer data, group similar customers together, and build a predictive model that can classify new customers into these groups. 

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

## Dataset
The dataset consists of customer information such as age, income, spending score, and other relevant features. This data was used to perform customer segmentation and build the predictive model. [Link to the dataset if available]

## Clustering Methods
The following clustering methods were implemented:
- **Hierarchical Clustering (Single & Complete Linkage):** Grouping customers based on different linkage criteria.
- **Agglomerative Clustering:** A method that builds clusters in a bottom-up manner.
- **K-Means Clustering:** Chosen for its optimal performance based on silhouette scores.
- **DBSCAN Clustering:** A density-based clustering approach.

## Predictive Modeling
A logistic regression model was built to classify new customers into the appropriate clusters. After testing various classification algorithms, logistic regression was selected for its simplicity and effectiveness.

## Deployment
The final model was deployed using Streamlit. The application allows users to input new customer data and predict the corresponding cluster.

### How to Run the App:
1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   
2. Run the Streamlit application
   ```bash
   streamlit run app.py

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/Thakarepradnyan/customer_segmentation_P416.git

2. Navigate to the project directory:
   ```bash
   cd customer-segmentation

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
## Usage
- Run the Jupyter notebooks in the `notebooks` directory to replicate the analysis.
- Launch the Streamlit application for real-time customer segmentation predictions.

## Contributing
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or suggestions, please reach out:

- **Pradnyan Thakare** - [LinkedIn](https://www.linkedin.com/in/pradnyanthakare) | [GitHub](https://github.com/Thakarepradnyan)


