import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configurazione pagina
st.set_page_config(page_title="MDW 2026 - Nautical Research", layout="wide")

st.title("🛥️ Nautical Design Research: MDW 2026")
st.subheader("Database Tappe Aggiornato (23-24 Aprile)")

# Database esteso dal documento PDF [cite: 1-59]
data = {
    'Nome': [
        'Mediateca Santa Teresa (Yinka Ilori)', 'Loro Piana (Cortile della Seta)', 'Boffi & Salvatori', 
        'Modulnova (Artistry)', 'Gessi & Grand Seiko', 'Orto Botanico (Annabel Karim Kassar)', 
        'Pinacoteca (Serotonin)', 'Palazzo Clerici', 'Appartamento Spagnolo', 
        'Signature Kitchen Suite', 'Tenoha Milano', 'Magna Pars (FIAT)', 
        'Superstudio Più (Lexus/Samsung)', 'Opificio 31 (IQOS/Devialet)', 'Palazzo Litta (Metamorphosis)', 
        'Le Cavallerizze (Alma Water)', 'Hub 5VIE (Vessels)', 'SIAM (Teatro alla Scala)', 
        'Palazzo Tomasi (Buccellati)', 'La Boiserie (David/Nicolas)', 'Fabbrica Sassetti', 
        'Copernico Isola (S32)', 'Stecca 3.0'
    ],
    'Lat': [
        45.4746, 45.4735, 45.4746, 45.4765, 45.4725, 45.4718, 
        45.4715, 45.4678, 45.4780, 45.4705, 45.4520, 45.4515, 
        45.4505, 45.4510, 45.4665, 45.4628, 45.4635, 45.4645, 
        45.4620, 45.4630, 45.4875, 45.4880, 45.4865
    ],
    'Lon': [
        9.1880, 9.1890, 9.1865, 9.1855, 9.1845, 9.1895, 
        9.1885, 9.1858, 9.1840, 9.1910, 9.1710, 9.1705, 
        9.1700, 9.1715, 9.1795, 9.1720, 9.1815, 9.1825, 
        45.4625, 9.1810, 9.1865, 9.1875, 9.1885
    ],
    'Area': [
        'Brera', 'Brera', 'Brera', 'Brera', 'Brera', 'Brera', 
        'Brera', 'Brera', 'Brera', 'Brera', 'Tortona', 'Tortona', 
        'Tortona', 'Tortona', '5Vie', '5Vie', '5Vie', '5Vie', 
        '5Vie', '5Vie', 'Isola', 'Isola', 'Isola'
    ],
    'Descrizione': [
        'Installazione Clicquot Café. [cite: 2]', 'Installazione tessile nel Cortile della Seta. ', 'Showroom storici e design di lusso. [cite: 4]',
        'Installazione "Artistry" su modularità. [cite: 5]', 'Esperienze immersive e "The Nature of Time". ', 'Installazione sensoriale all\'aperto. [cite: 8]',
        'Installazione "Serotonin" di Sara Ricciardi. [cite: 9]', 'Installazioni in sale affrescate. [cite: 11]', 'Focus sull\'interior design iberico. ',
        'Tecnologia e food-design. [cite: 13]', 'Design giapponese minimalista. ', 'Installazione "CIAO FUTURO!". [cite: 16]',
        'Hub tecnologico SuperNova e Lexus. ', 'Audio high-end e architettura. [cite: 18]', 'Labirinto rosa nel cortile d\'onore. [cite: 27, 28]',
        'Alma Water - La stanza del mare (Immersiva). [cite: 30, 31]', 'Vessels of the Intangible - Memoria e sensi. [cite: 34, 37]', 'Scenografia teatrale applicata al design. [cite: 38, 39]',
        'Aquae Mirabiles - Acqua e alta gioielleria. [cite: 41, 42]', 'Linguaggio architettonico immersivo. [cite: 47, 48]', 'Hub materiali sostenibili e design gallery. [cite: 50, 51]',
        'Domotica e futuro degli spazi di lavoro. [cite: 52]', 'Laboratorio rigenerazione materiali e scarti. [cite: 57, 58]'
    ],
    'Target_Nautico': [
        'Socialità e colori accesi per aree deck.', 'Tessuti di lusso resistenti per interni.', 'Standard qualitativo per galley e bagni.',
        'Sistemi di stivaggio e cucina modulare.', 'Precisione e illuminazione zen.', 'Integrazione del verde e materiali naturali.',
        'Effetti sensoriali per cabine VIP.', 'Contrasto tra storico e ultra-moderno.', 'Trend arredo internazionale.',
        'Elettrodomestici smart a scomparsa.', 'Minimalismo per spazi ridotti.', 'Materiali automotive traslabili.',
        'Interfacce utente e superfici hi-tech.', 'Integrazione sistemi audio di alta gamma.', 'Gestione flussi e volumi complessi.',
        'Sound design e relax legato all\'acqua.', 'Oggettistica di pregio e illuminazione mood.', 'Scenografia di bordo per eventi.',
        'Dettagli preziosi e lavorazione dei metalli.', 'Evoluzione delle pannellature in legno.', 'Materiali compositi sostenibili.',
        'Domotica integrata e ufficio a bordo.', 'Economia circolare: mobili da scarti plastici.'
    ]
}

df = pd.DataFrame(data)

# Sidebar
st.sidebar.title("📅 Date: 23-24 Aprile")
st.sidebar.info("Tutte le installazioni sono accessibili in entrambe le date (salvo eventi privati).")
area_choice = st.sidebar.multiselect("Filtra per Distretto:", df['Area'].unique(), default=['Brera', '5Vie'])

# Filtro dati
filtered_df = df[df['Area'].isin(area_choice)]

# Mappa
st.write("### 📍 Mappa Interattiva MDW")
m = folium.Map(location=[45.468, 9.185], zoom_start=14)
for i, row in filtered_df.iterrows():
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"<b>{row['Nome']}</b><br>{row['Descrizione']}",
        tooltip=row['Nome']
    ).add_to(m)
st_folium(m, width=900, height=500)

# Elenco dettagliato
st.write("---")
st.write("### 🔍 Schede di Ricerca sul Campo")
for i, row in filtered_df.iterrows():
    with st.expander(f"📍 {row['Area']} - {row['Nome']}"):
        st.write(f"**Descrizione:** {row['Descrizione']}")
        st.success(f"⚓ **Opportunità Nautica:** {row['Target_Nautico']}")
        st.text_area("Note del team (osservazioni su materiali/luci):", key=f"note_{i}")
