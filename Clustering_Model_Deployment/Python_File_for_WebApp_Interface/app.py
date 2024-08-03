import pickle
import streamlit as st
import pandas as pd

st.title('Customer Segmentation Clustering :shopping_trolley:')
load = open('Lr_Cluster_model.pkl', 'rb')
model = pickle.load(load)

def predict(Income, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds,
            NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, Complain, 
            Response, Age, Cust_Since_yrs, Num_Childrns, AcceptedCmp, Total_amt_spend):
    
    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'Income': [Income],
        'Recency': [Recency],
        'MntWines': [MntWines],
        'MntFruits': [MntFruits],
        'MntMeatProducts': [MntMeatProducts],
        'MntFishProducts': [MntFishProducts],
        'MntSweetProducts': [MntSweetProducts],
        'MntGoldProds': [MntGoldProds],
        'NumDealsPurchases': [NumDealsPurchases],
        'NumWebPurchases': [NumWebPurchases],
        'NumCatalogPurchases': [NumCatalogPurchases],
        'NumStorePurchases': [NumStorePurchases],
        'NumWebVisitsMonth': [NumWebVisitsMonth],
        'Complain': [1 if Complain == 'True' else 0],
        'Response': [1 if Response == 'True' else 0],
        'Age': [Age],
        'Cust_Since_yrs': [Cust_Since_yrs],
        'Num_Childrns': [Num_Childrns],
        'AcceptedCmp': [AcceptedCmp],
        'Total_amt_spend': [Total_amt_spend]
    })
    
    prediction = model.predict(input_data)
    return prediction
    
def main():
    st.markdown('This is a webapp which helps businesses to know their customers.')
    st.markdown('Use this tool for sorting your customers based on their information.')
    st.markdown('This tool can help businesses to provide offers and discounts to customers based on the group or cluster they belong to.')
    Income = st.number_input('Income of Customer', min_value=1200, max_value=70000)
    Recency = st.number_input('Number of Days since Customer Last Purchased', min_value=0, max_value=100)
    MntWines = st.number_input('Amount Spend on Wines', min_value=0, max_value=1500)
    MntFruits = st.number_input('Amount Spend on Fruits', min_value=0, max_value=1500)
    MntMeatProducts = st.number_input('Amount Spend on Meat Products', min_value=0, max_value=2000)
    MntFishProducts = st.number_input('Amount Spend on Fish Products', min_value=0)
    MntSweetProducts = st.number_input('Amount Spend on Sweets', min_value=0, max_value=300)
    MntGoldProds = st.number_input('Amount Spend on Gold Products', min_value=0, max_value=800)
    NumDealsPurchases = st.number_input('Number of Purchases Made With a Discount', min_value=0, max_value=15)
    NumWebPurchases = st.number_input('Number of Purchases Made through Website', min_value=0, max_value=30)
    NumCatalogPurchases = st.number_input('Number of Purchases Made through Catalog', min_value=0, max_value=30)
    NumStorePurchases = st.number_input('Number of Purchases Made through Store', min_value=0, max_value=30)
    NumWebVisitsMonth = st.number_input('Number of Times Customer Visited Website', min_value=0, max_value=30)
    Complain = st.selectbox('Customer Complained in Last 2 Years', ('True', 'False'))
    Response = st.selectbox('Did Customer Respond to Marketing Campaigns', ('True', 'False'))
    Age = st.number_input('Age of Customer', min_value=20, max_value=100)
    Cust_Since_yrs = st.number_input('Years of Relationship with Company', min_value=5, max_value=15)
    Num_Childrns = st.number_input('Number of Children Customer Has', min_value=0, max_value=5)
    AcceptedCmp = st.number_input('Which Campaign Did Customer Accept', min_value=0, max_value=4)
    
    Total_amt_spend = MntFishProducts + MntFruits + MntGoldProds + MntMeatProducts + MntSweetProducts + MntWines



    
    if st.button('Predict Cluster'):
        result = predict(Income, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds,
                         NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, Complain, 
                         Response, Age, Cust_Since_yrs, Num_Childrns, AcceptedCmp, Total_amt_spend)
        st.success('Customer with Above Information Belongs To Cluster: {}'.format(result))

if __name__ == '__main__':
    main()
