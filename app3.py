# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 09:10:09 2025

@author: jperezr
"""

import streamlit as st
import base64
import os  # Para verificar si los archivos existen

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background:
    radial-gradient(black 15%, transparent 16%) 0 0,
    radial-gradient(black 15%, transparent 16%) 8px 8px,
    radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
    radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
    background-color:#282828;
    background-size:16px 16px;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Función para mostrar el PDF
def show_pdf(pdf_file):
    if not os.path.exists(pdf_file):
        st.error(f"Error: No se encontró el archivo `{pdf_file}`.")
        return
    
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    
    # PDF en pantalla completa
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900px" type="application/pdf"></iframe>
    """
    
    st.markdown(pdf_display, unsafe_allow_html=True)

# Título de la aplicación
st.title("Visualizador de Propuestas para AFORE PENSIONISSSTE")

# Introducción con texto justificado y tamaño de letra más grande
st.markdown("""
<style>
.intro-text {
    text-align: justify;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.header("Introducción")
st.markdown("""
<div class="intro-text">
En un entorno cada vez más competitivo y tecnológicamente avanzado, la innovación y la mejora continua se han convertido en pilares fundamentales para el éxito de las organizaciones...
</div>
""", unsafe_allow_html=True)

# Sidebar para los botones y detalles adicionales
st.sidebar.header("Selecciona un PDF")

# Opciones en el sidebar
pdf_option = st.sidebar.radio("Selecciona un PDF:", {
    "PDF 1": "propuesta_1.pdf",
    "PDF 2": "propuesta_2.pdf",
    "PDF 3": "propuesta_3.pdf"
})

# Botón para mostrar el PDF
if st.sidebar.button("Mostrar PDF"):
    show_pdf(pdf_option)

# Agregar tu nombre y copyright en el sidebar
st.sidebar.markdown("---")  
st.sidebar.markdown("**Desarrollado por:** Javier Horacio Pérez Ricárdez")
st.sidebar.markdown("**© 2024 Todos los derechos reservados**")
