import streamlit as st

st.set_page_config(page_title="Panel de Evaluación", layout="wide")

# Configuración de backend de Matplotlib
import matplotlib
matplotlib.use('Agg')  # Configurar un backend compatible con Streamlit
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
