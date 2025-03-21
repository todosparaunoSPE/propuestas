# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 09:10:09 2025

@author: jperezr
"""

import streamlit as st
import base64
import requests

# Función para descargar un archivo PDF desde una URL
def download_pdf(url):
    response = requests.get(url)
    return response.content

# Función para mostrar el PDF en pantalla completa
def show_pdf(pdf_content):
    base64_pdf = base64.b64encode(pdf_content).decode("utf-8")
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
En un entorno cada vez más competitivo y tecnológicamente avanzado, la innovación y la mejora continua se han convertido en pilares fundamentales para el éxito de las organizaciones. En este contexto, AFORE PENSIONISSSTE tiene la oportunidad de posicionarse como un referente en el sector financiero, no solo a través de la implementación de tecnologías de vanguardia, sino también mediante la adopción de una cultura organizacional que fomente la creatividad, la colaboración y el liderazgo proactivo.

Esta propuesta surge como resultado de un análisis exhaustivo de las necesidades actuales de la institución, así como de las tendencias globales en inteligencia artificial, gestión de calidad e innovación. A lo largo de este documento, se presentan estrategias y soluciones que no solo buscan optimizar los procesos internos y mejorar la experiencia del afiliado, sino que también están diseñadas para fortalecer la posición de AFORE PENSIONISSSTE como una institución líder en el sector.

Es importante destacar que la elaboración de esta propuesta ha requerido un esfuerzo colaborativo y multidisciplinario, en el que se han integrado conocimientos técnicos, experiencia operativa y una visión estratégica alineada con los objetivos institucionales. Este trabajo refleja no solo un compromiso con la excelencia, sino también una clara intención de contribuir al crecimiento y desarrollo de la organización, asegurando que cada iniciativa propuesta esté respaldada por un enfoque práctico y resultados medibles.

Con esta propuesta, se busca no solo impulsar la transformación tecnológica y operativa de AFORE PENSIONISSSTE, sino también reconocer y potenciar el talento interno que, con dedicación y visión, está dispuesto a asumir nuevos desafíos y responsabilidades para llevar a la institución hacia un futuro más competitivo y sostenible.
</div>
""", unsafe_allow_html=True)

# Sidebar para los botones y detalles adicionales
st.sidebar.header("Selecciona un PDF")

# URLs de los PDFs en GitHub (reemplaza con tus URLs reales)
pdf_urls = {
    "PDF 1": "https://pdfhost.io/v/ntKGBHFecn_propuesta_1",
    "PDF 2": "https://github.com/todosparaunoSPE/propuestas/blob/main/propuesta_2.pdf",
    "PDF 3": "https://github.com/todosparaunoSPE/propuestas/blob/main/propuesta_3.pdf"
}

# Botones para seleccionar el PDF
pdf_option = st.sidebar.radio("Selecciona un PDF:", list(pdf_urls.keys()))

# Contenedor para el PDF (inicialmente oculto)
pdf_container = st.empty()

# Botón para mostrar el PDF
if st.sidebar.button("Mostrar PDF"):
    pdf_url = pdf_urls[pdf_option]
    pdf_content = download_pdf(pdf_url)
    with pdf_container:
        show_pdf(pdf_content)

# Agregar tu nombre y copyright en el sidebar
st.sidebar.markdown("---")  # Separador visual
st.sidebar.markdown("**Desarrollado por:** Javier Horacio Pérez Ricárdez")
st.sidebar.markdown("**© 2024 Todos los derechos reservados**")
