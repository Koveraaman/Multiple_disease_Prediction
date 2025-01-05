import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Liver Disease Prediction',
                            'Kidney Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['hospital', 'file-medical', 'person'],
                           default_index=0)

# Load the model from GitHub
# Load the model from GitHub
MODEL_URLS = {
    "Parkinsons":"https://raw.githubusercontent.com/Koveraaman/Multiple_disease_Prediction/main/parkinsons_model.pkl",
    "Liver_disease": "https://raw.githubusercontent.com/Koveraaman/Multiple_disease_Prediction/main/liver_model.pkl",
    "Kidney_disease": "https://raw.githubusercontent.com/Koveraaman/Multiple_disease_Prediction/main/kidney_model.pkl"
}
@st.cache_resource
def load_model(model_name):
    response = requests.get(MODEL_URLS[model_name]) # Accessing a specific model URL
    response.raise_for_status()
    model = pickle.loads(response.content)
    return model

if selected == "Parkinsons Prediction":
    Parkinsons = load_model("Parkinsons")

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = Parkinsons.predict([user_input]) # Use the loaded model

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
  
elif selected == "Liver Disease Prediction":

    Liver_disease = load_model("Liver_disease")
    st.title("Liver Disease Prediction using ML")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Gender = st.text_input('Gender: 0 = Female, 1 = Male')
    with col3:
        Total_Bilirubin = st.text_input('Total_Bilirubin')
    with col4:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')
    with col1:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')
    with col2:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')
    with col3:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')
    with col4:
        Total_Protiens = st.text_input('Total_Protiens')
    with col1:
        Albumin = st.text_input('Albumin')
    with col2:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
        
    Liver_diagnosis = ''

    if st.button("Liver Test Result"):
        user1_input=[Age,Gender, Total_Bilirubin, Direct_Bilirubin,
                    Alkaline_Phosphotase, Alamine_Aminotransferase,
                    Aspartate_Aminotransferase, Total_Protiens, Albumin,
                    Albumin_and_Globulin_Ratio]
        user1_input = [float(x) for x in user1_input]
        #Liver_prediction = Liver_disease.predict([user1_input]) # Missing model definition
        # Placeholder prediction (replace with actual model prediction)
        Liver_prediction = [0] # Example prediction, replace with your model's prediction
        if Liver_prediction[0] == 1:
            Liver_diagnosis = "The person doesn't have Liver disease"
        else:
            Liver_diagnosis = "The person has Liver disease"
    st.success(Liver_diagnosis)

elif selected == "Kidney Disease Prediction":
    Kidney_disease = load_model("Kidney_disease")

    st.title("Kidney Disease Prediction using ML")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    #'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
    #'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad',
    #'appet', 'pe', 'ane'

    with col1:
        age = st.text_input('age')
    with col2:
        bp = st.text_input('bp')
    with col3:
        sg = st.text_input('sg')
    with col4:
        al = st.text_input('al')
    with col5:
        su = st.text_input('su')
    with col6:
        rbc = st.text_input('rbc')
    with col1:
        pc = st.text_input('pc')
    with col2:
        pcc = st.text_input('pcc') 
    with col3:
        ba = st.text_input('ba')
    with col4:
        bgr = st.text_input('bgr')
    with col5:
        bu = st.text_input('bu')
    with col6:
        sc = st.text_input('sc')

    
    Kidney_diagnosis = ''
    if st.button("Kidney Test Result"):
        user2_input=[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc]
        user2_input = [float(x) for x in user2_input]
        Kidney_prediction = Kidney_disease.predict([user2_input])
        if Kidney_prediction[0] == 1:
            Kidney_diagnosis = "The person doesn't have Kidney disease"
        else:
            Kidney_diagnosis = "The person has Kidney disease"
