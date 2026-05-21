import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Vorteza Systems | Portfolio", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

# 1. KULOODPORNY CSS
st.markdown("""
    <style>
    /* Globalne tło inspirowane załącznikiem - stały gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f4f0 0%, #e5e2da 35%, #343d46 65%, #1a1e23 100%);
        background-attachment: fixed;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    
    /* Wspólne tła dla kart, aby tekst był czytelny na ciemnym tle */
    .glass-panel {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        border: 2px solid #bda886; /* Złota ramka */
    }

    /* Sekcja Hero */
    .hero-box {
        padding: 5rem 2rem;
        text-align: center;
        margin: 2rem auto 4rem auto;
        max-width: 900px;
    }
    .hero-title { color: #0b213f; font-size: 3.5rem; font-weight: 900; margin-bottom: 1.5rem; line-height: 1.2;}
    .hero-title span { color: #bda886; }
    .hero-subtitle { color: #5a6a7e; font-size: 1.2rem; max-width: 750px; margin: 0 auto 2.5rem auto; line-height: 1.6;}
    
    .btn-primary {
        background-color: #0b213f; color: #ffffff !important; padding: 12px 35px; border-radius: 50px; 
        text-decoration: none; font-weight: bold; transition: all 0.3s ease; border: 2px solid #bda886; display: inline-block;
    }
    .btn-primary:hover { background-color: #bda886; color: #0b213f !important; }

    /* Nagłówki sekcji */
    .section-header-dark { text-align: center; color: #0b213f; font-size: 2.2rem; font-weight: 800; margin: 3rem 0; text-transform: uppercase;}
    .section-header-light { text-align: center; color: #ffffff; font-size: 2.2rem; font-weight: 800; margin: 3rem 0; text-transform: uppercase; text-shadow: 0 2px 4px rgba(0,0,0,0.5);}

    /* Karty modułów */
    .module-card { padding: 2rem; height: 100%; transition: transform 0.3s ease; }
    .module-card:hover { transform: translateY(-5px); }
    .module-icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .module-title { color: #0b213f; font-weight: 800; font-size: 1.3rem; margin-bottom: 1rem; }
    .module-text { color: #5a6a7e; font-size: 0.95rem; line-height: 1.5; }

    /* Oś czasu (Zaufali mi) */
    .timeline-wrapper { position: relative; display: flex; justify-content: space-between; align-items: center; max-width: 1000px; margin: 0 auto; padding: 2rem 0;}
    .timeline-line { position: absolute; top: 40px; left: 5%; right: 25%; height: 2px; background-color: #0b213f; z-index: 1;}
    .trust-node { display: flex; flex-direction: column; align-items: center; z-index: 2; width: 150px;}
    .trust-circle { width: 80px; height: 80px; background: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; border: 3px solid #0b213f; margin-bottom: 1rem; box-shadow: 0 5px 15px rgba(0,0,0,0.1);}
    .trust-circle.active { border-color: #bda886; box-shadow: 0 0 15px rgba(189,168,134,0.5); }
    .trust-label { text-align: center; font-weight: bold; color: #0b213f; font-size: 0.9rem; line-height: 1.2;}

    /* Plakietka Vorteza */
    .plaque-box { width: 250px; height: 120px; border-radius: 5px; border: 4px solid #bda886; background: linear-gradient(135deg, #ffffff 0%, #e5e2da 100%); padding: 1rem; position: relative; box-shadow: 0 10px 20px rgba(0,0,0,0.2); z-index: 2;}
    .plaque-head { color: #5a6a7e; font-size: 0.75rem; font-weight: bold;}
    .plaque-title { color: #0b213f; font-size: 1.4rem; font-weight: 900; margin-top: 5px;}
    .plaque-v { position: absolute; top: 10px; right: 15px; font-size: 1.5rem; color: #bda886; font-weight: bold;}

    /* Zakładki Streamlit (wymuszenie czytelności) */
    div[data-baseweb="tabs"] { background: rgba(255,255,255,0.95); padding: 2rem; border-radius: 15px; border: 2px solid #bda886; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 4px; color: #0b213f; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# 2. HERO SECTION (Zwarte tagi HTML zapobiegające błędom)
html_hero = """<div class="glass-panel hero-box"><h1 class="hero-title">Praktyka biznesowa.<br><span>Zamieniona w kod.</span></h1><p class="hero-subtitle">Vorteza Systems to oprogramowanie B2B skrojone na miarę. Narzędzia, które tworzę, wyrastają z lat realnych doświadczeń operacyjnych. Przekształcam wąskie gardła w logistyce, prawie i medycynie pracy w zautomatyzowane, wydajne ekosystemy gotowe do pracy w chmurze i offline.</p><a href="#architektura" class="btn-primary">Poznaj Architekturę</a></div>"""
st.markdown(html_hero, unsafe_allow_html=True)

# 3. ZAUFALI MI NAJLEPSI (Skonstruowane jako jeden ciągły blok, żeby Streamlit się nie pogubił)
st.markdown("<h2 class='section-header-dark' style='background: rgba(255,255,255,0.8); padding: 10px; border-radius: 10px; display: inline-block; margin-left: 50%; transform: translateX(-50%);'>Zaufali Mi Najlepsi</h2>", unsafe_allow_html=True)

timeline_html = """<div class="timeline-wrapper"><div class="timeline-line"></div><div class="trust-node"><div class="trust-circle active"><svg width="40" height="40" viewBox="0 0 100 100"><path fill="#0b213f" d="M10 20 L20 10 L80 10 L90 20 L90 80 L80 90 L20 90 L10 80 ZM30 40 A10 10 0 0 1 70 40 L70 60 A10 10 0 0 1 30 60 Z"/></svg></div><div class="trust-label">Uniwersytet<br>Szczeciński</div></div><div class="trust-node"><div class="trust-circle"><svg width="40" height="40" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" stroke="#0b213f" stroke-width="4" fill="none"/><path d="M50 30 Q70 50 50 70 Q30 50 50 30 Z" fill="#0b213f"/></svg></div><div class="trust-label">Eneris<br>Surowce</div></div><div class="trust-node"><div class="trust-circle"><div style="font-size:1.5rem; font-weight:900; color:#0b213f;">TPV</div></div><div class="trust-label">TPV<br>Displays</div></div><div class="trust-node"><div class="trust-circle"><div style="font-size:1.5rem; font-weight:900; color:#0b213f;">SQM</div></div><div class="trust-label">SQM Multimedia<br>Solutions</div></div><div class="plaque-box"><div class="plaque-head">Autorski Projekt:</div><div class="plaque-title">Vorteza<br>Systems</div><div class="plaque-v">V</div></div></div>"""
st.markdown(timeline_html, unsafe_allow_html=True)

# 4. ARCHITEKTURA
st.markdown("<h2 id='architektura' class='section-header-light'>Trzy Filary Vorteza</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
html_card1 = """<div class="glass-panel module-card"><div class="module-icon">🧊</div><div class="module-title">Vorteza Stack</div><div class="module-text">Fundament danych. Solidna i bezpieczna infrastruktura backendowa. Pełna gotowość do wdrożeń lokalnych (Offline-Ready) w biurze oraz płynna integracja z narzędziami klasy Google Sheets.</div></div>"""
col1.markdown(html_card1, unsafe_allow_html=True)

html_card2 = """<div class="glass-panel module-card"><div class="module-icon">⚙️</div><div class="module-title">Vorteza Flow</div><div class="module-text">Automatyzacja procesów. Silnik zamieniający skomplikowane logiki biznesowe, od dysponowania flotą po obieg dokumentacji prawnej, w proste i błyskawiczne przepływy pracy.</div></div>"""
col2.markdown(html_card2, unsafe_allow_html=True)

html_card3 = """<div class="glass-panel module-card"><div class="module-icon">🌐</div><div class="module-title">Vorteza Hub</div><div class="module-text">Centrum integracji i dowodzenia. Ujednolicony interfejs dający kadrze zarządzającej podgląd operacji w czasie rzeczywistym. Od monitorowania tras po statusy spraw pacjentów.</div></div>"""
col3.markdown(html_card3, unsafe_allow_html=True)

# 5. PORTFOLIO BRANŻOWE
st.markdown("<h2 class='section-header-light'>Zrealizowane Ekosystemy</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚛 Logistyka & Transport", "⚖️ Usługi Prawne", "⚕️ Medycyna Pracy"])

with tab1:
    st.subheader("Automatyzacja procesów transportowych i spedycyjnych")
    st.write("Wielomodułowe rozwiązania usprawniające codzienną pracę dyspozytorów i spedytorów. Stworzone do obsługi wymagających operacji, w tym logistyki eventowej na rynkach międzynarodowych.")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.markdown("""
        * **SQM Dispatch:** Pełna kontrola nad flotą, zarządzanie kierowcami i śledzenie statusów.
        * **TABLICA:** Centralny system zarządzania danymi i cennikami (w tym obsługa Przewoźników Stałych i Giełdowych).
        * **Szybkie Zlecenie:** Błyskawiczne generowanie dokumentacji i kalkulacje ładunkowe.
        """)
        
    with col_b:
        fig = go.Figure(data=go.Scattergeo(
            lon = [14.55, -9.13, 11.58, -93.60], lat = [53.42, 38.72, 48.13, 41.60],
            text = ['Baza Operacyjna', 'Węzeł Południowy', 'Centrum Przeładunkowe', 'Trasa Transkontynentalna'], mode = 'markers',
            marker = dict(size=12, color='#bda886', line=dict(width=2, color='white'))
        ))
        fig.update_layout(
            geo=dict(projection_type="orthographic", showland=True, landcolor="#e5e2da", oceancolor="#ffffff", showocean=True, bgcolor="rgba(0,0,0,0)"),
            margin=dict(l=0, r=0, t=0, b=0), height=300, paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Dedykowany system dla Kancelarii Prawnych")
    st.markdown("""
    * Bezpieczne repozytorium akt i załączników.
    * Automatyzacja generowania powtarzalnych dokumentów i pism procesowych.
    * Cyfrowe zarządzanie kalendarzem spraw i śledzenie kluczowych terminów (deadlines).
    """)

with tab3:
    st.subheader("Zarządzanie kartoteką w Medycynie Pracy")
    st.markdown("""
    * Uporządkowana, cyfrowa baza danych pacjentów zachowująca standardy prywatności.
    * Automatyzacja procesu generowania skierowań na badania.
    * Szybkie wystawianie i archiwizacja orzeczeń lekarskich.
    """)

# 6. STOPKA
st.markdown("<br><br>", unsafe_allow_html=True)
html_footer = """<div class="glass-panel" style="text-align: center; padding: 2rem; margin: 0 auto; max-width: 600px;"><h2 style="color: #0b213f;">Gotowy na optymalizację?</h2><p style="color: #5a6a7e; margin-bottom: 2rem;">Zaprojektujmy system, który zdejmie z Twojego zespołu powtarzalną pracę.</p><a href="mailto:kontakt@vorteza.local" class="btn-primary">Porozmawiajmy o kodzie</a></div><br><br>"""
st.markdown(html_footer, unsafe_allow_html=True)
