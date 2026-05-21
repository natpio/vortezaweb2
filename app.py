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
    page_title="Vorteza Systems | Architektura B2B",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. SYSTEM OBSŁUGI ZASOBÓW (BACKGROUND & ASSETS)
# ==============================================================================
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

set_background('background.jpg')

# ==============================================================================
# 3. ZAAWANSOWANY CSS (DARK GLASSMORPHISM 2.0 - REALISM EDITION)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono&display=swap');
    
    .stApp { font-family: 'Plus Jakarta Sans', sans-serif; }
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1400px; }
    
    /* GŁÓWNY PANEL SZKLANY */
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
        transform: translateY(-4px);
        border: 1px solid rgba(189, 168, 134, 0.4);
        box-shadow: 0 50px 120px rgba(0, 0, 0, 0.8);
    }

    /* HERO SECTION */
    .hero-container { padding: 8rem 4rem; text-align: center; }
    .hero-pretitle { color: #bda886; font-weight: 800; letter-spacing: 5px; text-transform: uppercase; font-size: 0.9rem; margin-bottom: 1.5rem; }
    .hero-main-title { font-size: 4.8rem; font-weight: 800; line-height: 1.05; color: #ffffff; letter-spacing: -2px; margin-bottom: 2rem; text-shadow: 0 15px 40px rgba(0,0,0,0.4); }
    .hero-accent { background: linear-gradient(135deg, #bda886 0%, #ffffff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    /* PRZYCISKI */
    .v-btn-gold {
        background: linear-gradient(135deg, #bda886 0%, #9e8a69 100%);
        color: #0b213f !important; padding: 18px 50px; border-radius: 60px;
        text-decoration: none; font-weight: 900; font-size: 1.2rem;
        display: inline-block; transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(189, 168, 134, 0.4);
        text-transform: uppercase; letter-spacing: 2px;
    }
    .v-btn-gold:hover { transform: scale(1.03); box-shadow: 0 15px 40px rgba(189, 168, 134, 0.6); }

    /* NAGŁÓWKI SEKCJI */
    .v-section-header {
        font-size: 2.2rem; font-weight: 800; color: #ffffff;
        text-align: center; margin: 6rem 0 3rem 0;
        text-transform: uppercase; letter-spacing: 2px;
    }

    /* KARTY */
    .v-card { padding: 3rem; text-align: left; height: 100%; display: flex; flex-direction: column;}
    .v-icon { font-size: 3rem; margin-bottom: 2rem; display: block; }
    .v-title { font-size: 1.6rem; font-weight: 800; color: #ffffff; margin-bottom: 1rem; }
    .v-desc { color: #94a3b8; line-height: 1.7; font-size: 1.05rem; font-weight: 400; }

    /* CUSTOM TABS OVERRIDE DLA STREAMLIT */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.9); border-radius: 20px 20px 0 0;
        padding: 1rem 2rem 0 2rem; border-bottom: 2px solid rgba(189, 168, 134, 0.3);
    }
    .stTabs [data-baseweb="tab"] { height: 70px; color: #64748b; font-weight: 800; font-size: 1.2rem; background: transparent; }
    .stTabs [aria-selected="true"] { color: #bda886 !important; border-bottom-color: #bda886 !important;}
    
    /* FORMULARZ / KONTROLKI */
    .stNumberInput input, .stSelectbox select { background-color: rgba(15, 23, 42, 0.5) !important; color: white !important; border: 1px solid rgba(255,255,255,0.1) !important; font-weight: 600;}
    .stSlider div[data-baseweb="slider"] { padding-top: 1rem; }
    
    /* TABELE WYNIKÓW */
    .result-table { width: 100%; border-collapse: collapse; margin-top: 1rem; color: #ffffff; }
    .result-table th { text-align: left; padding: 12px; border-bottom: 1px solid rgba(255,255,255,0.2); color: #94a3b8; font-weight: 600; font-size: 0.9rem; text-transform: uppercase; }
    .result-table td { padding: 15px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); font-weight: 600; font-size: 1.1rem; }
    .td-highlight { color: #10b981; font-weight: 800; }
    .td-warning { color: #f59e0b; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. STRUKTURA STRONY - SEKCJA HERO
# ==============================================================================
st.markdown("""
    <div class="hero-container">
        <div class="hero-pretitle">Vorteza Systems | Piotr Dukiel</div>
        <h1 class="hero-main-title">Autorskie oprogramowanie B2B.<br><span class="hero-accent">Oparte na twardych danych.</span></h1>
        <p class="v-desc" style="max-width: 850px; margin: 0 auto 3rem auto; color: #cbd5e1; font-size: 1.2rem;">
            Gotowe systemy pudełkowe wymuszają kompromisy. Buduję dedykowaną architekturę cyfrową, 
            która bezbłędnie odwzorowuje Twoje unikalne procesy biznesowe. Koniec z excelem, 
            czas na oprogramowanie, które zabezpiecza Twoje zyski.
        </p>
        <a href="#narzedzia" class="v-btn-gold">Zobacz Architekturę Vorteza</a>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 5. FILARY TECHNOLOGICZNE (THE PILLARS)
# ==============================================================================
st.markdown("<div id='narzedzia'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='v-section-header'>Ekosystem Vorteza</h2>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">🧊 Vorteza Stack</div>
            <div class="v-desc">Solidny fundament danych zintegrowany z Twoim środowiskiem. Moduły są w 100% <b>Offline-Ready</b>, co oznacza, że działają płynnie wewnątrz firmowej sieci, gwarantując najwyższe bezpieczeństwo.</div>
        </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">⚙️ Vorteza Flow</div>
            <div class="v-desc">Logika biznesowa przeniesiona do kodu. Silnik rozpoznaje dychotomię procesów (np. osobne ścieżki dla stałych cenników a inne dla wolnego rynku), automatyzując obieg dokumentacji i zlecenia.</div>
        </div>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
        <div class="v-glass-panel v-card">
            <div class="v-title">🌐 Vorteza Hub</div>
            <div class="v-desc">Interfejs dla kadry zarządzającej. Czytelne moduły (jak TABLICA czy SQM Dispatch) dają pełen wgląd w statusy spraw, obciążenie floty i historię kartotek pacjentów.</div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 6. PRAKTYCZNE NARZĘDZIE: KALKULATOR TCO (STAŁY VS GIEŁDA)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Logika w Praktyce: Dychotomia Przewoźników</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 3rem;">', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="max-width: 900px; margin-bottom: 2.5rem;">
            <h3 style="color: white; font-size: 1.5rem; margin-bottom: 0.5rem;">Moduł: Optymalizacja Wyboru Kontrahenta (Spot vs. Contract)</h3>
            <p style="color: #94a3b8; font-size: 1.1rem; line-height: 1.6;">
                Poniższe narzędzie demonstruje, jak aplikacje Vorteza (np. moduł "TABLICA") automatyzują decyzje dyspozytorskie. 
                Zamiast ręcznych kalkulacji, system wylicza Całkowity Koszt Obsługi (TCO), wliczając w to ukryte koszty ryzyka pracy na wolnym rynku (Giełda) względem zaufanego partnera (Przewoźnik Stały).
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    calc_c1, calc_c2 = st.columns([1, 1.5])
    
    with calc_c1:
        st.markdown("<div style='color: #bda886; font-weight: 800; margin-bottom: 1rem; text-transform: uppercase;'>Parametry Zlecenia</div>", unsafe_allow_html=True)
        distance = st.number_input("Dystans trasy (km):", min_value=100, max_value=5000, value=1250, step=50)
        base_rate = st.number_input("Bazowa stawka stała (EUR/km):", min_value=0.50, max_value=3.00, value=1.15, step=0.05)
        spot_markup = st.slider("Aktualne odchylenie na Giełdzie (% od bazy):", min_value=-20, max_value=50, value=15, step=5)
        risk_premium = st.slider("Współczynnik ryzyka Giełdy (Koszty opóźnień w EUR):", min_value=0, max_value=500, value=150, step=50)
        
    with calc_c2:
        # Obliczenia Logiki Biznesowej
        # 1. Przewoźnik Stały
        cost_contract = distance * base_rate
        time_contract_admin = 2 # minuty (zautomatyzowane Szybkie Zlecenie)
        
        # 2. Przewoźnik Giełdowy (Spot)
        rate_spot = base_rate * (1 + (spot_markup / 100))
        cost_spot_base = distance * rate_spot
        cost_spot_total = cost_spot_base + risk_premium
        time_spot_admin = 25 # minuty (weryfikacja dokumentów, negocjacje, ręczne zlecenia)
        
        # Rekomendacja algorytmiczna
        if cost_contract <= cost_spot_total:
            recommendation = "PRZEWOŹNIK STAŁY"
            rec_color = "#10b981" # Zielony
            savings = cost_spot_total - cost_contract
        else:
            recommendation = "GIEŁDA (SPOT)"
            rec_color = "#f59e0b" # Pomarańczowy
            savings = cost_contract - cost_spot_total
            
        st.markdown(f"""
            <div style="background: rgba(0,0,0,0.2); padding: 2rem; border-radius: 15px; border: 1px solid rgba(255,255,255,0.05);">
                <div style="color: #94a3b8; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 0.5rem; letter-spacing: 1px;">Rekomendacja Systemu Vorteza:</div>
                <div style="font-size: 2rem; font-weight: 900; color: {rec_color}; margin-bottom: 1.5rem;">{recommendation}</div>
                
                <table class="result-table">
                    <thead>
                        <tr>
                            <th>Metryka</th>
                            <th>Przewoźnik Stały</th>
                            <th>Giełda (Spot)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="color: #94a3b8;">Koszt Frachtu</td>
                            <td>{cost_contract:.2f} €</td>
                            <td>{cost_spot_base:.2f} €</td>
                        </tr>
                        <tr>
                            <td style="color: #94a3b8;">Ukryte Ryzyko (TCO)</td>
                            <td style="color: #94a3b8;">0.00 € (Zaufany)</td>
                            <td style="color: #ef4444;">+{risk_premium:.2f} €</td>
                        </tr>
                        <tr>
                            <td style="color: #94a3b8;">Całkowity Koszt (TCO)</td>
                            <td class="{'td-highlight' if cost_contract <= cost_spot_total else ''}">{cost_contract:.2f} €</td>
                            <td class="{'td-warning' if cost_spot_total < cost_contract else ''}">{cost_spot_total:.2f} €</td>
                        </tr>
                        <tr style="border-top: 2px solid rgba(255,255,255,0.1);">
                            <td style="color: #94a3b8;">Czas obsługi adm.</td>
                            <td class="td-highlight">{time_contract_admin} min</td>
                            <td style="color: #ef4444;">{time_spot_admin} min</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 7. BRANŻOWE CASE STUDIES Z TWARDYMI DANYMI
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Realizacje Biznesowe</h2>", unsafe_allow_html=True)

t_log, t_leg, t_med = st.tabs(["🚛 Logistyka Eventowa (Case Study)", "⚖️ Legal-Tech (Obieg Akt)", "⚕️ Med-Tech (Kartoteki)"])

with t_log:
    c_log1, c_log2 = st.columns([1.2, 1])
    with c_log1:
        st.markdown("<h3 style='color: white; margin-top: 0;'>Wdrożenie: Airspace World 2026 (Lizbona)</h3>", unsafe_allow_html=True)
        st.write("Wysokostresowa obsługa logistyczna międzynarodowych targów wymaga perfekcyjnej synchronizacji między magazynem, flotą a klientem.")
        st.markdown("""
        <ul style="color: #cbd5e1; line-height: 1.8; margin-top: 1rem; font-size: 1.05rem;">
            <li><b style="color: white;">Moduł SQM Dispatch:</b> Wdrożenie zautomatyzowanego harmonogramu załadunków i rezerwacji slotów. Eliminacja zjawiska "wąskiego gardła" na rampie magazynowej.</li>
            <li><b style="color: white;">Dokumentacja CMR:</b> Automatyczny generator dokumentów na podstawie stałej bazy adresowej (Komorniki, Barcelona, Lizbona), minimalizujący ryzyko zwrotu ładunku przez błędy w NIP.</li>
            <li><b style="color: white;">Komunikacja z Technikami:</b> Transparentny hub dla zespołu na miejscu (Hubert P., Marcin P.), dający podgląd ETA pojazdów w czasie rzeczywistym.</li>
        </ul>
        """, unsafe_allow_html=True)
    with c_log2:
        # Prawdziwe, twarde dane telemetryczne (Wykres kaskadowy)
        data_case = pd.DataFrame({
            "Etap": ["Wycena Ręczna", "Automatyzacja Vorteza", "Wystawienie Zlecenia", "Generowanie CMR", "Czas Odzyskany"],
            "Minuty": [45, -30, -10, -3, 2],
            "Miara": ["absolute", "relative", "relative", "relative", "total"]
        })
        fig_waterfall = go.Figure(go.Waterfall(
            name = "Optymalizacja", orientation = "v",
            measure = data_case["Miara"],
            x = data_case["Etap"],
            y = data_case["Minuty"],
            connector = {"line":{"color":"rgba(255,255,255,0.2)"}},
            decreasing = {"marker":{"color":"#10b981"}}, # Zielony (Zysk czasu)
            increasing = {"marker":{"color":"#ef4444"}}, # Czerwony (Strata czasu)
            totals = {"marker":{"color":"#bda886"}} # Złoty (Finalny czas)
        ))
        fig_waterfall.update_layout(
            title=dict(text="Redukcja czasu obsługi 1 zlecenia targowego", font=dict(color="white", size=16)),
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0.2)',
            font=dict(color='#cbd5e1'), margin=dict(t=50, b=20, l=20, r=20),
            xaxis=dict(showgrid=False), yaxis=dict(title="Czas (Minuty)", showgrid=True, gridcolor='rgba(255,255,255,0.1)')
        )
        st.plotly_chart(fig_waterfall, use_container_width=True)

with t_leg:
    st.markdown("<h3 style='color: white; margin-top: 0;'>Digitalizacja Obiegu Spraw dla Kancelarii Prawnych</h3>", unsafe_allow_html=True)
    st.write("Dedykowana architektura zapewniająca najwyższe standardy bezpieczeństwa i porządek w skomplikowanych postępowaniach.")
    l_c1, l_c2 = st.columns(2)
    with l_c1:
        st.markdown("<div style='background: rgba(255,255,255,0.05); padding: 2.5rem; border-radius: 15px; height: 100%; border: 1px solid rgba(255,255,255,0.1);'><b style='color: #bda886; font-size: 1.3rem;'>Repozytorium Akt i Pism</b><br><br><span style='color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;'>Lokalne, szyfrowane środowisko eliminujące fizyczny obieg papieru. Zautomatyzowane kategoryzowanie załączników z błyskawicznym indeksem wyszukiwania.</span></div>", unsafe_allow_html=True)
    with l_c2:
        st.markdown("<div style='background: rgba(255,255,255,0.05); padding: 2.5rem; border-radius: 15px; height: 100%; border: 1px solid rgba(255,255,255,0.1);'><b style='color: #bda886; font-size: 1.3rem;'>Ścisła Kontrola Deadlines</b><br><br><span style='color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;'>Algorytmy wyliczające ustawowe terminy odpowiedzi na pisma urzędowe. System aktywnie alertuje zespół prawny o zbliżających się datach krytycznych.</span></div>", unsafe_allow_html=True)

with t_med:
    st.markdown("<h3 style='color: white; margin-top: 0;'>Automatyzacja Administracji w Medycynie Pracy</h3>", unsafe_allow_html=True)
    st.write("Optymalizacja pracy personelu medycznego i zabezpieczenie wrażliwych danych pacjentów.")
    st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-top: 2rem;">
        <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2.5rem 1.5rem; border-radius: 15px; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🗂️</div>
            <b style="color: white; font-size: 1.2rem;">Kartoteka Cyfrowa</b><br>
            <span style="color: #94a3b8; font-size: 1rem; display: block; margin-top: 0.8rem;">Szybkie i zgodne z RODO zarządzanie historią i badaniami pacjentów.</span>
        </div>
        <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2.5rem 1.5rem; border-radius: 15px; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📨</div>
            <b style="color: white; font-size: 1.2rem;">Auto-Skierowania</b><br>
            <span style="color: #94a3b8; font-size: 1rem; display: block; margin-top: 0.8rem;">Moduł błyskawicznie generujący pakiety badań na podstawie kodów stanowisk pracy.</span>
        </div>
        <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2.5rem 1.5rem; border-radius: 15px; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📋</div>
            <b style="color: white; font-size: 1.2rem;">E-Orzecznictwo</b><br>
            <span style="color: #94a3b8; font-size: 1rem; display: block; margin-top: 0.8rem;">Standardyzacja orzeczeń lekarskich z wbudowaną cyfrową archiwizacją.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# 8. PODSTAWY BIZNESOWE (ROI I MATEMATYKA)
# ==============================================================================
st.markdown("<h2 class='v-section-header'>Logika Algorytmiczna</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="v-glass-panel" style="padding: 3rem;">', unsafe_allow_html=True)
    
    m_c1, m_c2 = st.columns([1, 1])
    
    with m_c1:
        st.markdown("<h3 style='color: white;'>Oszczędność Zasobów (FTE)</h3>", unsafe_allow_html=True)
        st.write("Wdrażając oprogramowanie, opieramy się na precyzyjnym wyliczeniu zysku czasu (w pełnych etatyzacjach).")
        
        # Interaktywny mini-kalkulator
        tasks_per_day = st.slider("Powtarzalne operacje dziennie w firmie:", 10, 200, 50, 10)
        time_per_task = st.slider("Średni czas obsługi (minuty):", 2, 30, 15, 1)
        
        saved_hours = ((tasks_per_day * time_per_task) - (tasks_per_day * 1.5)) * 21 / 60
        st.markdown(f"""
            <div style="margin-top: 1rem; padding: 1rem; background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; border-radius: 4px;">
                <span style="color: #cbd5e1; font-size: 1rem;">Twój zysk operacyjny wynosi: </span>
                <span style="color: #ffffff; font-size: 1.4rem; font-weight: bold;">+{int(saved_hours)} godz/miesięcznie</span>
            </div>
        """, unsafe_allow_html=True)

    with m_c2:
        st.markdown("<h3 style='color: white;'>Model Optymalizacji Marży (TCO)</h3>", unsafe_allow_html=True)
        st.write("W Vorteza Flow algorytm matematycznie wylicza ukryte koszty ryzyka (np. na giełdzie transportowej).")
        
        st.markdown("""
        <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; text-align: center; color: #ffffff; font-size: 1.3rem;">
            $$C(x) = B_{rate} \cdot (1 + \Phi(u)) + \frac{\delta \cdot D}{S_{factor}}$$
        </div>
        <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5;">Gdzie: C(x) - wycena całkowita, B - stawka bazowa, Φ(u) - funkcja pilności zlecenia, δ - wskaźnik ryzyka, S - współczynnik stabilności/zaufania do przewoźnika.</p>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 9. KONTAKT I STOPKA (FINAL CTA)
# ==============================================================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="v-glass-panel" style="text-align: center; padding: 6rem 3rem; border-radius: 40px; border: 1px solid rgba(189,168,134,0.3);">
        <h2 style="font-size: 3.5rem; font-weight: 900; color: #ffffff; margin-bottom: 1.5rem; letter-spacing: -1px;">Czas zoptymalizować Twoją firmę.</h2>
        <p style="color: #cbd5e1; font-size: 1.3rem; max-width: 750px; margin: 0 auto 3.5rem auto; line-height: 1.6;">
            Przestań naginać swoje procesy do ograniczeń gotowych, pudełkowych systemów. 
            Stwórzmy dedykowaną architekturę cyfrową, która bezbłędnie rozumie Twój model operacyjny.
        </p>
        <a href="mailto:kontakt@vorteza.local" class="v-btn-gold" style="font-size: 1.25rem; padding: 20px 60px;">Zbudujmy Narzędzia Dla Ciebie</a>
        
        <div style="margin-top: 6rem; display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
            <div style="text-align: left;">
                <span style="color: #bda886; font-weight: 800; font-size: 1.5rem;">Vorteza Systems</span><br>
                <span style="color: #94a3b8; font-size: 0.95rem;">Architektura & Automatyzacja B2B</span>
            </div>
            <div style="text-align: right; color: #94a3b8; font-size: 0.95rem; line-height: 1.6;">
                <b>System:</b> Python • Streamlit • Plotly<br>
                <b>Baza Operacyjna:</b> SQM Prosta Spółka Akcyjna | Komorniki, PL
            </div>
        </div>
    </div>
    <br><br>
""", unsafe_allow_html=True)
