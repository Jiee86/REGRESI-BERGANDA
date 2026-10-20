import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model_harga_rumah.pkl')

st.title('Prediksi Harga Rumah')

luas = st.number_input('Luas rumah (m²)', min_value=10, value=150)
kamar = st.number_input('Jumlah kamar', min_value=1, value=3)
kamar_mandi = st.number_input('Jumlah kamar mandi', min_value=1, value=2)
usia = st.number_input('Usia rumah (tahun)', min_value=0, value=10)
jarak = st.number_input('Jarak dari pusat kota (km)', min_value=0.0, value=8.0)

if st.button('Prediksi'):
    data = pd.DataFrame(
        [[luas, kamar, kamar_mandi, usia, jarak]],
        columns=['luas_m2', 'kamar', 'kamar_mandi', 'usia_rumah', 'jarak_kota_km']
    )
    hasil = model.predict(data)[0]
    st.success(f'Perkiraan harga: Rp {hasil:,.0f} juta')