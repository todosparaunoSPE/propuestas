import streamlit as st

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

# URLs de los PDFs en GitHub (reemplaza con tus URLs reales)
pdf_urls = {
    "PDF 1": "https://pdfhost.io/v/ntKGBHFecn_propuesta_1",
    "PDF 2": "https://github.com/todosparaunoSPE/propuestas/blob/main/propuesta_2.pdf",
    "PDF 3": "https://github.com/todosparaunoSPE/propuestas/blob/main/propuesta_3.pdf"
}

# Botones para abrir el PDF en una nueva pestaña
for pdf_name, pdf_url in pdf_urls.items():
    if st.sidebar.button(f"Abrir {pdf_name}"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={pdf_url}">', unsafe_allow_html=True)

# Agregar tu nombre y copyright en el sidebar
st.sidebar.markdown("---")  # Separador visual
st.sidebar.markdown("**Desarrollado por:** Javier Horacio Pérez Ricárdez")
st.sidebar.markdown("**© 2024 Todos los derechos reservados**")
