import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import base64
import os
from datetime import datetime, timedelta

# ==========================================
# 1. KONFIGURACJA STRONY I STANU APLIKACJI
# ==========================================
st.set_page_config(
    page_title="Vorteza Systems | Architektura B2B",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicjalizacja stanu sesji dla interaktywnych elementów
if 'demo_clicks' not in st.session_state:
    st.session_state.demo_clicks = 0

# ==========================================
# 2. FUNKCJE POMOCNICZE (TŁO I DANE)
# ==========================================
def get_base64_of_bin_file(bin_file):
    """Konwertuje plik binarny (np. obraz) do stringa base64."""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    """Ustawia obraz tła z kinowym filtrem maskującym."""
    if os.path.exists(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: 
                linear-gradient(to right, rgba(11,33,63,0.15) 0%, rgba(11,33,63,0.6) 100%),
                url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Generowanie tła
set_background('background.jpg')

def generate_mock_logistics_data():
    """Generuje sztuczne dane do dema analitycznego Vorteza Hub."""
    np.random.seed(42)
    dates = pd.date_range(end=datetime.today(), periods=30)
    data = {
        'Data': dates,
        'Zlecenia_Stali': np.random.randint(20, 50, size=30),
        'Zlecenia_Gielda': np.random.randint(5, 25, size=30),
        'Czas_Obslugi_Minuty': np.random.uniform(4.5, 12.0, size=30)
    }
    df = pd.DataFrame(data)
    df['Suma_Zlecen'] = df['Zlecenia_Stali'] + df['Zlecenia_Gielda']
    # Symulacja trendu spadkowego dla czasu obsługi (dowód na optymalizację)
    df['Czas_Obslugi_Minuty'] = df['Czas_Obslugi_Minuty'] - (np.arange(30) * 0.1)
    return df

# ==========================================
# 3. ZAAWANSOWANY CSS (DARK GLASSMORPHISM PRO)
# ==========================================
st.markdown("""
    <style>
    /* Reset & Podstawy */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    .stApp { font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1300px; }
    
    /* Zmienne kolorystyczne */
    :root {
        --glass-bg: rgba(15, 23, 42, 0.75);
        --glass-border: rgba(255, 255, 255, 0.1);
        --gold-primary: #bda886;
        --gold-hover: #e0cca7;
        --text-main: #ffffff;
        --text-muted: #94a3b8;
    }
    
    /* GLASSMORPHISM - WSPÓLNA KLASA */
    .glass-panel {
        background: var(--glass-bg);
        backdrop-filter: blur(20px) saturate(120%);
        -webkit-backdrop-filter: blur(20px) saturate(120%);
        border-radius: 20px;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
        border: 1px solid var(--glass-border);
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        color: var(--text-main);
        transition: transform 0.4s ease, box-shadow 0.4s ease, border 0.4s ease;
    }
    .glass-panel:hover {
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.7);
        border: 1px solid rgba(189, 168, 134, 0.3);
    }
    
    /* HERO SECTION */
    .hero-container {
        padding: 7rem 4rem;
        text-align: center;
        margin: 2rem auto 6rem auto;
        position: relative;
        overflow: hidden;
    }
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 1.5rem;
        line-height: 1.1;
        text-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    .hero-accent {
        background: linear-gradient(135deg, #bda886 0%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        max-width: 800px;
        margin: 0 auto 3rem auto;
        line-height: 1.8;
        color: #cbd5e1;
        font-weight: 300;
    }
    
    /* PRZYCISKI */
    .btn-gold {
        background: linear-gradient(135deg, var(--gold-primary) 0%, #9e8a69 100%);
        color: #0b213f !important;
        padding: 16px 45px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 900;
        font-size: 1.15rem;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
        box-shadow: 0 10px 25px rgba(189, 168, 134, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .btn-gold:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 15px 35px rgba(189, 168, 134, 0.6);
        color: #000000 !important;
    }
    
    /* NAGŁÓWKI SEKCJI (BADGE STYLE) */
    .section-header-wrapper { text-align: center; margin: 6rem 0 4rem 0; }
    .section-header {
        display: inline-block;
        background: rgba(15, 23, 42, 0.9);
        padding: 12px 35px;
        border-radius: 50px;
        color: var(--gold-primary);
        font-size: 1.4rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 4px;
        border: 1px solid rgba(189, 168, 134, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }
    
    /* KARTY FILARÓW */
    .pillar-card {
        padding: 3rem 2.5rem;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .pillar-icon { font-size: 3.5rem; margin-bottom: 1.5rem; }
    .pillar-title { font-weight: 900; font-size: 1.8rem; margin-bottom: 1rem; }
    .pillar-desc { line-height: 1.7; font-size: 1.05rem; color: var(--text-muted); }
    
    /* OŚ CZASU (TIMELINE) */
    .timeline-container { position: relative; max-width: 900px; margin: 0 auto; padding: 2rem 0; }
    .timeline-container::after {
        content: ''; position: absolute; width: 2px; background: rgba(189, 168, 134, 0.3);
        top: 0; bottom: 0; left: 50%; margin-left: -1px;
    }
    .timeline-item { padding: 10px 40px; position: relative; background-color: inherit; width: 50%; }
    .timeline-left { left: 0; text-align: right; }
    .timeline-right { left: 50%; text-align: left; }
    .timeline-dot {
        position: absolute; width: 20px; height: 20px; right: -10px; background-color: var(--gold-primary);
        border: 4px solid #0f172a; top: 15px; border-radius: 50%; z-index: 1; box-shadow: 0 0 10px rgba(189,168,134,0.5);
    }
    .timeline-right .timeline-dot { left: -10px; }
    .timeline-content {
        padding: 1.5rem; background: rgba(15, 23, 42, 0.6); border-radius: 15px;
        border: 1px solid var(--glass-border); display: inline-block; width: 100%;
    }
    .timeline-date { color: var(--gold-primary); font-weight: 800; font-size: 0.9rem; margin-bottom: 0.5rem; letter-spacing: 1px;}
    .timeline-title { font-weight: 800; font-size: 1.2rem; color: #fff; margin-bottom: 0.5rem; }
    
    /* STREAMLIT TABS OVERRIDE */
    div[data-baseweb="tabs"] { width: 100%; }
    div[data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 20px 20px 0 0;
        padding: 1rem 2rem 0 2rem;
        border: 1px solid var(--glass-border);
        border-bottom: 1px solid rgba(189, 168, 134, 0.4);
        gap: 30px;
    }
    div[data-baseweb="tab-panel"] {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        border-radius: 0 0 20px 20px;
        padding: 3rem;
        border: 1px solid var(--glass-border);
        border-top: none;
        color: var(--text-main);
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: transparent; border-radius: 0;
        color: #64748b; font-weight: 800; font-size: 1.1rem; border-bottom: 3px solid transparent;
    }
    .stTabs [data-baseweb="tab"]:hover { color: #ffffff; }
    .stTabs [aria-selected="true"] { color: var(--gold-primary) !important; border-bottom: 3px solid var(--gold-primary) !important; }
    
    /* Klawisze i Inputy Streamlit wewnątrz kontenerów */
    .stNumberInput > div > div > input { color: white !important; }
    .stSelectbox > div > div > div { color: white !important; }
    
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. HERO SECTION
# ==========================================
st.markdown("""
    <div class="glass-panel hero-container">
        <div style="font-size: 1rem; color: #bda886; font-weight: bold; letter-spacing: 3px; margin-bottom: 1rem; text-transform: uppercase;">
            Autorski Ekosystem Oprogramowania
        </div>
        <h1 class="hero-title">Praktyka operacyjna.<br><span class="hero-accent">Przekuta w twardy kod.</span></h1>
        <p class="hero-subtitle">
            Nazywam się Piotr Dukiel. Tworzę oprogramowanie B2B, które nie zgaduje problemów biznesu, 
            lecz wynika z lat doświadczeń na pierwszej linii frontu logistycznego. Od automatyzacji 
            flot transportowych, po rygorystyczne przepływy danych w kancelariach i medycynie.
        </p>
        <a href="#architektura-rozwiazan" class="btn-gold">Zbadaj Architekturę</a>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. O ARCHITEKCIE (TIMELINE)
# ==========================================
st.markdown("<div class='section-header-wrapper'><div class='section-header'>Droga do Vorteza Systems</div></div>", unsafe_allow_html=True)

timeline_html = """
<div class="timeline-container">
    <div class="timeline-item timeline-left">
        <div class="timeline-dot"></div>
        <div class="timeline-content glass-panel" style="box-shadow: none;">
            <div class="timeline-date">EDUKACJA I FUNDAMENTY</div>
            <div class="timeline-title">Uniwersytet Szczeciński</div>
            <div class="pillar-desc" style="font-size:0.95rem;">
                Solidne podstawy akademickie, które ukształtowały analityczne podejście do rozwiązywania problemów i optymalizacji procesów. Początek ścieżki zawodowej.
            </div>
        </div>
    </div>
    <div class="timeline-item timeline-right">
        <div class="timeline-dot"></div>
        <div class="timeline-content glass-panel" style="box-shadow: none;">
            <div class="timeline-date">ZROZUMIENIE BIZNESU</div>
            <div class="timeline-title">Senior Logistics Specialist</div>
            <div class="pillar-desc" style="font-size:0.95rem;">
                Lata praktyki w SQM Prosta Spółka Akcyjna (Komorniki). Zarządzanie złożonymi łańcuchami dostaw, eventami międzynarodowymi i współpracą z Przewoźnikami Stałymi oraz Giełdowymi.
            </div>
        </div>
    </div>
    <div class="timeline-item timeline-left">
        <div class="timeline-dot"></div>
        <div class="timeline-content glass-panel" style="box-shadow: none;">
            <div class="timeline-date">TECHNOLOGIA</div>
            <div class="timeline-title">Python, Streamlit & GitHub</div>
            <div class="pillar-desc" style="font-size:0.95rem;">
                Przejście od analizowania wąskich gardeł do samodzielnego programowania narzędzi, które je eliminują. Tworzenie apletów optymalizujących czas pracy operacyjnej.
            </div>
        </div>
    </div>
    <div class="timeline-item timeline-right">
        <div class="timeline-dot"></div>
        <div class="timeline-content glass-panel" style="box-shadow: none; border: 1px solid #bda886;">
            <div class="timeline-date" style="color: #fff;">STAN OBECNY</div>
            <div class="timeline-title" style="color: #bda886;">Twórca Vorteza Systems</div>
            <div class="pillar-desc" style="font-size:0.95rem;">
                Budowa niezależnych modułów (TABLICA, SQM Dispatch), łączących się w kompleksowy ekosystem automatyzujący pracę B2B.
            </div>
        </div>
    </div>
</div>
"""
st.markdown(timeline_html, unsafe_allow_html=True)

# ==========================================
# 6. ARCHITEKTURA (FILARY VORTEZA)
# ==========================================
st.markdown("<div id='architektura-rozwiazan' class='section-header-wrapper'><div class='section-header'>Trzy Filary Vorteza</div></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
html_card1 = """<div class="glass-panel pillar-card"><div class="pillar-icon">🧊</div><div class="pillar-title">Vorteza Stack</div><div class="pillar-desc">Fundament danych. Solidna infrastruktura backendowa napisana w Pythonie. Gotowość do wdrożeń lokalnych (Offline-Ready) wewnątrz sieci firmowej i integracja z Arkuszami Google.</div></div>"""
col1.markdown(html_card1, unsafe_allow_html=True)

html_card2 = """<div class="glass-panel pillar-card"><div class="pillar-icon">⚙️</div><div class="pillar-title">Vorteza Flow</div><div class="pillar-desc">Silnik procesowy. Przekształca manualne procedury dyspozytorskie, prawnicze i medyczne w błyskawiczne, zautomatyzowane przepływy cyfrowe (od kalkulacji po wystawienie zlecenia).</div></div>"""
col2.markdown(html_card2, unsafe_allow_html=True)

html_card3 = """<div class="glass-panel pillar-card"><div class="pillar-icon">🌐</div><div class="pillar-title">Vorteza Hub</div><div class="pillar-desc">Centrum dowodzenia. Intuicyjny interfejs wizualizujący w czasie rzeczywistym wszystkie operacje. Zapewnia kadrze menedżerskiej kontrolę nad flotą, terminami spraw i dokumentacją.</div></div>"""
col3.markdown(html_card3, unsafe_allow_html=True)

# ==========================================
# 7. DEMO TECHNOLOGICZNE: KALKULATOR LDM
# ==========================================
st.markdown("<div class='section-header-wrapper'><div class='section-header'>Demo: Logika w Praktyce</div></div>", unsafe_allow_html=True)

# Używamy st.container do stworzenia ramki w stylu glassmorphismu dla elementów interaktywnych
with st.container():
    st.markdown("""
        <div style="background: rgba(15, 23, 42, 0.7); border-radius: 20px 20px 0 0; padding: 2rem; border: 1px solid rgba(255,255,255,0.1); border-bottom: none; text-align: center;">
            <h3 style="color: #ffffff; font-weight: 800; margin: 0;">Inteligentny Kalkulator Ładunkowy</h3>
            <p style="color: #94a3b8; font-size: 1rem; margin-top: 0.5rem;">Fragment kodu odpowiedzialny za automatyczny dobór pojazdu na podstawie wprowadzonych wymiarów (Proof of Concept).</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Blok interaktywny Streamlit
    c1, c2, c3 = st.columns(3)
    with c1:
        length = st.number_input("Długość ładunku (m)", min_value=0.0, max_value=13.6, value=3.2, step=0.1)
    with c2:
        width = st.number_input("Szerokość ładunku (m)", min_value=0.0, max_value=2.45, value=1.2, step=0.1)
    with c3:
        weight = st.number_input("Waga ładunku (kg)", min_value=0, max_value=24000, value=800, step=50)

    # Logika biznesowa
    ldm = (length * width) / 2.4
    if ldm <= 1.5 and weight <= 1200:
        recommendation = "BUS (do 3.5t DMC)"
        color = "#10b981" # Zielony
    elif ldm <= 3.5 and weight <= 3500:
        recommendation = "SOLÓWKA (do 7.5t DMC)"
        color = "#f59e0b" # Pomarańczowy
    elif ldm <= 7.0 and weight <= 8000:
        recommendation = "SOLÓWKA DUŻA (do 12t DMC)"
        color = "#f59e0b"
    else:
        recommendation = "NACZEPA STANDARD (13.6m)"
        color = "#ef4444" # Czerwony

    # Wynik z zachowaniem spójnego CSS
    st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.7); border-radius: 0 0 20px 20px; padding: 2rem; border: 1px solid rgba(255,255,255,0.1); border-top: 1px solid rgba(189,168,134,0.3); text-align: center;">
            <div style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 0.5rem;">Obliczone Metry Ładowne (LDM): <b>{ldm:.2f} m</b></div>
            <div style="color: #ffffff; font-size: 1.5rem; font-weight: 900;">Rekomendowany Pojazd: <span style="color: {color};">{recommendation}</span></div>
        </div>
    """, unsafe_allow_html=True)


# ==========================================
# 8. PORTFOLIO BRANŻOWE (ZAKŁADKI)
# ==========================================
st.markdown("<div class='section-header-wrapper'><div class='section-header'>Zrealizowane Ekosystemy</div></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚛 Logistyka Eventowa & TSL", "⚖️ Legal-Tech", "⚕️ Med-Tech"])

with tab1:
    st.markdown("<h2 style='color:#ffffff; font-weight:900; margin-top:0;'>Zarządzanie Czasem i Przestrzenią w Logistyce</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#cbd5e1; font-size:1.1rem; margin-bottom: 2rem;'>Buduję moduły odporne na stres operacyjny. Projektowane z myślą o skomplikowanych operacjach, takich jak logistyka targowa (np. Intersolar Munich, Airspace World Lisbon).</p>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1.2, 1])
    with col_a:
        st.markdown("""
        <style> .custom-ul li { margin-bottom: 15px; color: #cbd5e1; font-size: 1.05rem;} .custom-ul b { color: #bda886; } </style>
        <ul class='custom-ul'>
            <li><b>SQM Dispatch:</b> Kompleksowe środowisko do zarządzania slotami załadunkowymi, awizacjami i CMR. System weryfikujący gotowość sprzętu i koordynujący magazyn z flotą.</li>
            <li><b>TABLICA:</b> Baza danych z wbudowaną dychotomią operacyjną: osobny workflow dla <i>Przewoźników Stałych</i> (sztywne cenniki) oraz <i>Przewoźników Giełdowych</i> (zmienne koszty).</li>
            <li><b>Szybkie Zlecenie:</b> Automatyczny generator dokumentów PDF. Redukuje czas wystawienia zlecenia o 80%, minimalizując ryzyko błędów ludzkich (np. pomyłki w NIP firmy czy adresach w Komornikach).</li>
        </ul>
        """, unsafe_allow_html=True)
        
    with col_b:
        # Wizualizacja tras logistycznych w Europie i USA
        fig = go.Figure()
        
        # Współrzędne: Komorniki/PL, Lisbon/PT, Munich/DE, Midwest US (Chicago area)
        lons = [16.80, -9.13, 11.58, -87.62] 
        lats = [52.34, 38.72, 48.13, 41.87]
        names = ['Baza SQM', 'Airspace World', 'Intersolar', 'Legendary Midwest Route']
        
        for i in range(1, len(lons)):
            fig.add_trace(go.Scattergeo(
                lon = [lons[0], lons[i]], lat = [lats[0], lats[i]],
                mode = 'lines', line = dict(width = 2, color = '#bda886'), opacity = 0.8
            ))

        fig.add_trace(go.Scattergeo(
            lon = lons, lat = lats, text = names, mode = 'markers+text', textposition="top right",
            textfont=dict(color="#ffffff", size=11, family="Inter"),
            marker = dict(size=12, color='#bda886', line=dict(width=2, color='#0f172a'))
        ))

        fig.update_layout(
            showlegend=False,
            geo = dict(
                projection_type="orthographic", showland=True, landcolor="rgba(255, 255, 255, 0.08)", 
                showocean=True, oceancolor="rgba(0,0,0,0)", showcountries=True, countrycolor="rgba(189,168,134,0.2)",
                bgcolor="rgba(0,0,0,0)"
            ),
            margin=dict(l=0, r=0, t=0, b=0), height=350, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("<h2 style='color:#ffffff; font-weight:900; margin-top:0;'>Porządek Algorytmiczny w Usługach Prawnych</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='custom-ul' style='margin-top: 1.5rem;'>
        <li><b>Bezpieczeństwo i Architektura Danych:</b> Tworzenie szyfrowanych, lokalnych środowisk do zarządzania ściśle poufną dokumentacją procesową.</li>
        <li><b>Generator Pism Procesowych:</b> Automatyzacja tworzenia wielostronicowych pism na podstawie tagów i predefiniowanych baz danych klientów.</li>
        <li><b>Zarządzanie Czasem (Deadlines):</b> Algorytmy wyliczające ustawowe terminy odpowiedzi na pisma urzędowe i powiadamiające zespół o zbliżających się datach krytycznych.</li>
    </ul>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h2 style='color:#ffffff; font-weight:900; margin-top:0;'>Usprawnienie Administracji w Medycynie Pracy</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='custom-ul' style='margin-top: 1.5rem;'>
        <li><b>Zarządzanie Kartoteką Cyfrową:</b> Systemy eliminujące papierowy obieg dokumentów. Szybkie wyszukiwanie pacjentów, historii badań i ważności certyfikatów.</li>
        <li><b>Automatyzacja Skierowań:</b> Błyskawiczne generowanie skierowań na padania psychologiczne czy wysokościowe na podstawie kodu stanowiska pracownika.</li>
        <li><b>Cyfrowe Orzecznictwo:</b> Wystawianie orzeczeń zgodnych z normami prawnymi, archiwizowanych w ustrukturyzowanej bazie danych z pełnym audytem logowań.</li>
    </ul>
    """, unsafe_allow_html=True)

# ==========================================
# 9. VORTEZA HUB - LIVE DASHBOARD PREVIEW
# ==========================================
st.markdown("<div class='section-header-wrapper'><div class='section-header'>Analityka: Vorteza Hub Dashboard</div></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#cbd5e1; margin-bottom: 2rem;'>Symulacja na żywo. Wykresy generowane za pomocą Python Plotly na podstawie analizy 30-dniowego wolumenu operacyjnego.</p>", unsafe_allow_html=True)

df_mock = generate_mock_logistics_data()

c_dash1, c_dash2 = st.columns([1, 1])

with c_dash1:
    # Wykres 1: Struktura Zleceń (Bar Chart)
    fig1 = px.bar(
        df_mock, x='Data', y=['Zlecenia_Stali', 'Zlecenia_Gielda'],
        title="Dzienny Wolumen Zleceń Transportowych",
        color_discrete_map={'Zlecenia_Stali': '#bda886', 'Zlecenia_Gielda': '#475569'},
        labels={'value': 'Ilość Zleceń', 'variable': 'Typ Przewoźnika'}
    )
    fig1.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15, 23, 42, 0.65)',
        font=dict(color='#cbd5e1'), title_font=dict(color='#ffffff', size=18, family="Inter"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=60, b=20, l=20, r=20),
        xaxis=dict(showgrid=False, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    # Rysowanie w szklanym panelu
    st.plotly_chart(fig1, use_container_width=True)

with c_dash2:
    # Wykres 2: Optymalizacja Czasu (Line Chart)
    fig2 = px.line(
        df_mock, x='Data', y='Czas_Obslugi_Minuty',
        title="Średni Czas Wystawienia Zlecenia (Efekt Automatyzacji)",
        color_discrete_sequence=['#10b981']
    )
    # Wypełnienie pod linią
    fig2.update_traces(fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.2)')
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15, 23, 42, 0.65)',
        font=dict(color='#cbd5e1'), title_font=dict(color='#ffffff', size=18, family="Inter"),
        margin=dict(t=60, b=20, l=20, r=20),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title="Czas (Minuty)")
    )
    st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# 10. STOPKA I CALL TO ACTION
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
html_footer = """
    <div class="glass-panel" style="text-align: center; padding: 4rem 3rem; margin: 0 auto; max-width: 900px; border-radius: 30px;">
        <h2 style="font-weight: 900; margin-bottom: 1rem; color: #ffffff; font-size: 2.8rem; letter-spacing: -1px;">Czas na optymalizację Twojej firmy.</h2>
        <p style="color: #cbd5e1; margin-bottom: 3rem; font-size: 1.25rem; line-height: 1.6;">
            Przestań dopasowywać swoje procesy do gotowego oprogramowania.<br>
            Zbudujmy system, który zdejmie z Twojego zespołu powtarzalną pracę operacyjną.
        </p>
        <a href="mailto:kontakt@vorteza.local" class="btn-gold" style="font-size: 1.25rem; padding: 18px 50px;">Porozmawiajmy o Architekturze</a>
        
        <div style="margin-top: 4rem; padding-top: 2.5rem; border-top: 1px solid rgba(255,255,255,0.15); display: flex; justify-content: space-between; align-items: flex-end; text-align: left;">
            <div>
                <span style="color: #bda886; font-weight: 900; font-size: 1.4rem; letter-spacing: 1px;">Vorteza Systems</span><br>
                <span style="color: #94a3b8; font-size: 0.95rem;">Autorski projekt Piotra Dukiela</span>
            </div>
            <div style="text-align: right; color: #94a3b8; font-size: 0.95rem; line-height: 1.5;">
                <b>Baza Operacyjna:</b><br>
                SQM Prosta Spółka Akcyjna<br>
                Komorniki, Polska
            </div>
        </div>
    </div>
    <br><br>
"""
st.markdown(html_footer, unsafe_allow_html=True)
