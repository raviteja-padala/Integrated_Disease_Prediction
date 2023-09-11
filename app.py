import streamlit as st
import pickle

# Load the pickled models
with open('models/model__heart.sav', 'rb') as model_file:
    heart_model = pickle.load(model_file)

with open('models/model_liver.sav', 'rb') as model_file:
    liver_model = pickle.load(model_file)

with open('models/model_kidney.sav', 'rb') as model_file:
    kidney_model = pickle.load(model_file)

import streamlit as st

# Define a custom CSS style to center the title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the centered title
st.markdown("<h1 class='title'>Integrated Disease Prediction</h1>", unsafe_allow_html=True)

# Define the Streamlit app
def main():
    #st.title("Integrated Disease Prediction")
    
    # Dropdown to select disease type
    disease_type = st.selectbox("Select Disease Type:", ["Heart Disease", "Liver Disease", "Kidney Disease"])
    
    # Form to input attributes
    st.subheader(f"{disease_type} Prediction")
    
    if disease_type == 'Heart Disease':
        st.subheader('Enter Heart Disease Attributes:')
        age = st.number_input('Age', min_value=0, value=40, max_value=100)
        sex = st.radio('Sex', ['Male', 'Female'])
        chest_pain_type = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure',min_value=0.0)
        chol = st.number_input('Serum Cholestoral',min_value=0)
        fbs = st.radio('Is Fasting Blood Sugar > 120 mg/dl?', ['No', 'Yes'])
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'Abnormal ST-T wave', 'probable left ventricular hypertrophy'])
        thalach = st.number_input('Maximum Heart Rate Achieved')
        exang = st.radio('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise',min_value=0)
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.selectbox('Colored Blood Vessels Post Fluoroscopy', ['0', '1', '2', '3'])
        thal = st.selectbox('Results of Thallium Stress Test', ['Normal', 'Fixed Defect', 'Reversible Defect'])

        if st.button('Predict Heart Disease'):
            if any([age == 0, sex == '', chest_pain_type == '', trestbps == 0, chol == 0, fbs == '', restecg == '', thalach == 0, exang == '',  slope == '', ca == '', thal == '']):
                st.warning("Please enter values for all attributes.")
            else:
                # Prepare input data
                sex_value = 0 if sex == 'Male' else 1
                # Map chest pain type to numerical values
                cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3}
                cp = cp_mapping[chest_pain_type]
                fbs_value = 0 if fbs == 'No' else 1
                # Map restecg to numerical values
                restecg_mapping = {'Normal': 0, 'Abnormal ST-T wave': 1, 'probable left ventricular hypertrophy': 2}
                restecg_value = restecg_mapping[restecg]
                exang_value = 0 if exang == 'No' else 1
                # Map slope to numerical values
                slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
                slope_value = slope_mapping[slope]
                # Map thal to numerical values
                thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
                thal_value = thal_mapping[thal]

                heart_attributes = [age, sex_value, cp, trestbps, chol, fbs_value, restecg_value, thalach, exang_value, oldpeak, slope_value, ca, thal_value]
                prediction = heart_model.predict([heart_attributes])
                disease_name = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'

                st.subheader(f"Model prediction:")
                st.subheader(f"The diagnosis is Positive for {disease_name}." if prediction[0] == 1 else f"Model prediction: The diagnosis is Negative, {disease_name}")

                #st.write(f"Model prediction: The diagnosis is Positive for {disease_name}." if prediction[0] == 1 else f"Model prediction: The diagnosis is Negative , {disease_name}")


    elif disease_type == "Liver Disease":
        st.subheader('Enter Liver Disease Attributes:')
        age = st.number_input('Age', min_value=0, value=40, max_value=100)
        gender = st.radio('Gender', ['Male', 'Female'])
        total_bilirubin = st.number_input('Total Bilirubin',min_value = 0.0)
        direct_bilirubin = st.number_input('Direct Bilirubin',min_value=0.0)
        alkaline_phosphotase = st.number_input('Alkaline Phosphotase',min_value=0)
        alamine_aminotransferase = st.number_input('Alamine Aminotransferase',min_value=0)
        aspartate_aminotransferase = st.number_input('Aspartate Aminotransferase',min_value=0)
        total_protiens = st.number_input('Total Protiens',min_value=0.0)
        albumin = st.number_input('Albumin',min_value=0)
        albumin_and_globulin_ratio = st.number_input('Albumin and Globulin Ratio',min_value=0.0)

        if st.button('Predict Liver Disease'):
            if any([age == 0, gender == '', total_bilirubin == 0.0, direct_bilirubin == 0.0, alkaline_phosphotase == 0, alamine_aminotransferase == 0, aspartate_aminotransferase == 0, total_protiens == 0.0, albumin == 0, albumin_and_globulin_ratio == 0.0]):
                st.warning("Please enter values for all attributes.")
            else:
                # Prepare input data
                gender_value = 0 if gender == 'Male' else 1

                liver_attributes = [age, gender_value, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase, total_protiens, albumin, albumin_and_globulin_ratio]
                prediction = liver_model.predict([liver_attributes])
                disease_name = 'Liver Disease' if prediction[0] == 1 else 'No Liver Disease'
                st.write(f"Model prediction: The diagnosis is Positive for {disease_name}." if prediction[0] == 1 else f"Model prediction: The diagnosis is Negative for {disease_name}")

    elif disease_type == "Kidney Disease":
        st.subheader('Enter Kidney Disease Attributes:')
        age = st.number_input('Age', min_value=0, value=40, max_value=100)
        blood_pressure = st.number_input('Blood Pressure', min_value=0)
        specific_gravity = st.number_input('Specific Gravity', min_value=0.0)
        albumin = st.number_input('Albumin', min_value=0)
        sugar = st.number_input('Sugar', min_value=0)
        blood_glucose_random = st.number_input('Blood_Glucose_Random', min_value=0)
        blood_urea = st.number_input('Blood_urea', min_value=0)
        serum_creatinine = st.number_input('Serum_creatinine', min_value=0.0)
        sodium = st.number_input('Sodium', min_value=0)
        potassium = st.number_input('Potassium', min_value=0.0)
        haemoglobin = st.number_input('Haemoglobin', min_value=0.0)
        packed_cell_volume = st.number_input('Packed_cell_volume', min_value=0)
        white_blood_cell_count = st.number_input('White_blood_cell_count', min_value=0)
        red_blood_cell_count = st.number_input('Red_Blood_cell_count', min_value=0.0)

        # One-hot encode categorical variables using selectbox
        st.subheader('Select Categorical Attributes:')
        red_blood_cells = st.selectbox('Red Blood Cells', ['normal', 'abnormal'])
        pus_cell = st.selectbox('Pus Cell', ['normal', 'abnormal'])
        pus_cell_clumps = st.selectbox('Pus Cell Clumps', ['notpresent', 'present'])
        bacteria = st.selectbox('Bacteria', ['notpresent', 'present'])
        hypertension = st.selectbox('Hypertension', ['yes', 'no'])
        diabetes_mellitus = st.selectbox('Diabetes Mellitus', ['yes', 'no'])
        coronary_artery_disease = st.selectbox('Coronary Artery Disease', ['no', 'yes'])
        appetite = st.selectbox('Appetite', ['good', 'poor'])
        pedal_edema = st.selectbox('Pedal Edema', ['no', 'yes'])
        aanemia = st.selectbox('Aanemia', ['no', 'yes'])

        if st.button('Predict Kidney Disease'):
             if any([
                age == 0, blood_pressure == 0, specific_gravity == 0.0, albumin == 0, sugar == 0, blood_glucose_random == 0,
                blood_urea == 0, serum_creatinine == 0.0, sodium == 0, potassium == 0.0, haemoglobin == 0.0,
                packed_cell_volume == 0, white_blood_cell_count == 0, red_blood_cell_count == 0.0
        ]) or any([
                red_blood_cells == '', pus_cell == '', pus_cell_clumps == '', bacteria == '', hypertension == '',
                diabetes_mellitus == '', coronary_artery_disease == '', appetite == '', pedal_edema == '', aanemia == ''
        ]):
                 st.warning("Please enter values for all attributes.")
        
             else:
                # One-hot encode categorical attributes
                red_blood_cells_encoded = 1 if red_blood_cells == 'abnormal' else 0
                pus_cell_encoded = 1 if pus_cell == 'abnormal' else 0
                pus_cell_clumps_encoded = 1 if pus_cell_clumps == 'present' else 0
                bacteria_encoded = 1 if bacteria == 'present' else 0
                hypertension_encoded = 1 if hypertension == 'yes' else 0
                diabetes_mellitus_encoded = 1 if diabetes_mellitus == 'yes' else 0
                coronary_artery_disease_encoded = 1 if coronary_artery_disease == 'yes' else 0
                appetite_encoded = 1 if appetite == 'poor' else 0
                pedal_edema_encoded = 1 if pedal_edema == 'yes' else 0
                aanemia_encoded = 1 if aanemia == 'yes' else 0

                # Prepare input data
                kidney_attributes = [
                    age, blood_pressure, specific_gravity, albumin, sugar, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
                    red_blood_cells_encoded, pus_cell_encoded, pus_cell_clumps_encoded, bacteria_encoded,
                    hypertension_encoded, diabetes_mellitus_encoded, coronary_artery_disease_encoded,
                    appetite_encoded, pedal_edema_encoded, aanemia_encoded
                ]

                prediction = kidney_model.predict([kidney_attributes])
                disease_name = 'Chronic Kidney Disease' if prediction[0] == 1 else 'No Chronic Kidney Disease'
                st.write(f"Model prediction: The diagnosis is Positive for {disease_name}." if prediction[0] == 1 else f"Model prediction: The diagnosis is Negative, {disease_name}")

if __name__ == '__main__':
    main()
