import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. KONFIGURACJA STRONY
st.set_page_config(
    page_title="Vorteza Systems | Portfolio",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ZAAWANSOWANY CSS (Modularne Fundamenty & Efekt WOW)
st.markdown("""
    <style>
    /* Reset i tło globalne */
    .stApp {
        background-color: #f4f7f6;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Ukrycie elementów Streamlit dla czystego wyglądu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Główna sekcja Hero */
    .hero-box {
        background: linear-gradient(135deg, #ffffff 0%, #eef2f3 100%);
        border-radius: 20px;
        padding: 6rem 3rem;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.04);
        margin-top: 2rem;
        margin-bottom: 4rem;
        border: 1px solid rgba(255,255,255,0.5);
    }
    .hero-title {
        color: #0b213f;
        font-size: 3.8rem;
        font-weight: 900;
        letter-spacing: -1.5px;
        margin-bottom: 1.5rem;
        line-height: 1.1;
    }
    .hero-title span {
        color: #16a085; /* Zielony akcent technologiczny */
    }
    .hero-subtitle {
        color: #5a6a7e;
        font-size: 1.25rem;
        max-width: 800px;
        margin: 0 auto 2.5rem auto;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Karty Modułów (Stack, Flow, Hub) */
    .module-card {
        background-color: white;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        height: 100%;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-top: 4px solid #16a085;
    }
    .module-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    }
    .module-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .module-title {
        color: #0b213f;
        font-weight: 700;
        font-size: 1.4rem;
        margin-bottom: 1rem;
    }
    .module-text {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Nagłówki sekcji */
    .section-header {
        text-align: center;
        color: #0b213f;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 4rem 0 2rem 0;
    }
    
    /* Przyciski */
    .btn-primary {
        background-color: #0b213f;
        color: #ffffff !important;
        padding: 14px 36px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(11, 33, 63, 0.2);
    }
    .btn-primary:hover {
        background-color: #16a085;
        box-shadow: 0 6px 20px rgba(22, 160, 133, 0.3);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown("""
    <div class="hero-box">
        <h1 class="hero-title">Praktyka biznesowa.<br><span>Zamieniona w kod.</span></h1>
        <p class="hero-subtitle">
            Vorteza Systems to oprogramowanie B2B skrojone na miarę. Narzędzia, które tworzę, 
            wyrastają z lat realnych doświadczeń operacyjnych. Przekształcam wąskie gardła w logistyce, 
            prawie i medycynie pracy w zautomatyzowane, wydajne ekosystemy gotowe do pracy w chmurze i offline.
        </p>
        <a href="#architektura" class="btn-primary">Poznaj Architekturę</a>
    </div>
""", unsafe_allow_html=True)

# 4. ARCHITEKTURA (FILARY VORTEZA)
st.markdown("<h2 id='architektura' class='section-header'>Trzy Filary Vorteza</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="module-card">
            <div class="module-icon">🧊</div>
            <div class="module-title">Vorteza Stack</div>
            <div class="module-text">
                Fundament danych. Solidna i bezpieczna infrastruktura backendowa. 
                Pełna gotowość do wdrożeń lokalnych (Offline-Ready) w biurze oraz płynna integracja 
                z narzędziami klasy Google Sheets.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="module-card">
            <div class="module-icon">⚙️</div>
            <div class="module-title">Vorteza Flow</div>
            <div class="module-text">
                Automatyzacja procesów. Silnik zamieniający skomplikowane logiki biznesowe, 
                od dysponowania flotą po obieg dokumentacji prawnej, w proste i błyskawiczne 
                przepływy pracy.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="module-card">
            <div class="module-icon">🌐</div>
            <div class="module-title">Vorteza Hub</div>
            <div class="module-text">
                Centrum integracji i dowodzenia. Ujednolicony interfejs dający kadrze 
                zarządzającej podgląd operacji w czasie rzeczywistym. Od monitorowania 
                tras po statusy spraw pacjentów.
            </div>
        </div>
    """, unsafe_allow_html=True)


# 5. PORTFOLIO BRANŻOWE (Interaktywne Zakładki)
st.markdown("<h2 class='section-header'>Zrealizowane Ekosystemy</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚛 Logistyka & Transport", "⚖️ Usługi Prawne", "⚕️ Medycyna Pracy"])

with tab1:
    st.subheader("Automatyzacja procesów transportowych i spedycyjnych")
    st.write("Wielomodułowe rozwiązania usprawniające codzienną pracę dyspozytorów i spedytorów. Stworzone do obsługi wymagających operacji, w tym logistyki eventowej na rynkach międzynarodowych.")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.markdown("""
        * **SQM Dispatch:** Pełna kontrola nad flotą, zarządzanie kierowcami i śledzenie statusów.
        * **TABLICA:** Centralny system zarządzania danymi i cennikami, z bezproblemową wymianą informacji dla Przewoźników Stałych i Giełdowych.
        * **Szybkie Zlecenie:** Moduł redukujący czas wystawiania dokumentacji i automatyzujący kalkulacje ładunkowe.
        """)
        
    with col_b:
        # Interaktywny element - Globus Plotly (pokazuje zasięg i skille programistyczne)
        # Niewidoczne wplecenie: współrzędne odpowiadają trasom i punktom (Szczecin, Lisbona, Monachium, Midwest US)
        fig = go.Figure(data=go.Scattergeo(
            lon = [14.55, -9.13, 11.58, -93.60], 
            lat = [53.42, 38.72, 48.13, 41.60],
            text = ['Baza Operacyjna', 'Węzeł Południowy', 'Centrum Przeładunkowe', 'Trasa Transkontynentalna'],
            mode = 'markers',
            marker = dict(size=12, color='#16a085', line=dict(width=2, color='white'))
        ))
        fig.update_layout(
            geo = dict(
                projection_type="orthographic", 
                showland=True, 
                landcolor="#eef2f3", 
                oceancolor="#ffffff",
                showocean=True,
                bgcolor="rgba(0,0,0,0)"
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            height=300,
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Dedykowany system dla Kancelarii Prawnych")
    st.write("Bezpieczeństwo i porządek w świecie paragrafów.")
    st.markdown("""
    * Bezpieczne repozytorium akt i załączników.
    * Automatyzacja generowania powtarzalnych dokumentów i pism procesowych.
    * Cyfrowe zarządzanie kalendarzem spraw i śledzenie kluczowych terminów (deadlines).
    """)

with tab3:
    st.subheader("Zarządzanie kartoteką w Medycynie Pracy")
    st.write("Odciążenie personelu administracyjnego poprzez optymalizację przepływu danych.")
    st.markdown("""
    * Uporządkowana, cyfrowa baza danych pacjentów zachowująca standardy prywatności.
    * Automatyzacja procesu generowania skierowań na badania.
    * Szybkie wystawianie i archiwizacja orzeczeń lekarskich.
    """)

# 6. STOPKA / KONTAKT
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; padding: 2rem; background-color: #0b213f; border-radius: 15px; color: white;">
        <h2>Gotowy na optymalizację?</h2>
        <p style="color: #a0aec0; margin-bottom: 2rem;">Zaprojektujmy system, który zdejmie z Twojego zespołu powtarzalną pracę.</p>
        <a href="mailto:kontakt@vorteza.local" class="btn-primary" style="background-color: #16a085; box-shadow: none;">Porozmawiajmy o kodzie</a>
    </div>
""", unsafe_allow_html=True)
