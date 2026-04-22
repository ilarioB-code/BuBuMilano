import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configurazione pagina
st.set_page_config(page_title="Nautical Design Research - MDW 2026", layout="wide")

st.title("🛥️ Ricerca Nautica: MDW 2026")
st.subheader("Itinerario Esclusivo - 23 Aprile")

# 1. Database delle tappe
data = {
    'Nome': ['glo™ for art', 'Boffi Solferino', 'Grand Seiko', 'Sara Ricciardi (ALMA)', 'Poltrona Frau', 'Statale (INTERNI)'],
    'Lat': [45.4795, 45.4746, 45.4715, 45.4628, 45.4695, 45.4608],
    'Lon': [9.1874, 9.1865, 9.1860, 9.1720, 9.1915, 9.1945],
    'Area': ['Brera', 'Brera', 'Brera', '5VIE', 'Manzoni', 'Statale'],
    'Focus': ['Luce/Colore', 'Cucina Tecnica', 'Precisione', 'Acustica/Acqua', 'Pelle/Touch', 'Modularità']
}
df = pd.DataFrame(data)

# 2. Sidebar per filtri
st.sidebar.header("Filtra per Area")
area_choice = st.sidebar.multiselect("Scegli zona:", df['Area'].unique(), default=df['Area'].unique())
filtered_df = df[df['Area'].isin(area_choice)]

# 3. Mappa Interattiva
st.write("### 📍 Mappa delle Installazioni")
# Centra la mappa su Milano
m = folium.Map(location=[45.468, 9.185], zoom_start=14)

for i, row in filtered_df.iterrows():
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"<b>{row['Nome']}</b><br>{row['Focus']}",
        tooltip=row['Nome'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

st_folium(m, width=700, height=450)

# 4. Schede di Dettaglio
st.write("---")
st.write("### 📝 Dettagli Tappe e Obiettivi Nautici")

for i, row in filtered_df.iterrows():
    with st.expander(f"{row['Nome']} ({row['Area']})"):
        st.write(f"**Focus Design:** {row['Focus']}")
        st.info("💡 **Spunto Nautico:** Analizzare la traduzione di questo concept per interni di yacht o beach club.")
        # Spazio per i commenti del team
        st.text_input(f"Note dal campo per {row['Nome']}:", key=f"note_{i}")
