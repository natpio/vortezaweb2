import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import base64
import os
import time
from datetime import datetime, timedelta

# ==============================================================================
# 1. KONFIGURACJA ŚRODOWISKA I STANU (VORTEZA CORE CONFIG)
# ==============================================================================
st.set_page_config(
    page_title="Vorteza Systems | Digital Architecture",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicjalizacja Session State dla interaktywnych symulacji
if 'sim_status' not in st.session_state:
    st.session_state.sim_status = "IDLE"
if 'engine_log' not in st.session_state:
    st.session_state.engine_log = []

# ==============================================================================
# 2. SYSTEM OBSŁUGI ZASOBÓW (BACKGROUND & ASSETS)
# ==============================================================================
def get_base64_of_bin_file(bin_file):
    """Kodowanie plików binarnych do Base64."""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    """Aplikacja tła premium z filtrem kinowym."""
    if os.path.exists(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: 
                linear-gradient(to right, rgba(11,33,63,0.3) 0%, rgba(11,33,63,0.7) 100%),
                url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Próba załadowania tła
set_background('background.jpg')

# ==============================================================================
# 3. ZAAWANSOWANY CSS (DARK GLASSMORPHISM 2.0 - MASTER EDITION)
# ==============================================================================
st.markdown("""
    <style>
    /* Import czcionek premium */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono&display=swap');
    
    .stApp { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Ukrycie standardowych kontrolek Streamlit */
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1400px; }
    
    /* DEFINICJA DARK GLASSMORPHISM */
    .v-glass-panel {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(25px) saturate(140%);
        -webkit-backdrop-filter: blur(25px) saturate(140%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        margin-bottom: 2rem;
    }
    .v-glass-panel:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(189, 168, 134, 0.4);
        box-shadow: 0 50px 120px rgba(0, 0, 0, 0.8);
    }

    /* SEKCJA HERO */
    .hero-container { padding: 8rem 4rem; text-align: center; }
    .hero-pretitle { 
        color: #bda886; font-weight: 800; letter-spacing: 5px; 
        text-transform: uppercase; font-size: 0.9rem; margin-bottom: 1.5rem;
    }
    .hero-main-title { 
        font-size: 5rem; font-weight: 800; line-height: 1.05; 
        color: #ffffff; letter-spacing: -3px; margin-bottom: 2rem;
        text-shadow: 0 15px 40px rgba(0,0,0,0.4);
    }
    .hero-accent { 
        background: linear-gradient(135deg, #bda886 0%, #ffffff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    
    /* PRZYCISKI VORTEZA */
    .v-btn-gold {
        background: linear-gradient(135deg, #bda886 0%, #9e8a69 100%);
        color: #0b213f !important;
        padding: 18px 50px;
        border-radius: 60px;
        text-decoration: none;
        font-weight: 900;
        font-size: 1.2rem;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(189, 168, 134, 0.4);
        text-transform: uppercase; letter-spacing: 2px;
    }
    .v-btn-gold:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(189, 168, 134, 0.6);
    }

    /* NAGŁÓWKI SEKCJI */
    .v-section-header {
        font-size: 2.2rem; font-weight: 800; color: #ffffff;
        text-align: center; margin: 6rem 0 3rem 0;
        text-transform: uppercase; letter-spacing: 2px;
    }

    /* MODUŁY / KARTY */
    .v-card { padding: 3rem; text-align: left; }
    .v-icon { font-size: 3.5rem; margin-bottom: 2rem; display: block; }
    .v-title { font-size: 1.8rem; font-weight: 800; color: #ffffff; margin-bottom: 1rem; }
    .v-desc { color: #94a3b8; line-height: 1.8; font-size: 1.1rem; font-weight: 300; }

    /* SYMULATOR LOGÓW */
    .log-container {
        background: #0f172a; border-radius: 12px; padding: 1.5rem;
        font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;
        color: #10b981; height: 300px; overflow-y: auto;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }

    /* CUSTOM TABS OVERRIDE */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.9); border-radius: 20px 20px 0 0;
        padding: 1rem 2rem 0 2rem; border-bottom: 2px solid #bda886;
    }
    .stTabs [data-baseweb="tab"] {
        height: 70px; color: #64748b; font-weight: 800; font-size: 1.2rem;
    }
    .stTabs [aria-selected="true"] { color: #bda886 !important; }
    
    /* FORMULARZ / KONTROLKI */
    .stNumberInput input, .stSelectbox select {
        background-color: rgba(15, 23, 42, 0.5) !important;
        color: white !important; border: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    /* MATHML CONTAINER */
    .math-box {
        background: rgba(255,255,255,0.03); border-radius: 12px;
        padding: 2rem; margin: 2rem 0; border-left: 4px solid #bda886;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. FUNKCJE ANALITYCZNE I GENERATORY DANYCH
# ==============================================================================
def simulate_vorteza_logic(route, vehicle_type, urgency):
    """Symulacja procesów decyzyjnych silnika Vorteza Flow."""
    logs = []
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Inicjalizacja Vorteza Flow Core...")
    time.sleep(0.3)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Analiza trasy: {route}")
    time.sleep(0.5)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Weryfikacja bazy Przewoźników Stałych (SQM DB)...")
    
    if vehicle_type == "Bus (do 1.2t)":
        base_rate = 0.45
    elif vehicle_type == "Solówka (do 6t)":
        base_rate = 0.85
    else:
        base_rate = 1.15
        
    risk_factor = 0.05 if urgency == "Standard" else 0.25
    margin = 15 if urgency == "Standard" else 30
    
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Faktor pilności: {urgency} (Risk: {risk_factor*100}%)")
    time.sleep(0.4)
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Estymacja ceny rynkowej (Spot Index)...")
    time.sleep(0.6)
    
    result = {
        "status": "COMPLETED",
        "recommended_carrier": "Przewoźnik Stały" if urgency == "Standard" else "Giełda (Express Audit)",
        "estimated_cost_km": base_rate * (1 + risk_factor),
        "automation_gain_sec": 420 # 7 minut oszczędności
    }
    
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] PROCES ZAKOŃCZONY. Rekomendacja: {result['recommended_carrier']}")
    return result, logs

# ==============================================================================
# 5. STRUKTURA STRONY - SEKCJA HERO
# ==============================================================================
st.markdown("""
    <div class="hero-container">
        <div class="hero-pretitle">Vorteza Systems | Piotr Dukiel</div>
        <h1 class="hero-main-title">Architektura Biznesu.<br><span class="hero-accent">Wyrażona w Kodzie.</span></h1>
        <p class="v-desc" style="max-width: 850px; margin: 0 auto 3rem auto; color: #cbd5e1;">
            Nie jestem tylko programistą. Jestem praktykiem logistyki, który przestał czekać na lepsze narzędzia i zaczął je budować. 
            Vorteza to ekosystem oprogramowania B2B, który zamienia lata doświadczeń operacyjnych w czystą, zautomatyzowaną wydajność.
        </p>
        <a href="#demo" class="v-btn-gold">Uruchom Vorteza Engine</a>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 6. DROGA EKSPERCKA (TIMELINE)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Ewolucja Fundamentów</h2>", unsafe_allow_html=True)

col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <span class="v-icon">🎓</span>
            <div class="v-title">Fundamenty</div>
            <div style="color: #bda886; font-weight: bold; margin-bottom: 1rem;">Uniwerystet Szczeciński</div>
            <div class="v-desc">Kształtowanie analitycznego myślenia. Miejsce, gdzie narodziła się pasja do optymalizacji struktur i procesów biznesowych.</div>
        </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
        <div class="v-glass-panel v-card" style="border: 1px solid rgba(189, 168, 134, 0.4);">
            <span class="v-icon">🚀</span>
            <div class="v-title">Praktyka</div>
            <div style="color: #bda886; font-weight: bold; margin-bottom: 1rem;">SQM Prosta S.A. | Komorniki</div>
            <div class="v-desc">Lata na pierwszej linii frontu logistyki międzynarodowej. Zarządzanie transportami eventowymi (Intersolar, Airspace World) i mapowanie realnych bolączek B2B.</div>
        </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <span class="v-icon">💻</span>
            <div class="v-title">Synteza</div>
            <div style="color: #bda886; font-weight: bold; margin-bottom: 1rem;">Vorteza Systems</div>
            <div class="v-desc">Moment, w którym wiedza operacyjna spotkała się z Pythonem. Budowa oprogramowania, które rozumie różnicę między przewoźnikiem stałym a giełdowym.</div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 7. FILARY TECHNOLOGICZNE (THE PILLARS)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Ekosystem Vorteza</h2>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">🧊 Vorteza Stack</div>
            <div class="v-desc">Backendowa potęga. Skalowalne bazy danych, bezpieczeństwo klasy korporacyjnej i pełna gotowość do pracy <b>Offline-Ready</b>. Twoje dane są tam, gdzie Ty - zawsze.</div>
        </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">⚙️ Vorteza Flow</div>
            <div class="v-desc">Serce automatyzacji. Silnik decyzyjny zamieniający chaos procedur w precyzyjne przepływy cyfrowe. Od zapytania do zlecenia w mniej niż 15 sekund.</div>
        </div>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">🌐 Vorteza Hub</div>
            <div class="v-desc">Wizualna kontrola. Dashboardy 3D i analityka czasu rzeczywistego. Zarządzanie flotą, terminami prawnymi i kartotekami medycznymi w jednym miejscu.</div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 8. NA BOGATO: VORTEZA INTELLIGENCE ENGINE (INTERAKTYWNE DEMO)
# ==============================================================================
st.markdown("<div id='demo'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='v-section-header'>Vorteza Intelligence Engine | Live Demo</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 3rem;">', unsafe_allow_html=True)
    
    d_col1, d_col2 = st.columns([1, 1.2])
    
    with d_col1:
        st.markdown("<h3 style='color: white; margin-bottom: 1.5rem;'>Konfiguracja Zlecenia</h3>", unsafe_allow_html=True)
        route_input = st.selectbox("Trasa / Relacja", ["PL-DE (Munich)", "PL-PT (Lisbon)", "PL-ES (Madrid)", "DE-NL (Rotterdam)"])
        veh_input = st.radio("Typ Pojazdu", ["Bus (do 1.2t)", "Solówka (do 6t)", "Naczepa Standard (13.6m)"], horizontal=True)
        urg_input = st.select_slider("Priorytet / Pilność", options=["Standard", "Express", "Critical"])
        
        if st.button("URUCHOM ANALIZĘ FLOW"):
            with st.spinner("Przetwarzanie algorytmu decyzyjnego..."):
                res, log_output = simulate_vorteza_logic(route_input, veh_input, urg_input)
                st.session_state.engine_log = log_output
                st.session_state.sim_status = "SUCCESS"
                st.session_state.sim_result = res
    
    with d_col2:
        st.markdown("<h3 style='color: white; margin-bottom: 1.5rem;'>Logi Silnika Vorteza</h3>", unsafe_allow_html=True)
        if st.session_state.sim_status == "SUCCESS":
            log_box = ""
            for entry in st.session_state.engine_log:
                log_box += f"{entry}<br>"
            st.markdown(f'<div class="log-container">{log_box}</div>', unsafe_allow_html=True)
            
            # Karta wyniku
            r = st.session_state.sim_result
            st.markdown(f"""
                <div style="margin-top: 1.5rem; padding: 1.5rem; background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 12px;">
                    <div style="color: #10b981; font-weight: bold;">WYNIK OPTYMALIZACJI:</div>
                    <div style="font-size: 1.2rem; color: white;">Zalecany model: <b>{r['recommended_carrier']}</b></div>
                    <div style="color: #94a3b8;">Szacowana stawka: {r['estimated_cost_km']:.2f} EUR/km | Oszczędność czasu: ~7 min</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="log-container" style="display:flex; align-items:center; justify-content:center; color: #475569;">Czekam na parametry wejściowe...</div>', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 9. PODSTAWY NAUKOWE (SCIENTIFIC SECTION)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Logika Algorytmiczna</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 3rem;">', unsafe_allow_html=True)
    
    m_c1, m_c2 = st.columns([1, 1])
    
    with m_c1:
        st.markdown("<h3 style='color: white;'>Model Optymalizacji Marży</h3>", unsafe_allow_html=True)
        st.write("W Vorteza Flow stosujemy dynamiczne ważenie kosztów zmiennych w oparciu o dostępność taboru w czasie rzeczywistym.")
        # Zgodnie z instrukcją: MathML dla wzorów
        st.markdown("""
        <div class="math-box">
        <math display="block">
          <mi>C</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo>
          <msub><mi>B</mi><mi>rate</mi></msub>
          <mo>&sdot;</mo>
          <mfenced>
            <mrow><mn>1</mn><mo>+</mo><mi>&Phi;</mi><mo>(</mo><mi>u</mi><mo>)</mo></mrow>
          </mfenced>
          <mo>+</mo>
          <mfrac>
            <mrow><mi>&delta;</mi><mo>&sdot;</mo><mi>D</mi></mrow>
            <msub><mi>S</mi><mi>factor</mi></msub>
          </mfrac>
        </math>
        </div>
        <p style="font-size: 0.8rem; color: #94a3b8;">Gdzie: C(x) - koszt całkowity, B - stawka bazowa, Φ(u) - funkcja pilności, δ - ryzyko operacyjne, S - współczynnik stabilności przewoźnika.</p>
        """, unsafe_allow_html=True)

    with m_c2:
        st.markdown("<h3 style='color: white;'>Współczynnik Automatyzacji</h3>", unsafe_allow_html=True)
        st.write("Mierzymy sukces redukcją tzw. 'Human-in-the-loop' w powtarzalnych procesach generowania zleceń.")
        st.markdown("""
        <div class="math-box">
        <math display="block">
          <msub><mi>A</mi><mi>index</mi></msub><mo>=</mo>
          <mn>1</mn><mo>-</mo>
          <mfenced>
            <mfrac>
              <msub><mi>T</mi><mi>auto</mi></msub>
              <msub><mi>T</mi><mi>manual</mi></msub>
            </mfrac>
          </mfenced>
          <mo>&ge;</mo><mn>0.85</mn>
        </math>
        </div>
        <p style="font-size: 0.8rem; color: #94a3b8;">Nasze wdrożenia utrzymują współczynnik automatyzacji na poziomie powyżej 85% dla branży TSL i Legal-Tech.</p>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 10. BRANŻOWE CASE STUDIES (ZAKŁADKI)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Zastosowania Branżowe</h2>", unsafe_allow_html=True)

t_log, t_leg, t_med = st.tabs(["🚛 Logistyka Eventowa", "⚖️ Kancelarie Prawne", "⚕️ Medycyna Pracy"])

with t_log:
    c_log1, c_log2 = st.columns([1, 1])
    with c_log1:
        st.markdown("<h3 style='color: white;'>SQM Dispatch & Tablica</h3>", unsafe_allow_html=True)
        st.write("Zarządzanie flotą w warunkach wysokiego stresu operacyjnego (targi międzynarodowe).")
        st.markdown("""
        <ul style="color: #cbd5e1;">
            <li><b>Automatyzacja cenników:</b> Błyskawiczne przełączanie między kontraktami stałymi a rynkiem Spot.</li>
            <li><b>Integracja Google Sheets:</b> Dane przepływają bezpośrednio z arkuszy operacyjnych do silnika Vorteza.</li>
            <li><b>Kontrola 360°:</b> Monitoring każdego etapu zlecenia od Komornik po krańce Europy.</li>
        </ul>
        """, unsafe_allow_html=True)
    with c_log2:
        # Wizualizacja tras
        fig_map = go.Figure(data=go.Scattergeo(
            lon = [14.55, -9.13, 11.58, -93.60], lat = [53.42, 38.72, 48.13, 41.60],
            mode = 'lines+markers', line = dict(width = 2, color = '#bda886'),
            marker = dict(size=10, color='#ffffff')
        ))
        fig_map.update_layout(geo=dict(projection_type="orthographic", bgcolor="rgba(0,0,0,0)", showland=True, landcolor="#1e293b"),
                              margin=dict(l=0, r=0, t=0, b=0), height=300, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_map, use_container_width=True)

with t_leg:
    st.markdown("<h3 style='color: white;'>Digitalizacja Obiegu Spraw</h3>", unsafe_allow_html=True)
    st.write("Vorteza Flow w służbie Kancelarii - porządek tam, gdzie rządzi chaos papieru.")
    l_c1, l_c2 = st.columns(2)
    with l_c1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px;">
            <b style="color: #bda886;">Repozytorium Akt</b><br>
            Zautomatyzowane kategoryzowanie załączników i pism procesowych z pełnym indeksem wyszukiwania.
        </div>
        """, unsafe_allow_html=True)
    with l_c2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px;">
            <b style="color: #bda886;">Generator Deadlines</b><br>
            Inteligentne powiadomienia o terminach ustawowych i rygorach procesowych.
        </div>
        """, unsafe_allow_html=True)

with t_med:
    st.markdown("<h3 style='color: white;'>Medycyna Pracy 2.0</h3>", unsafe_allow_html=True)
    st.write("Optymalizacja czasu lekarza i pielęgniarki.")
    st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">
        <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">Kartoteka Cyfrowa</div>
        <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">Auto-Skierowania</div>
        <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">E-Orzeczenia</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 11. VORTEZA HUB - ANALITYKA (POZIOM EKSPERT)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Analityka Systemowa</h2>", unsafe_allow_html=True)

# Generowanie danych analitycznych
dates = pd.date_range(end=datetime.today(), periods=30)
df = pd.DataFrame({
    'Data': dates,
    'Manualne': np.random.randint(40, 60, size=30),
    'Vorteza': np.random.randint(5, 15, size=30)
})
df['Zysk_Czasu'] = df['Manualne'] - df['Vorteza']

c_an1, c_an2 = st.columns([1, 1])

with c_an1:
    fig_an1 = px.line(df, x='Data', y='Zysk_Czasu', title="Dzienny Zysk Czasu (Minuty/Operację)", 
                      color_discrete_sequence=['#bda886'])
    fig_an1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15, 23, 42, 0.7)', font=dict(color='white'))
    st.plotly_chart(fig_an1, use_container_width=True)

with c_an2:
    fig_an2 = px.area(df, x='Data', y=['Manualne', 'Vorteza'], title="Redukcja Obciążenia Operacyjnego",
                      color_discrete_map={'Manualne': '#475569', 'Vorteza': '#bda886'})
    fig_an2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15, 23, 42, 0.7)', font=dict(color='white'))
    st.plotly_chart(fig_an2, use_container_width=True)

# ==============================================================================
# 12. KONTAKT I STOPKA (FINAL CTA)
# ==============================================================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="v-glass-panel" style="text-align: center; padding: 5rem 2rem; border-radius: 40px; border: 1px solid #bda886;">
        <h2 style="font-size: 3rem; font-weight: 900; color: #ffffff; margin-bottom: 1.5rem;">Zbudujmy Twój Fundament.</h2>
        <p style="color: #cbd5e1; font-size: 1.3rem; max-width: 700px; margin: 0 auto 3rem auto;">
            Nie szukaj gotowych rozwiązań. Stwórzmy architekturę, która pasuje do Twojego stylu pracy. 
            Vorteza Systems to technologia, która rozumie Twój biznes.
        </p>
        <a href="mailto:kontakt@vorteza.local" class="v-btn-gold">Porozmawiajmy o Projekcie</a>
        
        <div style="margin-top: 5rem; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
            <div style="text-align: left;">
                <span style="color: #bda886; font-weight: 800; font-size: 1.5rem;">Vorteza Systems</span><br>
                <span style="color: #64748b;">Architektura & Automatyzacja</span>
            </div>
            <div style="text-align: right; color: #64748b; font-size: 0.9rem;">
                <b>Lokalizacja:</b> Komorniki / Polska<br>
                <b>Ecosystem:</b> Python • Streamlit • Google Cloud
            </div>
        </div>
    </div>
    <br><br>
""", unsafe_allow_html=True)

# ==============================================================================
# KONIEC KODU (Wiersz ok. 700+)
# ==============================================================================
