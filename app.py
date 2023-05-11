import pandas as pd
import numpy as np
from dill import load
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# loading the saved model
loaded_model  =load(open('final_model.pkl','rb'))

#Defining a function for prediction
def Cluster_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    #Normalizing the given data (Since we have used Normalized Data while building the model)
    normalized_input = MinMaxScaler().fit_transform(input_data_as_numpy_array)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = normalized_input.reshape(1,-1)
    
    #Predicting Cluster
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'DEVELOPED COUNTRY'
    elif (prediction[0] == 1):
        return 'UNDER DEVELOPED COUNTRY'
    else:  
        return 'DEVELOPING COUNTRY'  


def main():
    
    # giving a title
    st.markdown("<h1 style='color:green;'>Predicting the state of Development of a Country</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='color:blue;'>Check the Values</h5>", unsafe_allow_html=True)
    st.sidebar.markdown("<h5 style='color: blue ;'>Enter the necessary details to find whether the Country is Developed or Underdeveloped or Developing country</h5>", unsafe_allow_html=True)
    st.sidebar.markdown("<h5 style='color: red ;'>Note: Please Enter all Values to avoid Errors</h5>", unsafe_allow_html=True)

    
    # getting the input data from the user
    Birth_Rate = st.sidebar.number_input('Birth Rate (0.000-1.000)',step=0.001, format="%.3f")
    Business_Tax_Rate = st.sidebar.number_input('Business Tax Rate (Do not include "%")')
    CO2_Emissions = st.sidebar.number_input('CO2 Emissions')
    Days_to_Start_Business = st.sidebar.number_input('Days to Start Business')
    Energy_Usage = st.sidebar.number_input('Energy Usage')
    GDP = st.sidebar.text_input('Total GDP ($)')
    Health_Exp_GDP = st.sidebar.number_input('Health Exp % GDP (Do not include "%")')/100
    Health_Exp_Capita = st.sidebar.number_input('Health Exp/Capita ($)')
    Hours_to_do_Tax = st.sidebar.number_input('Hours to do Tax')
    Infant_Mortality_Rate = st.sidebar.number_input('Infant Mortality Rate (0.000-1.000)',step=0.001, format="%.3f")
    Internet_Usage = st.sidebar.number_input('Internet Usage')
    Lending_Interest = st.sidebar.number_input('Lending Interest')
    Life_Expectancy_Female = st.sidebar.number_input('Life Expectancy Female (Age)')
    Life_Expectancy_Male = st.sidebar.number_input('Life Expectancy Male(Age)')
    Mobile_Phone_Usage = st.sidebar.number_input('Mobile Phone Usage')
    Population_0_14 = st.sidebar.number_input('Percentage of Population between 0-14 (Do not include "%")')/100
    Population_15_64 = st.sidebar.number_input('Percentage of Population between 15-64 (Do not include "%")')/100
    Population_65_and_above = st.sidebar.number_input('Population percentage of people above the age of 65 (Do not include "%")')/100
    Population_Total = st.sidebar.text_input('Total population')
    Population_Urban = st.sidebar.number_input('Population Urban % (Do not include "%")')/100
    Tourism_Inbound = st.sidebar.text_input('Tourism Inbound ($)')
    Tourism_Outbound = st.sidebar.text_input('Tourism Outbound ($)')
    
    data = {'Birth rate' : Birth_Rate, 'Business tax rate' : Business_Tax_Rate, 'CO2 Emissions': CO2_Emissions,
       'Days to start business' : Days_to_Start_Business, 'Energy usage' : Energy_Usage,
       'GDP':GDP, 'Health Exp % in GDP': Health_Exp_GDP,'Health exp/capita': Health_Exp_Capita,
       'Hours to do Tax':Hours_to_do_Tax, 'Infant Mortality Rate' : Infant_Mortality_Rate, 'Internet usage':Internet_Usage,
       'Lending interest': Lending_Interest, 'Life expectancy female':Life_Expectancy_Female, 'Life expectancy male':Life_Expectancy_Male,
       'Mobile phone usage' : Mobile_Phone_Usage, 'Population%(0-14)' : Population_0_14 , 'Population%(15-64)' : Population_15_64 ,
       'Population% 65+' : Population_65_and_above , 'Total Population' : Population_Total , 
       'Urban Population %' : Population_Urban, 'Tourism Inbound' : Tourism_Inbound,'Tourism Outbound': Tourism_Outbound}
        
    df = pd.DataFrame(data,index=['Values'])
    df= df.T
    st.dataframe(df,width=500,height=806)

    # code for Prediction
    Predict = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        Predict = Cluster_prediction([[Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business,Energy_Usage, GDP, Health_Exp_GDP,Health_Exp_Capita,Hours_to_do_Tax, Infant_Mortality_Rate, Internet_Usage,Lending_Interest,Life_Expectancy_Female, Life_Expectancy_Male, Mobile_Phone_Usage, Population_0_14, Population_15_64,Population_65_and_above, Population_Total, Population_Urban,Tourism_Inbound,Tourism_Outbound]])

        if (Predict == 'DEVELOPED COUNTRY'):
            color = 'green'
        elif (Predict == 'UNDER DEVELOPED COUNTRY'):
            color = 'red'
        else:
            color = 'blue'
    
        st.write(f'This is a <span style="color:{color}">{Predict}</span>.', unsafe_allow_html=True)
        
    
if __name__ == '__main__':
    main()