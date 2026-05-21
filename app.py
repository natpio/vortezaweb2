import streamlit as st
import plotly.graph_objects as go
import base64
import os

# 1. KONFIGURACJA STRONY (Zmniejszenie domyślnych marginesów)
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
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: 
                linear-gradient(to right, rgba(11,33,63,0.1) 0%, rgba(11,33,63,0.4) 100%),
                url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.jpg')

# 3. ZAAWANSOWANY CSS - POZIOM PRO (DARK GLASSMORPHISM)
st.markdown("""
    <style>
    /* Reset i fonty */
    .stApp { font-family: 'Inter', 'Segoe UI', sans-serif; }
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    
    /* Optymalizacja marginesów górnych Streamlit */
    .block-container { padding-top: 3rem; padding-bottom: 2rem; max-width: 1200px; }
    
    /* DARK GLASSMORPHISM - Luksusowe ciemne panele */
    .glass-panel {
        background: rgba(15, 23, 42, 0.65); /* Głęboki, elegancki granat/czerń */
        backdrop-filter: blur(16px) saturate(120%);
        -webkit-backdrop-filter: blur(16px) saturate(120%);
        border-radius: 20px;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.2); /* Subtelne odbicie światła na krawędzi */
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
        color: #ffffff;
    }
    .glass-panel:hover {
        transform: translateY(-8px);
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(189, 168, 134, 0.4); /* Złota poświata ramki przy najechaniu */
    }
    
    /* Typografia dla ciemnego tła */
    .text-white { color: #ffffff; }
    .text-accent { color: #bda886; } /* Szlachetne złoto */
    .text-muted-light { color: #94a3b8; }
    
    /* Sekcja Hero */
    .hero-box { padding: 6rem 4rem; text-align: center; margin: 0 auto 5rem auto; max-width: 1000px; }
    .hero-title { font-size: 4rem; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 1.5rem; line-height: 1.1; text-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    .hero-subtitle { font-size: 1.25rem; max-width: 800px; margin: 0 auto 3rem auto; line-height: 1.8; font-weight: 400; color: #cbd5e1; }
    
    /* Przyciski PRO - Złoty Glow */
    .btn-primary {
        background: linear-gradient(135deg, #bda886 0%, #9e8a69 100%);
        color: #0b213f !important;
        padding: 16px 42px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 900;
        font-size: 1.15rem;
        transition: all 0.3s ease;
        display: inline-block;
        border: none;
        box-shadow: 0 10px 25px rgba(189, 168, 134, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .btn-primary:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 35px rgba(189, 168, 134, 0.6);
        color: #000000 !important;
    }
    
    /* Nagłówki sekcji - styl "Badge" dla perfekcyjnego kontrastu */
    .section-header-wrapper { text-align: center; margin: 5rem 0 3rem 0; }
    .section-header {
        display: inline-block;
        background: rgba(15, 23, 42, 0.8);
        padding: 10px 30px;
        border-radius: 50px;
        color: #bda886;
        font-size: 1.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 3px;
        border: 1px solid rgba(189, 168, 134, 0.3);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Karty Modułów */
    .module-card { padding: 3rem 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-start; }
    .module-icon { font-size: 3rem; margin-bottom: 1.5rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4)); }
    .module-title { font-weight: 800; font-size: 1.6rem; margin-bottom: 1rem; color: #ffffff; }
    .module-desc { line-height: 1.7; font-size: 1.05rem; }
    
    /* ZAKŁADKI PRO - Przebudowa Streamlit Tabs */
    div[data-baseweb="tabs"] { width: 100%; }
    div[data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(16px);
        border-radius: 20px 20px 0 0;
        padding: 1rem 2rem 0 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(189, 168, 134, 0.3);
        gap: 30px;
    }
    div[data-baseweb="tab-panel"] {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        border-radius: 0 0 20px 20px;
        padding: 3rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: none;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
        color: #ffffff;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: transparent; border-radius: 0;
        color: #94a3b8; font-weight: 800; font-size: 1.1rem; border-bottom: 3px solid transparent;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover { color: #ffffff; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: transparent; }
    .stTabs [aria-selected="true"] { color: #bda886 !important; border-bottom: 3px solid #bda886 !important; }
    
    /* Listy w zakładkach */
    ul.pro-list { padding-left: 1.5rem; }
    ul.pro-list li { margin-bottom: 1rem; color: #cbd5e1; }
    ul.pro-list b { color: #ffffff; }
    
    /* Pasek Przewijania */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #0b213f; }
    ::-webkit-scrollbar-thumb { background: #bda886; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 4. HERO SECTION
html_hero = """
    <div class="glass-panel hero-box">
        <h1 class="hero-title text-white">Praktyka biznesowa.<br><span class="text-accent">Zamieniona w kod.</span></h1>
        <p class="hero-subtitle">
            Vorteza Systems to oprogramowanie B2B skrojone na miarę. Narzędzia, które tworzę, 
            wyrastają z lat realnych doświadczeń operacyjnych. Przekształcam wąskie gardła w logistyce, 
            prawie i medycynie pracy w zautomatyzowane, wydajne ekosystemy gotowe do pracy w chmurze i offline.
        </p>
        <a href="#architektura" class="btn-primary">Poznaj Architekturę</a>
    </div>
"""
st.markdown(html_hero, unsafe_allow_html=True)

# 5. ARCHITEKTURA (FILARY VORTEZA)
st.markdown("<div id='architektura' class='section-header-wrapper'><div class='section-header'>Trzy Filary Vorteza</div></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

html_card1 = """<div class="glass-panel module-card"><div class="module-icon">🧊</div><div class="module-title">Vorteza Stack</div><div class="module-desc text-muted-light">Fundament danych. Solidna i bezpieczna infrastruktura backendowa. Pełna gotowość do wdrożeń lokalnych (Offline-Ready) w biurze oraz płynna integracja z narzędziami klasy Google Sheets.</div></div>"""
col1.markdown(html_card1, unsafe_allow_html=True)

html_card2 = """<div class="glass-panel module-card"><div class="module-icon">⚙️</div><div class="module-title">Vorteza Flow</div><div class="module-desc text-muted-light">Automatyzacja procesów. Silnik zamieniający skomplikowane logiki biznesowe, od dysponowania flotą po obieg dokumentacji prawnej, w proste i błyskawiczne przepływy pracy.</div></div>"""
col2.markdown(html_card2, unsafe_allow_html=True)

html_card3 = """<div class="glass-panel module-card"><div class="module-icon">🌐</div><div class="module-title">Vorteza Hub</div><div class="module-desc text-muted-light">Centrum integracji i dowodzenia. Ujednolicony interfejs dający kadrze zarządzającej podgląd operacji w czasie rzeczywistym. Od monitorowania tras po statusy spraw pacjentów.</div></div>"""
col3.markdown(html_card3, unsafe_allow_html=True)

# 6. PORTFOLIO BRANŻOWE
st.markdown("<div class='section-header-wrapper'><div class='section-header'>Zrealizowane Ekosystemy</div></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚛 Logistyka & Transport", "⚖️ Usługi Prawne", "⚕️ Medycyna Pracy"])

with tab1:
    st.markdown("<h2 style='color:#ffffff; font-weight:800; margin-top:0;'>Automatyzacja procesów transportowych i spedycyjnych</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#cbd5e1; font-size:1.1rem; margin-bottom: 2rem;'>Wielomodułowe rozwiązania usprawniające codzienną pracę dyspozytorów i spedytorów. Stworzone do obsługi wymagających operacji na rynkach międzynarodowych.</p>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1.2, 1])
    with col_a:
        st.markdown("""
        <ul class='pro-list'>
            <li><b>SQM Dispatch:</b> Pełna kontrola nad flotą, zarządzanie kierowcami i śledzenie statusów.</li>
            <li><b>TABLICA:</b> Centralny system zarządzania danymi. Osobne, zautomatyzowane przepływy pracy dla <i>Przewoźników Stałych</i> oraz <i>Przewoźników Giełdowych</i>.</li>
            <li><b>Szybkie Zlecenie:</b> Błyskawiczne generowanie dokumentacji uwzględniające elastyczne i stałe cenniki.</li>
        </ul>
        """, unsafe_allow_html=True)
        
    with col_b:
        # ZAAWANSOWANY GLOBUS 3D Z TRASAMI LOGISTYCZNYMI (PRO LEVEL)
        lons = [14.55, -9.13, 11.58, -93.60]
        lats = [53.42, 38.72, 48.13, 41.60]
        
        fig = go.Figure()
        
        # Linie tras (Połączenia węzłów)
        for i in range(1, len(lons)):
            fig.add_trace(go.Scattergeo(
                lon = [lons[0], lons[i]], lat = [lats[0], lats[i]],
                mode = 'lines', line = dict(width = 2, color = '#bda886'),
                opacity = 0.6, hoverinfo='skip'
            ))

        # Punkty (Węzły operacyjne)
        fig.add_trace(go.Scattergeo(
            lon = lons, lat = lats,
            text = ['Baza Operacyjna (PL)', 'Węzeł Południowy (PT)', 'Centrum Przeładunkowe (DE)', 'Trasa Transkontynentalna (US)'],
            mode = 'markers+text',
            textposition="top center",
            textfont=dict(color="rgba(255,255,255,0.7)", size=10),
            marker = dict(size=14, color='#bda886', line=dict(width=3, color='rgba(15, 23, 42, 0.8)'))
        ))

        fig.update_layout(
            showlegend=False,
            geo = dict(
                projection_type="orthographic", 
                showland=True, landcolor="rgba(255, 255, 255, 0.05)", # Przezroczyste, techniczne kontynenty
                showocean=True, oceancolor="rgba(0,0,0,0)",
                showcountries=True, countrycolor="rgba(255,255,255,0.1)",
                bgcolor="rgba(0,0,0,0)",
                resolution=50
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("<h2 style='color:#ffffff; font-weight:800; margin-top:0;'>Dedykowany system dla Kancelarii Prawnych</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='pro-list' style='margin-top: 1.5rem;'>
        <li><b>Bezpieczeństwo akt:</b> Szyfrowane repozytorium załączników i dokumentacji procesowej.</li>
        <li><b>Generator Pism:</b> Automatyzacja tworzenia powtarzalnych dokumentów na podstawie zmiennych danych.</li>
        <li><b>Kontrola Terminów:</b> Cyfrowe zarządzanie kalendarzem spraw i rygorystyczne śledzenie kluczowych terminów (deadlines).</li>
    </ul>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h2 style='color:#ffffff; font-weight:800; margin-top:0;'>Zarządzanie kartoteką w Medycynie Pracy</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='pro-list' style='margin-top: 1.5rem;'>
        <li><b>Bazy Danych:</b> Uporządkowana, cyfrowa kartoteka pacjentów zachowująca najwyższe standardy prywatności.</li>
        <li><b>Automatyzacja Skierowań:</b> Szybkie generowanie i obieg dokumentów na badania specjalistyczne.</li>
        <li><b>Orzecznictwo:</b> Błyskawiczne wystawianie, archiwizacja i weryfikacja orzeczeń lekarskich.</li>
    </ul>
    """, unsafe_allow_html=True)

# 7. STOPKA PRO
st.markdown("<br><br><br>", unsafe_allow_html=True)
html_footer = """
    <div class="glass-panel" style="text-align: center; padding: 4rem 2rem; margin: 0 auto; max-width: 800px; border-radius: 30px;">
        <h2 style="font-weight: 900; margin-bottom: 1rem; color: #ffffff; font-size: 2.5rem;">Gotowy na optymalizację?</h2>
        <p style="color: #cbd5e1; margin-bottom: 3rem; font-size: 1.2rem;">Zaprojektujmy system, który zdejmie z Twojego zespołu powtarzalną pracę operacyjną.</p>
        <a href="mailto:kontakt@vorteza.local" class="btn-primary">Porozmawiajmy o kodzie</a>
        
        <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; text-align: left;">
            <div>
                <span style="color: #bda886; font-weight: bold; font-size: 1.2rem;">Vorteza Systems</span><br>
                <span style="color: #64748b; font-size: 0.9rem;">Architektura Rozwiązań B2B</span>
            </div>
            <div style="text-align: right; color: #64748b; font-size: 0.9rem;">
                <b>Baza Operacyjna:</b><br>
                SQM Prosta Spółka Akcyjna<br>
                Komorniki, Polska
            </div>
        </div>
    </div>
    <br><br>
"""
st.markdown(html_footer, unsafe_allow_html=True)
