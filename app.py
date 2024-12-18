import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from joblib import load
import streamlit as st

# Import Model
model = load("model/xbcmodel.joblib")

columns_to_scale = [
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Age at enrollment",
]

feature = ["Debtor", "Scholarship holder", "Tuition fees up to date"]


# Function to preprocess input data
st.set_page_config(
    page_title="Prediksi Mahasiswa Dropout", page_icon="🏫", layout="wide"
)


def preprocess_data(df):
    processed_df = df.copy()

    # Perform label encoding for categorical columns
    categorical_cols = [
        "Debtor",
        "Scholarship holder",
        "Tuition fees up to date",
        "Application mode",
    ]
    label_encoder = LabelEncoder()
    for col in categorical_cols:
        if col in processed_df.columns:
            processed_df[col] = label_encoder.fit_transform(processed_df[col])

    # Perform Min-Max scaling for all columns
    mm_scaler = MinMaxScaler()
    processed_df[processed_df.columns] = mm_scaler.fit_transform(processed_df)

    return processed_df


def preprocessor(input_df):
    # Preprocess categorical and numerical columns separately
    input_df = preprocess_data(input_df)
    return input_df


# Streamlit app
def main():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://github.com/muhammadsahrul59/student-performance-dashboard/blob/main/images/logo-cute.png?raw=true",
            width=130,
        )
    with col2:
        st.header("Kiyut Institute")
        st.header("Student Dropout Predictor")

    # Input form
    st.subheader("Masukkan Informasi Mahasiswa:")

    input_data = {}  # Dictionary to store user input data
    col1, col2 = st.columns(2)  # Split the interface into two columns

    with col1:
        # Collect user inputs for country and some financial indicators
        input_data["Debtor"] = st.radio("Pilih Debtor:", ["Tidak", "Ya"])
        input_data["Scholarship holder"] = st.radio(
            "Pilih Scholarship holder:", ["Tidak", "Ya"]
        )
        input_data["Tuition fees up to date"] = st.radio(
            "Pilih Tuition fees up to date:", ["Tidak", "Ya"]
        )
        input_data["Application mode"] = st.selectbox(
            "Application mode:",
            [
                "2nd phase - general contingent" "International student (bachelor)",
                "1st phase - general contingent",
                "Over 23 years old",
                "3rd phase - general contingent",
                "Short cycle diploma holders",
                "Technological specialization diploma holders",
                "Change of institution/course",
                "Change of course",
                "Holders of other higher courses",
                "Transfer",
                "1st phase - special contingent (Madeira Island)",
                "1st phase - special contingent (Azores Island)",
                "Ordinance No. 612/93",
                "Ordinance No. 854-B/99",
                "Change of institution/course (International)",
                "Ordinance No. 533-A/99, item b2 (Different Plan)",
                "Ordinance No. 533-A/99, item b3 (Other Institution)",
            ],
        )

    with col2:
        input_data["Age at enrollment"] = st.number_input("Umur", step=1)
        input_data["Curricular units 1st sem (approved)"] = st.number_input(
            "Menyetujui Mata Kuliah Semester Pertama: ", step=1
        )
        input_data["Curricular units 1st sem (grade)"] = st.number_input(
            "Nilai Semester 1: ", step=1
        )
        input_data["Curricular units 2nd sem (approved)"] = st.number_input(
            "Menyetujui Unit Mata Kuliah Semester Pertama: ", step=1
        )
        input_data["Curricular units 2nd sem (grade)"] = st.number_input(
            "Nilai Semester 2: ", step=1
        )
        # inputs = {}

        # for column in columns_to_scale:
        # inputs[column] = st.number_input(f"{column}:", value=0.0, min_value=0.0, max_value=100.0, step=1.0)

    input_df = pd.DataFrame([input_data])  # Convert collected data into a DataFrame

    if st.button("Prediksi"):  # When the 'Predict' button is clicked
        final_df = preprocessor(input_df)  # Preprocess the collected data
        prediction = model.predict(final_df)[0]  # Use the model to predict the outcome

        # Display the prediction result
        if prediction == 1:
            st.write("Graduate")
        elif prediction == 0:
            st.write("Dropout")


if __name__ == "__main__":
    main()
