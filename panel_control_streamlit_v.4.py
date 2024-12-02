# Debe estar antes de cualquier otra cosa
import streamlit as st

st.set_page_config(page_title="Panel de Evaluación", layout="wide")  # Debe ser la primera línea ejecutable

# Luego el resto de las importaciones y el código
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data():
    return pd.read_excel("Informe_Ejecutivosv.10.xlsx")

df = load_data()

# Renombrar columnas para mayor claridad
df.rename(columns={'Nombre': 'Ejecutivo', 'Contacto': 'Nota Contacto', 'Reunión': 'Nota Reunión'}, inplace=True)

# Título de la aplicación
st.title("Panel Interactivo de Evaluación de Ejecutivos")

# Sidebar para filtros
st.sidebar.header("Filtros")
selected_supervisor = st.sidebar.selectbox("Seleccione un Supervisor", df['Supervisor'].unique())
filtered_executives = df[df['Supervisor'] == selected_supervisor]['Ejecutivo'].unique()
selected_executive = st.sidebar.selectbox("Seleccione un Ejecutivo", filtered_executives)

# Código restante...
