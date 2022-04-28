


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn import datasets
#from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier12.pkl","rb")
classifier=pickle.load(pickle_in)

#df=pd.read_csv("C://Users//visha//Desktop//MajorProject//Bank Note")
#st.line_chart(df)


#@app.route('/')
def welcome():
    return "Welcome All"
 
dataset_name=st.sidebar.selectbox(  'Select Dataset',('BankNote_Authentication','None'))
classifier_name=st.sidebar.selectbox("select Classifier",("RandomForest","SVM","LogisticRegression"))





#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    

   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    #st.write("""#   Bank Authenticator""")
   # st.title("           ")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;"> Bank Authenticator </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance")
    
        
    skewness = st.text_input("Skewness")
    curtosis = st.text_input("Curtosis")
    entropy = st.text_input("Entropy")
    result=""
    


    st.text("")
    st.text("")

    
    if st.button("Predict"):
        if variance.isdigit():
         pass
        else:
         print("type numeric value only")
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 0:
            st.error('The Banknotes are Forged ⚔️')
        else:

            st.success('The Banknotes are Genuine ✔️')
            # st.success('The output is {}'.format(result))
    if st.button("About"):

        st.text("Built with Streamlit")
        st.text("Vishal")

if __name__=='__main__':
    main()
    
if classifier_name=="RandomForest":
    st.write(" Classifier name: RandomForest")
    st.write(" Accuracy score: 0.9967213114754099")
elif classifier_name=="SVM":
     st.write(" Classifier name :" "SVM")
     st.write(" Accuracy score: 0.7114754098360656")
elif classifier_name=="LogisticRegression":
    st.write(" Classifier name:" "LogisticRegression")
    st.write(""" Accuracy score: 0.9901639344262295""")

    
    
