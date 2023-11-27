#pip install scikit-learn
import sklearn
import numpy as np
import pickle
import streamlit as st
load_model = pickle.load(open('C:/BIA NOTES/ML Model Implementation/train_model.sav','rb'))

def diabetes_prediction(input_data):
   # input = (6,148,72,35,0,33.6,0.627,50)
    np_array=np.asarray(input_data)
    ip_reshaped=np_array.reshape(1,-1)
    prediction=load_model.predict(ip_reshaped) 
    print(prediction)
    if(prediction[0]==0):
      return("The person is non diabetic")
    else:
      return("The person is diabetic")

def main():
    #title
    st.title('Diabetes prediction Web App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Number of Glucose')
    BP = st.text_input('Level of BP')
    SkinThickness=st.text_input('Value of SkinThickness')
    Insulin=st.text_input('Level of Insulin')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('DF Value')
    Age=st.text_input('Age of the person')

    #code for predicting 
    diagnosis = ""
    
    #creating button
    if st.button('Diabetes test result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()