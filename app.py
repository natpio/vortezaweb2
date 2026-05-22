import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import base64
import os

# ==============================================================================
# 1. KONFIGURACJA ŚRODOWISKA I STANU (VORTEZA CORE CONFIG)
# ==============================================================================
st.set_page_config(
    page_title="Vorteza Systems | Oprogramowanie B2B",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. SYSTEM OBSŁUGI ZASOBÓW (BACKGROUND & IMAGES)
# ==============================================================================
def get_base64_of_bin_file(bin_file):
    """Konwersja obrazu do Base64 dla płynnego renderowania CSS/HTML."""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def set_background(png_file):
    """Aplikacja tła premium z gradientem maskującym."""
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: 
                linear-gradient(to right, rgba(11,33,63,0.3) 0%, rgba(11,33,63,0.85) 100%),
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
        st.warning(f"Brak pliku tła: {png_file}")

set_background('background.jpg')

def render_image_html(file_name, alt_text="Screenshot"):
    """Renderuje obraz w szklanej, lewitującej ramce 3D."""
    base64_img = get_base64_of_bin_file(file_name)
    if base64_img:
        # Detekcja rozszerzenia
        ext = "png" if file_name.endswith(".png") else "jpeg"
        return f'''
            <div class="saas-image-wrapper">
                <img src="data:image/{ext};base64,{base64_img}" alt="{alt_text}" class="saas-image">
            </div>
        '''
    return f"<div class='saas-image-wrapper' style='text-align:center; padding:5rem; color:#94a3b8;'>[Brak pliku: {file_name}]</div>"

# ==============================================================================
# 3. ZAAWANSOWANY CSS (ENTERPRISE SAAS SHOWROOM)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800;900&family=JetBrains+Mono&display=swap');
    
    .stApp { font-family: 'Plus Jakarta Sans', sans-serif; }
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1400px; }
    
    /* GŁÓWNY PANEL SZKLANY (GLASSMORPHISM) */
    .v-glass-panel {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 40px 100px rgba(0, 0, 0, 0.5);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        margin-bottom: 2rem;
    }
    .v-glass-panel:hover {
        border: 1px solid rgba(189, 168, 134, 0.3);
        box-shadow: 0 50px 120px rgba(0, 0, 0, 0.7);
    }

    /* RAMKI NA ZRZUTY EKRANU (SHOWCASE 3D) */
    .saas-image-wrapper {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        transition: transform 0.5s ease, box-shadow 0.5s ease;
        background: #0f172a;
    }
    .saas-image-wrapper:hover {
        transform: scale(1.02) translateY(-5px);
        box-shadow: 0 35px 60px -15px rgba(189, 168, 134, 0.3);
        border: 1px solid rgba(189, 168, 134, 0.5);
    }
    .saas-image { width: 100%; height: auto; display: block; }

    /* HERO SECTION */
    .hero-container { padding: 6rem 2rem 8rem 2rem; text-align: center; }
    .hero-pretitle { color: #bda886; font-weight: 900; letter-spacing: 4px; text-transform: uppercase; font-size: 1rem; margin-bottom: 1.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);}
    .hero-main-title { font-size: 5.5rem; font-weight: 900; line-height: 1.1; color: #ffffff; letter-spacing: -2px; margin-bottom: 2rem; text-shadow: 0 20px 50px rgba(0,0,0,0.6); }
    .hero-accent { background: linear-gradient(135deg, #bda886 0%, #ffffff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    /* PRZYCISKI */
    .v-btn-gold {
        background: linear-gradient(135deg, #bda886 0%, #9e8a69 100%);
        color: #0b213f !important; padding: 20px 55px; border-radius: 60px;
        text-decoration: none; font-weight: 900; font-size: 1.25rem;
        display: inline-block; transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(189, 168, 134, 0.4);
        text-transform: uppercase; letter-spacing: 2px;
    }
    .v-btn-gold:hover { transform: scale(1.04); box-shadow: 0 20px 45px rgba(189, 168, 134, 0.6); }

    /* NAGŁÓWKI SEKCJI I KONTENT */
    .v-section-header { font-size: 2.8rem; font-weight: 900; color: #ffffff; text-align: center; margin: 8rem 0 4rem 0; letter-spacing: -1px; text-shadow: 0 5px 15px rgba(0,0,0,0.5);}
    .v-feature-title { font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-bottom: 1.5rem; line-height: 1.2;}
    .v-feature-desc { color: #94a3b8; font-size: 1.2rem; line-height: 1.8; margin-bottom: 2rem; font-weight: 400;}
    
    /* LISTY CECH (FEATURES) */
    .feature-list { list-style: none; padding: 0; margin: 0; }
    .feature-list li { position: relative; padding-left: 2rem; margin-bottom: 1.2rem; color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;}
    .feature-list li::before { content: '✦'; position: absolute; left: 0; top: 2px; color: #bda886; font-size: 1.2rem; }
    .feature-list b { color: #ffffff; font-weight: 800;}

    /* TAGI BRANŻOWE */
    .industry-tag { display: inline-block; padding: 6px 16px; background: rgba(189, 168, 134, 0.15); border: 1px solid rgba(189, 168, 134, 0.4); border-radius: 20px; color: #bda886; font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1.5rem;}
    
    /* CUSTOM TABS OVERRIDE DLA STREAMLIT */
    .stTabs [data-baseweb="tab-list"] { background: rgba(15, 23, 42, 0.8); border-radius: 20px 20px 0 0; padding: 1rem 2rem 0 2rem; border-bottom: 2px solid rgba(189, 168, 134, 0.2); }
    .stTabs [data-baseweb="tab"] { height: 70px; color: #64748b; font-weight: 800; font-size: 1.2rem; background: transparent; }
    .stTabs [aria-selected="true"] { color: #bda886 !important; border-bottom-color: #bda886 !important;}
    
    /* KONTROLKI UI */
    .stNumberInput input, .stSelectbox select { background-color: rgba(15, 23, 42, 0.6) !important; color: white !important; border: 1px solid rgba(255,255,255,0.1) !important; font-weight: 600; border-radius: 8px;}
    
    /* MATHML CONTAINER */
    .math-box { background: rgba(255,255,255,0.02); border-radius: 12px; padding: 2rem; margin: 1rem 0; border-left: 4px solid #bda886; text-align: center; color: #ffffff; font-size: 1.3rem;}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. STRUKTURA STRONY - SEKCJA HERO
# ==============================================================================
st.markdown("""
    <div class="hero-container">
        <div class="hero-pretitle">Vorteza Systems | Piotr Dukiel</div>
        <h1 class="hero-main-title">Architektura Biznesu.<br><span class="hero-accent">Klasy Enterprise.</span></h1>
        <p style="max-width: 900px; margin: 0 auto 3rem auto; color: #cbd5e1; font-size: 1.35rem; line-height: 1.7;">
            Nie koduję z szablonów. Projektuję zaawansowane ekosystemy B2B, które natywnie wspierają 
            najbardziej wymagające procesy operacyjne – od logistyki eventowej, przez zarządzanie kancelarią, 
            aż po pełną administrację placówkami medycznymi.
        </p>
        <a href="#showroom" class="v-btn-gold">Eksploruj Oprogramowanie</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div id='showroom'></div>", unsafe_allow_html=True)

# ==============================================================================
# 5. SHOWROOM PRODUKTOWY: LOGISTYKA & TRANSPORT (TSL)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Logistyka & Łańcuch Dostaw</h2>", unsafe_allow_html=True)

# --- VORTEZA STACK PRO (Planer 3D) ---
with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    c_stack_text, c_stack_img = st.columns([1, 1.4])
    
    with c_stack_text:
        st.markdown("<div class='industry-tag'>Vorteza Stack Pro v26</div>", unsafe_allow_html=True)
        st.markdown("<h3 class='v-feature-title'>Planer Przestrzenny 3D i Utylizacja Floty</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc'>Koniec z szacowaniem miejsca 'na oko'. Silnik algorytmicznie przelicza metry ładowne (LDM), generując precyzyjny manifest załadunkowy i wizualizację dla magazynu.</p>", unsafe_allow_html=True)
        st.markdown("""
            <ul class="feature-list">
                <li><b>Wizualizacja Wolumenu:</b> Renderowanie ułożenia towaru (np. P2.6 Yestech) wewnątrz wybranej naczepy lub solówki.</li>
                <li><b>Matematyka Ładunku:</b> Automatyczne wyliczanie miejsc paletowych, wagi brutto i procentowej utylizacji przestrzeni.</li>
                <li><b>Minimalizacja "Pustych Przebiegów":</b> Algorytm dobiera najmniejszy możliwy pojazd dla zdefiniowanego ładunku.</li>
            </ul>
        """, unsafe_allow_html=True)
        
    with c_stack_img:
        # Wymagany plik: stack3d.jpg
        st.markdown(render_image_html("stack3d.jpg", "Vorteza Stack Pro 3D Planner"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- VORTEZA FLOW (Finanse i Marża) ---
with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    c_flow_img, c_flow_text = st.columns([1.4, 1])
    
    with c_flow_img:
         # Wymagany plik: flow.jpg
        st.markdown(render_image_html("flow.jpg", "Vorteza Flow Profitability"), unsafe_allow_html=True)
        
    with c_flow_text:
        st.markdown("<div class='industry-tag' style='margin-left: 2rem;'>Vorteza Flow</div>", unsafe_allow_html=True)
        st.markdown("<h3 class='v-feature-title' style='padding-left: 2rem;'>Bezwzględna Kontrola Rentowności (BEP)</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc' style='padding-left: 2rem;'>System, który pilnuje Twoich zysków zanim zlecenie wyruszy w trasę. Kompleksowa kalkulacja kosztów zmiennych uwzględniająca dychotomię Przewoźników Stałych i Giełdowych.</p>", unsafe_allow_html=True)
        st.markdown("""
            <ul class="feature-list" style="padding-left: 2rem;">
                <li><b>Struktura Kosztów:</b> Precyzyjny podział na paliwo, myto (przewalutowanie EUR->PLN), serwis, amortyzację oraz koszty kierowcy na trasie i postoju.</li>
                <li><b>Próg Rentowności (BEP):</b> Dynamiczne wyliczanie kosztu przejechania 1 km dla wybranej relacji.</li>
                <li><b>Smart Fuel:</b> Kalkulacja najtańszych stref tankowania (PL vs UE).</li>
            </ul>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SQM DYSPOZYTORNIA (Operacje / Eventy) ---
with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    c_sqm_text, c_sqm_img = st.columns([1, 1.4])
    
    with c_sqm_text:
        st.markdown("<div class='industry-tag'>SQM Dyspozytornia</div>", unsafe_allow_html=True)
        st.markdown("<h3 class='v-feature-title'>Zarządzanie Czasem i Przestrzenią</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc'>Środowisko stworzone do obsługi operacji wysokiego stresu, takich jak montaże na Intersolar Munich czy Airspace World. Pełna synchronizacja floty z magazynem i ekipą techniczną.</p>", unsafe_allow_html=True)
        st.markdown("""
            <ul class="feature-list">
                <li><b>Interaktywny Harmonogram:</b> Kalendarzowy i izometryczny podgląd pracy floty i techników. Idealny do koordynacji trudnych załadunków (np. transport z magazynów SADY, ATM, TSE).</li>
                <li><b>Telemetria Floty:</b> Podział zleceń na dzisiejsze, w trasie i zakończone, z pełnym cyfrowym archiwum zasileń.</li>
                <li><b>Zarządzanie Zespołem:</b> Przypisywanie ról dla kierowców i operatorów na konkretne sloty czasowe.</li>
            </ul>
        """, unsafe_allow_html=True)
        
    with c_sqm_img:
        # Wymagany plik: dyspozytornia.jpg
        st.markdown(render_image_html("dyspozytornia.jpg", "SQM Dyspozytornia Isometric"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 6. SHOWROOM PRODUKTOWY: LEGAL-TECH & MED-TECH
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Zarządzanie i Administracja (Legal & Med)</h2>", unsafe_allow_html=True)

# --- VORTEZA LEX (Kancelarie) ---
with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    c_lex_img, c_lex_text = st.columns([1.4, 1])
    
    with c_lex_img:
        # Wymagany plik: lex.jpg
        st.markdown(render_image_html("lex.jpg", "Vorteza Lex Dashboard"), unsafe_allow_html=True)
        
    with c_lex_text:
        st.markdown("<div class='industry-tag' style='margin-left: 2rem;'>Vorteza Lex</div>", unsafe_allow_html=True)
        st.markdown("<h3 class='v-feature-title' style='padding-left: 2rem;'>Środowisko Pracy Prawnika</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc' style='padding-left: 2rem;'>Zamiana chaosu papierowych akt na ustrukturyzowany, szyfrowany ekosystem, który chroni czas i marżę kancelarii.</p>", unsafe_allow_html=True)
        st.markdown("""
            <ul class="feature-list" style="padding-left: 2rem;">
                <li><b>Live Tracking (Billable Hours):</b> Wbudowany stoper precyzyjnie mierzący czas pracy nad sprawą, błyskawicznie przeliczający go na wypracowany zysk (PLN).</li>
                <li><b>Zadania i Terminy:</b> Cyfrowy kalendarz procesowy powiadamiający o zbliżających się deadlinach ustawowych.</li>
                <li><b>Bezpieczny Rejestr Spraw:</b> Szybkie wyszukiwanie klientów (po numerze lub nazwisku) z natychmiastowym podglądem bazy faktur.</li>
            </ul>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- MEDYCYNA PRACY (Med-Tech) ---
with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    c_med_text, c_med_img = st.columns([1, 1.4])
    
    with c_med_text:
        st.markdown("<div class='industry-tag'>Med-Tech Panel</div>", unsafe_allow_html=True)
        st.markdown("<h3 class='v-feature-title'>Cyfrowa Klinika Medycyny Pracy</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc'>Uwolnienie personelu recepcji i lekarzy od biurokracji. Intuicyjny panel, który przyspiesza proces od rejestracji pacjenta po wydruk orzeczenia.</p>", unsafe_allow_html=True)
        st.markdown("""
            <ul class="feature-list">
                <li><b>Radar Obłożenia:</b> Terminarz wizyt sygnalizujący dni zamknięte i obłożenie placówki, połączony z błyskawicznym umawianiem pacjentów z firm kontraktowych.</li>
                <li><b>Ścisła Prywatność RODO:</b> Wbudowany system autoryzacji oparty na kodach jednorazowych (Google Authenticator / TOTP).</li>
                <li><b>Szybkie Notatki i Akcje:</b> Moduł pozwalający lekarzom i recepcji na płynny przepływ informacji o pacjentach i wygenerowanych dokumentach.</li>
            </ul>
        """, unsafe_allow_html=True)
        
    with c_med_img:
        # Wymagany plik: med.jpg
        st.markdown(render_image_html("med.jpg", "Medycyna Pracy Dashboard"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 7. LOGIKA ALGORYTMICZNA I KALKULATOR TCO (ROI)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Logika Zysku i Automatyzacji</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    
    roi_c1, roi_c2 = st.columns([1.2, 1])
    
    with roi_c1:
        st.markdown("<h3 class='v-feature-title'>Ile kosztuje Cię praca ręczna?</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc' style='margin-bottom: 2rem;'>Wdrażając oprogramowanie klasy Vorteza, opieramy się na precyzyjnym wyliczeniu zysku czasu (w pełnych etatyzacjach). Sprawdź, ile godzin odzyskasz automatyzując powtarzalne procesy operacyjne.</p>", unsafe_allow_html=True)
        
        # Interaktywny Kalkulator
        tasks_per_day = st.slider("Liczba powtarzalnych operacji dziennie (np. wycena, zlecenie, pismo, orzeczenie):", min_value=10, max_value=300, value=80, step=10)
        time_per_task = st.slider("Obecny średni czas ręcznej obsługi 1 operacji (minuty):", min_value=2, max_value=45, value=12, step=1)
        
        # Logika
        manual_time_per_day = tasks_per_day * time_per_task
        vorteza_time_per_task = 1.5 # Zakładany czas w systemie zautomatyzowanym
        vorteza_time_per_day = tasks_per_day * vorteza_time_per_task
        
        saved_hours_per_month = ((manual_time_per_day - vorteza_time_per_day) * 21) / 60 
        saved_fte = saved_hours_per_month / 160 
        
    with roi_c2:
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 3rem; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center; box-shadow: 0 10px 30px rgba(16, 185, 129, 0.1);">
                <div style="color: #10b981; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem; font-weight: 900;">Zaoszczędzony czas zespołu</div>
                <div style="color: #ffffff; font-size: 4.5rem; font-weight: 900; line-height: 1; text-shadow: 0 5px 15px rgba(0,0,0,0.3);">+{int(saved_hours_per_month)} <span style="font-size: 1.5rem; color: #10b981;">godz. / mies.</span></div>
                
                <hr style="border-top: 1px solid rgba(16, 185, 129, 0.2); margin: 2rem 0;">
                
                <div style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;">
                    To odzyskana przepustowość równa <b>{saved_fte:.1f} pełnym etatom (FTE)</b>.<br>
                    Czas, który Twoi pracownicy mogą przeznaczyć na skalowanie biznesu, zamiast na rutynową biurokrację.
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 4rem;">', unsafe_allow_html=True)
    
    math_c1, math_c2 = st.columns([1, 1])
    with math_c1:
        st.markdown("<h3 class='v-feature-title'>Model Optymalizacji Marży (TCO)</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc'>W modułach takich jak Vorteza Flow, algorytm używa poniższego modelu do dynamicznego zabezpieczania marży, wliczając ryzyko podejmowane przy zleceniach na rynku Spot.</p>", unsafe_allow_html=True)
        st.markdown("""
        <div class="math-box">
            $$C(x) = B_{rate} \cdot (1 + \Phi(u)) + \frac{\delta \cdot D}{S_{factor}}$$
        </div>
        <p style="font-size: 0.9rem; color: #94a3b8; line-height: 1.6;">Gdzie: C(x) - wycena całkowita, B - stawka bazowa, Φ(u) - funkcja pilności, δ - wskaźnik ryzyka, S - współczynnik stabilności (Kontraktowy vs. Giełdowy).</p>
        """, unsafe_allow_html=True)

    with math_c2:
        st.markdown("<h3 class='v-feature-title'>Globalny Zasięg Operacji</h3>", unsafe_allow_html=True)
        st.markdown("<p class='v-feature-desc'>Systemy te były projektowane dla operacji przekraczających granice kontynentów, od transportów eventowych w Europie, po trasy transatlantyckie.</p>", unsafe_allow_html=True)
        
        # Prawdziwe operacje z historii użytkownika
        fig_map = go.Figure()
        lons = [16.80, -9.13, 11.58, -93.62] 
        lats = [52.34, 38.72, 48.13, 41.58]
        names = ['Komorniki (HQ)', 'Airspace World (PT)', 'Intersolar (DE)', 'Legendary Midwest Route']
        
        for i in range(1, len(lons)):
            fig_map.add_trace(go.Scattergeo(lon = [lons[0], lons[i]], lat = [lats[0], lats[i]], mode = 'lines', line = dict(width = 2, color = '#bda886'), opacity=0.7))

        fig_map.add_trace(go.Scattergeo(lon = lons, lat = lats, text = names, mode = 'markers+text', textposition="top right", textfont=dict(color="#ffffff", size=11, family="Plus Jakarta Sans"), marker=dict(size=12, color='#bda886')))
        fig_map.update_layout(geo=dict(projection_type="orthographic", bgcolor="rgba(0,0,0,0)", showland=True, landcolor="#1e293b", showocean=True, oceancolor="rgba(0,0,0,0)"), margin=dict(l=0, r=0, t=0, b=0), height=300, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_map, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 8. KONTAKT I STOPKA (FINAL CTA)
# ==============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="v-glass-panel" style="text-align: center; padding: 7rem 3rem; border-radius: 40px; border: 1px solid rgba(189,168,134,0.4);">
        <h2 style="font-size: 3.8rem; font-weight: 900; color: #ffffff; margin-bottom: 1.5rem; letter-spacing: -1px; line-height: 1.1;">Twoja firma jest gotowa <br>na oprogramowanie tej klasy.</h2>
        <p style="color: #cbd5e1; font-size: 1.3rem; max-width: 800px; margin: 0 auto 4rem auto; line-height: 1.7;">
            Zapomnij o rozwiązaniach, które wymagają szkolenia personelu z obsługi przestarzałych formularzy. 
            Zbudujmy system, który wyrasta bezpośrednio z Twoich potrzeb operacyjnych.
        </p>
        <a href="mailto:kontakt@vorteza.local" class="v-btn-gold" style="font-size: 1.3rem; padding: 22px 70px;">Rozpocznij Projekt</a>
        
        <div style="margin-top: 7rem; display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2.5rem;">
            <div style="text-align: left;">
                <span style="color: #bda886; font-weight: 900; font-size: 1.8rem; letter-spacing: 1px;">Vorteza Systems</span><br>
                <span style="color: #94a3b8; font-size: 1.05rem;">Enterprise B2B Architecture</span>
            </div>
            <div style="text-align: right; color: #94a3b8; font-size: 1rem; line-height: 1.7;">
                <b>Stack Technologiczny:</b> Python • Streamlit • Cloud Native<br>
                <b>Baza Operacyjna:</b> SQM S.A. | Komorniki, PL
            </div>
        </div>
    </div>
    <br><br>
""", unsafe_allow_html=True)
