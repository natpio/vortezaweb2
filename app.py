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

# 2. ZAAWANSOWANY CSS (Modularne Fundamenty & Styl z Załącznika Image_8.png)
st.markdown("""
    <style>
    /* Reset i tło globalne - STYL IMAGE_8.PNG */
    .stApp {
        background-color: #f4f7f6;
        /* Kompleksowe tło: Marmurowy gradient przechodzący w grafitową sieć połączeń */
        background-image: 
            linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(224,229,236,0.5) 100%),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'%3E%3Cdefs%3E%3Cpattern id='pattern' width='200' height='200' patternUnits='userSpaceOnUse'%3E%3Cpath d='M100 0 A100 100 0 0 1 200 100 L200 200 L0 200 A100 100 0 0 1 100 0 Z' fill='%23eceff3' fill-opacity='0.2'/%3E%3C/pattern%3E%3C/defs%3E%3Crect width='100%' height='100%' fill='url(%23pattern)'/%3E%3C/svg%3E"),
            radial-gradient(circle at 75% 25%, #2c3e50, #1a1a2e), /* Głębia grafitowa z prawej strony */
            radial-gradient(circle at 25% 75%, #ffffff, #eef2f3); /* Marmur z lewej strony */
        background-blend-mode: overlay, normal, normal, normal;
        background-attachment: fixed;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #0b213f; /* Ciemnogranatowy tekst jak w Vortezie */
    }
    
    /* Ukrycie elementów Streamlit dla czystego wyglądu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Sekcja Hero - dodanie złotej ramki w stylu plakietki */
    .hero-box {
        background-color: white;
        border-radius: 20px;
        padding: 6rem 3rem;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.04);
        margin-top: 2rem;
        margin-bottom: 4rem;
        border: 2px solid #bda886; /* Złota ramka jak w plakietce */
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
        color: #bda886; /* Złoty akcent technologiczny zamiast zielonego */
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
        border-top: 4px solid #bda886; /* Złota ramka */
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
    
    /* Nagłówki sekcji - Styl Image_8.png */
    .section-header {
        text-align: center;
        color: #0b213f;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 4rem 0 2rem 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Stylizacja Osi Czasu Trusted Sections (Wzorowane na Image_8.png) */
    .trusted-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 4rem 0;
        position: relative;
    }
    .timeline-line {
        position: absolute;
        width: 80%;
        height: 2px;
        background-color: #0b213f; /* Linia główna */
        top: 50%;
        left: 10%;
        transform: translateY(-50%);
        z-index: 1;
    }
    .trust-logo {
        width: 120px;
        height: 120px;
        background-color: rgba(255,255,255,0.8);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px solid rgba(11,33,63,0.1);
        position: relative;
        z-index: 2;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin: 0 1rem;
    }
    .trust-logo.active-node::after {
        content: '';
        position: absolute;
        width: 15px;
        height: 15px;
        background-color: #bda886; /* Złota kropka węzła */
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 10px rgba(189,168,134,0.7);
    }
    .trust-text {
        text-align: center;
        color: #0b213f;
        font-weight: bold;
        margin-top: 1rem;
        font-size: 0.9rem;
    }
    
    /* Styl Plakietki Vorteza (Identynczne z Image_8.png) */
    .plaque-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 300px;
        height: 150px;
        margin-left: 1rem;
        position: relative;
        z-index: 2;
    }
    .plaque-frame {
        border-radius: 5px;
        border: 4px solid #bda886; /* Złota ramka plakietki */
        background: linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(224,229,236,0.5) 100%);
        padding: 1.5rem;
        position: relative;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .plaque-header {
        position: absolute;
        top: 10px;
        left: 15px;
        color: #5a6a7e;
        font-size: 0.85rem;
        text-transform: none;
    }
    .plaque-body {
        color: #0b213f;
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 1rem;
    }
    .plaque-v-logo {
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 2.5rem;
    }
    
    /* Przyciski - Złoty Kolor */
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
        background-color: #bda886; /* Złoty akcent technologiczny */
        box-shadow: 0 6px 20px rgba(189,168,134,0.3);
        transform: translateY(-2px);
    }
    
    /* Ukrycie paska zakładek Streamlit */
    div[data-baseweb="tabs"] {
        background-color: rgba(255,255,255,0.5);
        border-radius: 10px;
        padding: 5px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.03);
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

# 5. NOWA SEKCJA: ZAUFALI MI NAJLEPSI (Styl Image_8.png)
st.markdown("<h2 class='section-header'>Zaufali Mi Najlepsi</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class="trusted-container">
        <div class="timeline-line"></div>
        
        <div>
            <div class="trust-logo active-node">
                <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 100 100"><path fill="%230b213f" d="M10 20 L20 10 L80 10 L90 20 L90 80 L80 90 L20 90 L10 80 ZM30 40 A10 10 0 0 1 70 40 L70 60 A10 10 0 0 1 30 60 Z"/><text x="25" y="105" font-size="12" fill="%230b213f" font-weight="bold">Uniwersytet Szczeciński</text></svg>
            </div>
            <div class="trust-text">Uniwersytet Szczeciński</div>
        </div>
        
        <div>
            <div class="trust-logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" stroke="%230b213f" stroke-width="2" fill="none"/><path d="M50 30 Q70 50 50 70 Q30 50 50 30 Z" fill="%230b213f"/><text x="35" y="105" font-size="12" fill="%230b213f" font-weight="bold">Eneris Surowce</text></svg>
            </div>
            <div class="trust-text">Eneris Surowce</div>
        </div>
        
        <div>
            <div class="trust-logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 100 100"><text x="15" y="60" font-size="30" fill="%230b213f" font-weight="bold">TPV</text><text x="30" y="80" font-size="12" fill="%230b213f">Displays</text></svg>
            </div>
            <div class="trust-text">TPV Displays</div>
        </div>
        
        <div>
            <div class="trust-logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 100 100"><text x="15" y="60" font-size="30" fill="%230b213f" font-weight="bold">SQM</text><text x="10" y="80" font-size="12" fill="%230b213f">Multimedia Solutions</text></svg>
            </div>
            <div class="trust-text">SQM Multimedia Solutions</div>
        </div>
        
        <div class="plaque-wrapper">
            <div class="plaque-frame">
                <div class="plaque-header">Autorski Projekt:</div>
                <div class="plaque-body">Vorteza Systems</div>
                <div class="plaque-v-logo">🧊</div> </div>
        </div>
        
    </div>
""", unsafe_allow_html=True)


# 6. PORTFOLIO BRANŻOWE (Interaktywne Zakładki)
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
        fig = go.Figure(data=go.Scattergeo(
            lon = [14.55, -9.13, 11.58, -93.60], 
            lat = [53.42, 38.72, 48.13, 41.60],
            text = ['Baza Operacyjna', 'Węzeł Południowy', 'Centrum Przeładunkowe', 'Trasa Transkontynentalna'],
            mode = 'markers',
            marker = dict(size=12, color='#bda886', line=dict(width=2, color='white'))
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

# 7. STOPKA / KONTAKT - Zmiana koloru stopki
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; padding: 2rem; background-color: #0b213f; border-radius: 15px; color: white;">
        <h2>Gotowy na optymalizację?</h2>
        <p style="color: #a0aec0; margin-bottom: 2rem;">Zaprojektujmy system, który zdejmie z Twojego zespołu powtarzalną pracę.</p>
        <a href="mailto:kontakt@vorteza.local" class="btn-primary" style="background-color: #bda886; box-shadow: none;">Porozmawiajmy o kodzie</a>
    </div>
""", unsafe_allow_html=True)
