import streamlit as st
import pickle

LABELS = {
    "0": r'10.00mL AA+ NR/PVA(2:8)',
    "1": r'10.10.00mL AA+ NR/PVA(6:4)',
    "2": r'10.00mL AA+ NR/PVA(8:2)',
    "3": r'10.00mL AA+ NR/PVA(9:1)',
    "4": r'6.00mL AA+ NR/PVA(2:8)',
    "5": r'6.00mL AA+ NR/PVA(6:4)',
    "6": r'6.00mL AA+ NR/PVA(8:2)',
    "7": r'6.00mL AA+ NR/PVA(9:1)',
    "8": r'8.00mL AA+ NR/PVA(2:8)',
    "9": r'8.00mL AA+ NR/PVA(6:4)',
    "10": r'8.00mL AA+ NR/PVA(8:2)',
    "11": r'8.00mL AA+ NR/PVA(9:1)',
    "12": r'F2',
    "13": r'F3',
    "14": r'F4',
    "15": r'F5',
}

model = pickle.load(open("xgb_classification.pkl", "rb"))

def predict_output(N,P,K,temperature,humidity,ph,rainfall,ReleaseRate):
    input_data = [[N,P,K,temperature,humidity,ph,rainfall,ReleaseRate]]
    prediction = model.predict(input_data)[0]
    prediction_label = LABELS[str(prediction)]
    return prediction_label

def main():
    st.title("ML Web App")

    st.header("Input Parameters")

    nitrogen = st.number_input("Nitrogen (kg/ hectare)")
    phosphorous = st.number_input("Phosphorous Content (kg/ hectare)")
    potassium = st.number_input("Potassium Content (kg/ hectare)")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    ph = st.number_input("Ph")
    rainfall = st.number_input("Rainfall")
    plant_grown = st.text_input("Plant Grown")
    release_rate = st.number_input("Release Rate")

    if st.button("Predict"):
        prediction = predict_output(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, release_rate)
        
        st.header("Prediction")
        st.write(prediction)

if __name__ == "__main__":
    main()
