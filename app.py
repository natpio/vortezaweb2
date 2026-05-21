import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# 1. KONFIGURACJA STRONY
st.set_page_config(
    page_title="Vorteza Systems | Portfolio",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. FUNKCJA ŁADUJĄCA TŁO Z KINOWYM FILTREM (OVERLAY)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    if os.path.exists(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        # Dodany linear-gradient maskujący kompresję tła i poprawiający kontrast
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: 
                linear-gradient(to right, rgba(255,255,255,0.05) 0%, rgba(11,33,63,0.5) 100%),
                url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.warning("Prześlij plik 'background.jpg' do repozytorium, aby zobaczyć tło.")

set_background('background2.png')

# 3. ZAAWANSOWANY CSS (Glassmorphism & Naprawa Zakładek)
st.markdown("""
    <style>
    /* Globalne czcionki */
    .stApp {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    
    /* GLASSMORPHISM - Szklane panele */
    .glass-panel {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(189, 168, 134, 0.5);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-panel:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(189, 168, 134, 0.8);
    }
    
    /* Teksty */
    .text-dark { color: #0b213f; }
    .text-accent { color: #bda886; }
    .text-muted { color: #4a5568; }
    
    /* Sekcja Hero */
    .hero-box { padding: 5rem 3rem; text-align: center; margin: 2rem auto 4rem auto; max-width: 900px; }
    .hero-title { font-size: 3.5rem; font-weight: 900; letter-spacing: -1px; margin-bottom: 1.5rem; line-height: 1.2; }
    .hero-subtitle { font-size: 1.2rem; max-width: 750px; margin: 0 auto 2.5rem auto; line-height: 1.7; font-weight: 500; }
    
    /* Przyciski */
    .btn-primary {
        background-color: #bda886; color: #0b213f !important; padding: 14px 36px; border-radius: 50px;
        text-decoration: none; font-weight: 800; font-size: 1.1rem; transition: all 0.3s ease;
        display: inline-block; border: 2px solid #bda886; box-shadow: 0 4px 15px rgba(189, 168, 134, 0.3);
    }
    .btn-primary:hover { background-color: transparent; color: #ffffff !important; background: rgba(11, 33, 63, 0.9); transform: translateY(-2px); }
    
    /* Nagłówki sekcji */
    .section-header { text-align: center; color: #ffffff; font-size: 2.5rem; font-weight: 900; margin: 4rem 0 2.5rem 0; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 4px 15px rgba(0,0,0,0.6); }
    
    /* Karty Modułów */
    .module-card { padding: 2.5rem 2rem; height: 100%; }
    .module-icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .module-title { font-weight: 800; font-size: 1.4rem; margin-bottom: 1rem; }
    
    /* NAPRAWA: ZAKŁADKI I ICH ZAWARTOŚĆ W SZKLE */
    div[data-baseweb="tabs"] {
        background: transparent;
    }
    div[data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border-radius: 15px 15px 0 0;
        padding: 1rem 2rem 0 2rem;
        border: 1px solid rgba(189, 168, 134, 0.5);
        border-bottom: none;
        gap: 24px;
    }
    div[data-baseweb="tab-panel"] {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border-radius: 0 0 15px 15px;
        padding: 2rem;
        border: 1px solid rgba(189, 168, 134, 0.5);
        border-top: none;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: transparent;
        border-radius: 4px; color: #0b213f; font-weight: 800;
    }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #bda886; }
    </style>
""", unsafe_allow_html=True)

# 4. HERO SECTION
html_hero = """
    <div class="glass-panel hero-box text-dark">
        <h1 class="hero-title text-dark">Praktyka biznesowa.<br><span class="text-accent">Zamieniona w kod.</span></h1>
        <p class="hero-subtitle text-muted">
            Vorteza Systems to oprogramowanie B2B skrojone na miarę. Narzędzia, które tworzę, 
            wyrastają z lat realnych doświadczeń operacyjnych. Przekształcam wąskie gardła w logistyce, 
            prawie i medycynie pracy w zautomatyzowane, wydajne ekosystemy gotowe do pracy w chmurze i offline.
        </p>
        <a href="#architektura" class="btn-primary">Poznaj Architekturę</a>
    </div>
"""
st.markdown(html_hero, unsafe_allow_html=True)

# 5. ARCHITEKTURA (FILARY VORTEZA)
st.markdown("<h2 id='architektura' class='section-header'>Trzy Filary Vorteza</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

html_card1 = """<div class="glass-panel module-card"><div class="module-icon">🧊</div><div class="module-title text-dark">Vorteza Stack</div><div class="text-muted">Fundament danych. Solidna i bezpieczna infrastruktura backendowa. Pełna gotowość do wdrożeń lokalnych (Offline-Ready) w biurze oraz płynna integracja z narzędziami klasy Google Sheets.</div></div>"""
col1.markdown(html_card1, unsafe_allow_html=True)

html_card2 = """<div class="glass-panel module-card"><div class="module-icon">⚙️</div><div class="module-title text-dark">Vorteza Flow</div><div class="text-muted">Automatyzacja procesów. Silnik zamieniający skomplikowane logiki biznesowe, od dysponowania flotą po obieg dokumentacji prawnej, w proste i błyskawiczne przepływy pracy.</div></div>"""
col2.markdown(html_card2, unsafe_allow_html=True)

html_card3 = """<div class="glass-panel module-card"><div class="module-icon">🌐</div><div class="module-title text-dark">Vorteza Hub</div><div class="text-muted">Centrum integracji i dowodzenia. Ujednolicony interfejs dający kadrze zarządzającej podgląd operacji w czasie rzeczywistym. Od monitorowania tras po statusy spraw pacjentów.</div></div>"""
col3.markdown(html_card3, unsafe_allow_html=True)

# 6. PORTFOLIO BRANŻOWE
st.markdown("<h2 class='section-header'>Zrealizowane Ekosystemy</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚛 Logistyka & Transport", "⚖️ Usługi Prawne", "⚕️ Medycyna Pracy"])

with tab1:
    st.markdown("<h3 class='text-dark' style='margin-top:0;'>Automatyzacja procesów transportowych i spedycyjnych</h3>", unsafe_allow_html=True)
    st.markdown("<p class='text-muted'>Wielomodułowe rozwiązania usprawniające codzienną pracę dyspozytorów i spedytorów. Stworzone do obsługi wymagających operacji na rynkach międzynarodowych.</p>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.markdown("""
        <div class='text-dark' style='margin-top: 1rem;'>
        <ul style='line-height: 1.8;'>
            <li><b>SQM Dispatch:</b> Pełna kontrola nad flotą, zarządzanie kierowcami i śledzenie statusów.</li>
            <li><b>TABLICA:</b> Centralny system zarządzania danymi. Osobne, zautomatyzowane przepływy pracy dla <i>Przewoźników Stałych</i> oraz <i>Przewoźników Giełdowych</i>.</li>
            <li><b>Szybkie Zlecenie:</b> Błyskawiczne generowanie dokumentacji uwzględniające elastyczne i stałe cenniki.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        fig = go.Figure(data=go.Scattergeo(
            lon = [14.55, -9.13, 11.58, -93.60], 
            lat = [53.42, 38.72, 48.13, 41.60],
            text = ['Centrala Operacyjna', 'Węzeł Południowy', 'Centrum Przeładunkowe', 'Trasa Transkontynentalna'],
            mode = 'markers',
            marker = dict(size=12, color='#bda886', line=dict(width=2, color='#0b213f'))
        ))
        fig.update_layout(
            geo = dict(
                projection_type="orthographic", 
                showland=True, 
                landcolor="#e5e2da", 
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
    st.markdown("<h3 class='text-dark' style='margin-top:0;'>Dedykowany system dla Kancelarii Prawnych</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='text-dark' style='margin-top: 1rem;'>
    <ul style='line-height: 1.8;'>
        <li>Bezpieczne repozytorium akt i załączników.</li>
        <li>Automatyzacja generowania powtarzalnych dokumentów i pism procesowych.</li>
        <li>Cyfrowe zarządzanie kalendarzem spraw i śledzenie kluczowych terminów (deadlines).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 class='text-dark' style='margin-top:0;'>Zarządzanie kartoteką w Medycynie Pracy</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='text-dark' style='margin-top: 1rem;'>
    <ul style='line-height: 1.8;'>
        <li>Uporządkowana, cyfrowa baza danych pacjentów zachowująca najwyższe standardy prywatności.</li>
        <li>Automatyzacja procesu generowania skierowań na badania.</li>
        <li>Szybkie wystawianie i archiwizacja orzeczeń lekarskich.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# 7. STOPKA
st.markdown("<br><br>", unsafe_allow_html=True)
html_footer = """
    <div class="glass-panel text-dark" style="text-align: center; padding: 2.5rem; margin: 0 auto; max-width: 700px;">
        <h2 style="font-weight: 900; margin-bottom: 0.5rem; color: #0b213f;">Gotowy na optymalizację?</h2>
        <p class="text-muted" style="margin-bottom: 2rem; font-size: 1.1rem;">Zaprojektujmy system, który zdejmie z Twojego zespołu powtarzalną pracę.</p>
        <a href="mailto:kontakt@vorteza.local" class="btn-primary">Porozmawiajmy o kodzie</a>
        
        <hr style="border-top: 1px solid rgba(189, 168, 134, 0.3); margin: 2rem 0 1rem 0;">
        <div style="font-size: 0.85rem; color: #4a5568;">
            <b>Projekt:</b> Vorteza Systems<br>
            <b>Baza Operacyjna:</b> SQM Prosta Spółka Akcyjna, Komorniki
        </div>
    </div>
    <br><br>
"""
st.markdown(html_footer, unsafe_allow_html=True)
