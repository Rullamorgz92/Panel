import streamlit as st
import matplotlib
matplotlib.use('Agg')  # Configuración del backend
import matplotlib.pyplot as plt

st.title("Prueba de Matplotlib")

# Crear datos de prueba
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
