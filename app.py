# app.py
# ============================================================
# GEOPOLITICAL OIL IMPACT ANALYSIS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Geopolitical Oil Impact Analysis",
    page_icon="🌍",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

h1, h2, h3 {
    color: #0f172a;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

.insight-box {
    background-color: #ffffff;
    padding: 18px;
    border-left: 6px solid #2563eb;
    border-radius: 10px;
    margin-bottom: 20px;
}

.big-font {
    font-size:20px !important;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Project Overview",
        "📈 Market Timeline",
        "🔥 Extreme Market Movements",
        "🤖 Machine Learning Insights",
        "📉 Forecasting",
        "📊 Correlation Analysis",
        "🌍 Economic Impact Simulator",   # FIX 2: Simulator is now its own page
        "💡 Final Insights"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    This dashboard analyzes how geopolitical conflicts impact:

    - Brent Crude Oil
    - Indian Rupee (INR)
    - NIFTY 50

    using Data Science & Machine Learning.
    """
)

# ============================================================
# TITLE
# ============================================================

st.title("🌍 Geopolitical Impact on Oil & Indian Economy")
st.markdown(
    """
    ### Using Data Science & Machine Learning to Analyze:
    - Oil Price Volatility
    - INR/USD Movements
    - Indian Stock Market Reactions
    - War & Conflict Impact
    """
)

# ============================================================
# FIX 1: SAFE IMAGE LOADING
# Images are loaded inside a function with try/except.
# If a PNG file is missing, the app shows a clear warning
# instead of crashing with FileNotFoundError.
# ============================================================

def load_image(filename):
    if os.path.exists(filename):
        return Image.open(filename)
    return None

def show_image(img, filename):
    if img is not None:
        st.image(img, width=900)
    else:
        st.warning(
            f"Image '{filename}' not found. "
            "Run the notebook first to generate all plots."
        )
timeline_img  = load_image("plots/plot_price_timeline.png")
corr_img      = load_image("plots/plot_correlation.png")
fat_tail_img  = load_image("plots/plot_return_distributions.png")
feature_img   = load_image("plots/plot_feature_importance.png")
forecast_img  = load_image("plots/plot_arima_forecast.png")

# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "🏠 Project Overview":

    st.header("📌 Project Objective")

    st.markdown("""
    <div class="insight-box">
    This project studies how major geopolitical conflicts affect:

    ✅ Global Oil Prices<br>
    ✅ Indian Currency (INR/USD)<br>
    ✅ Indian Stock Market (NIFTY 50)<br><br>

    The analysis combines:
    - Time Series Analysis
    - Machine Learning
    - Economic Analysis
    - Financial Risk Analysis
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Oil Data", "2020 - 2026")

    with col2:
        st.metric("Forecast Accuracy", "MAE = $0.25")

    with col3:
        st.metric("ML Features Used", "11")

    st.markdown("---")

    st.subheader("🌍 Major Events Included")

    events = pd.DataFrame({
        "Event": [
            "COVID-19 Pandemic",
            "Russia-Ukraine War",
            "Israel-Hamas Conflict",
            "Iran-Israel Tensions",
            "US-Iran Escalation"
        ],
        "Impact": [
            "Oil crash & volatility",
            "Global energy shock",
            "Middle East uncertainty",
            "Supply chain concerns",
            "Oil market instability"
        ]
    })

    st.table(events)

# ============================================================
# MARKET TIMELINE
# ============================================================

elif page == "📈 Market Timeline":

    st.header("📈 Oil, INR & NIFTY Timeline")

    st.markdown("""
    This visualization shows how geopolitical events affected:

    - Brent Crude Oil
    - Indian Rupee
    - NIFTY 50 Index
    """)

    show_image(timeline_img, "plot_price_timeline.png")

    st.markdown("""
    <div class="insight-box">

    <span class="big-font">Key Insights:</span>

    - Oil prices surged during global conflicts
    - INR weakened when oil became expensive
    - Indian markets showed resilience after shocks
    - Geopolitical instability increases market volatility

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FAT TAIL ANALYSIS
# ============================================================

elif page == "🔥 Extreme Market Movements":

    st.header("🔥 Extreme Market Movement Analysis")

    st.markdown("""
    Financial markets do not behave normally during crises.

    This chart shows:
    - Extreme price jumps
    - Volatility spikes
    - Fat-tail behavior in markets
    """)

    show_image(fat_tail_img, "plot_return_distributions.png")

    st.markdown("""
    <div class="insight-box">

    <span class="big-font">What Does This Mean?</span>

    During geopolitical conflicts:

    - Oil prices can move abnormally fast
    - Market crashes happen more often
    - Risk increases sharply
    - Traditional assumptions fail

    This is called "Fat Tail Risk".

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# MACHINE LEARNING PAGE
# ============================================================

elif page == "🤖 Machine Learning Insights":

    st.header("🤖 Machine Learning Analysis")

    st.markdown("""
    A Machine Learning model was trained to understand:

    > What factors most strongly predict oil price direction?
    """)

    show_image(feature_img, "plot_feature_importance.png")

    st.markdown("""
    <div class="insight-box">

    <span class="big-font">Main Findings:</span>

    ✅ Oil returns were the strongest predictor<br>
    ✅ Currency movement (INR/USD) mattered<br>
    ✅ Historical lag values improved predictions<br>
    ✅ News sentiment had lower impact than expected

    </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Features Used")

    features = pd.DataFrame({
        "Feature": [
            "oil_return",
            "month",
            "inr_return",
            "oil_volatility",
            "lag_features",
            "news_sentiment"
        ],
        "Purpose": [
            "Daily oil movement",
            "Seasonality effects",
            "Currency reaction",
            "Risk measurement",
            "Historical memory",
            "News impact analysis"
        ]
    })

    st.dataframe(features, use_container_width=True)

# ============================================================
# FORECAST PAGE
# ============================================================

elif page == "📉 Forecasting":

    st.header("📉 Oil Price Forecasting")

    st.markdown("""
    ARIMA Time-Series Forecasting was used to predict future oil prices.
    """)

    show_image(forecast_img, "plot_arima_forecast.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "ARIMA(2,1,2)")

    with col2:
        st.metric("Forecast Window", "30 Days")

    with col3:
        st.metric("MAE", "$0.25")

    st.markdown("""
    <div class="insight-box">

    <span class="big-font">Forecast Interpretation:</span>

    - The model successfully tracked oil trends
    - Short-term forecasts were relatively accurate
    - Oil prices remained sensitive to geopolitical events
    - Forecasting becomes harder during extreme crises

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CORRELATION PAGE
# ============================================================

elif page == "📊 Correlation Analysis":

    st.header("📊 Market Correlation Analysis")

    st.markdown("""
    This heatmap shows how strongly markets move together.
    """)

    show_image(corr_img, "plot_correlation.png")

    st.markdown("""
    <div class="insight-box">

    <span class="big-font">Main Observations:</span>

    ✅ Oil and INR showed moderate relationship<br>
    ✅ NIFTY had weaker direct oil correlation<br>
    ✅ Currency reacts faster than stock markets<br>
    ✅ Economic shocks spread across markets differently

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FIX 2: SIMULATOR IS NOW ITS OWN PAGE
# Previously this block ran on every page because it had
# no if/elif wrapping it. Now it only runs when selected.
# ============================================================

elif page == "🌍 Economic Impact Simulator":

    st.header("🌍 Economic Impact Simulator")

    st.markdown("""
    Adjust global conditions to see how they may impact India's economy.
    """)

    oil_price = st.slider("🛢 Brent Oil Price ($/barrel)", 40, 150, 85)
    inr_value = st.slider("💱 INR per USD", 65, 95, 83)
    conflict_level = st.selectbox(
        "⚠ Geopolitical Conflict Level",
        ["Low", "Medium", "High", "Extreme"]
    )

    st.markdown("---")
    st.subheader("📊 Economic Impact Analysis")

    # OIL ANALYSIS
    if oil_price < 70:
        st.success("✅ Oil prices are relatively stable.")
        st.write("- Lower fuel inflation")
        st.write("- Better for Indian economy")
        st.write("- Positive for businesses")
    elif oil_price < 100:
        st.warning("⚠ Oil prices are rising.")
        st.write("- Fuel prices may increase")
        st.write("- Transportation costs rise")
        st.write("- Inflation pressure increases")
    else:
        st.error("🚨 High Oil Risk Detected!")
        st.write("- Severe inflation risk")
        st.write("- INR may weaken")
        st.write("- Government import burden increases")
        st.write("- Stock market volatility may rise")

    st.markdown("---")

    # INR ANALYSIS
    if inr_value < 78:
        st.success("✅ INR is relatively strong.")
    elif inr_value < 85:
        st.warning("⚠ INR is weakening.")
        st.write("- Imports become expensive")
        st.write("- Oil import costs rise")
    else:
        st.error("🚨 Currency Stress Detected!")
        st.write("- High import pressure")
        st.write("- Inflation risk increases")
        st.write("- Foreign investor confidence may weaken")

    st.markdown("---")

    # CONFLICT ANALYSIS
    if conflict_level == "Low":
        st.success("✅ Global geopolitical risk is low.")
    elif conflict_level == "Medium":
        st.warning("⚠ Moderate geopolitical uncertainty detected.")
    elif conflict_level == "High":
        st.error("🚨 High geopolitical tension!")
        st.write("- Oil supply disruption risk")
        st.write("- Commodity volatility increases")
        st.write("- Financial markets become unstable")
    else:
        st.error("🔥 EXTREME GLOBAL RISK!")
        st.write("- Possible oil shock")
        st.write("- Major market volatility")
        st.write("- High economic uncertainty")
        st.write("- Risk of global inflation surge")

    st.markdown("---")
    st.subheader("📈 Overall Economic Risk Meter")

    # FIX 3: Risk score used elif so Extreme does not double-count.
    # Also added Medium (was 0 before which made no sense).
    # Old code: two separate `if` blocks meant High AND Extreme both fired.
    risk_score = 0

    if oil_price > 100:
        risk_score += 40

    if inr_value > 85:
        risk_score += 30

    if conflict_level == "Medium":
        risk_score += 10
    elif conflict_level == "High":
        risk_score += 20
    elif conflict_level == "Extreme":
        risk_score += 40   # only 40, not 20+40=60 like before

    # Cap at 100
    risk_score = min(risk_score, 100)

    if risk_score < 30:
        st.success(f"🟢 LOW RISK — Score: {risk_score}/100")
    elif risk_score < 60:
        st.warning(f"🟠 MODERATE RISK — Score: {risk_score}/100")
    else:
        st.error(f"🔴 HIGH ECONOMIC RISK — Score: {risk_score}/100")

# ============================================================
# FIX 4: FINAL INSIGHTS — changed `if` to `elif`
# Old code used `if` here which made this section render
# on top of the simulator output instead of replacing it.
# ============================================================

elif page == "💡 Final Insights":

    st.header("💡 Final Business Insights")

    st.markdown("### Key Conclusions From The Project")

    insights = [
        "Geopolitical conflicts significantly impact oil markets",
        "India is vulnerable to global energy shocks",
        "Oil volatility influences INR stability",
        "Stock markets recover faster than commodity markets",
        "Machine Learning can help identify early warning signals",
        "Extreme market movements occur more frequently during crises"
    ]

    for insight in insights:
        st.success(insight)

    st.markdown("---")

    st.subheader("🚀 Future Improvements")

    future = [
        "Live oil price integration",
        "Real-time news sentiment analysis",
        "Interactive forecasting",
        "Advanced ML models (XGBoost/LSTM)",
        "Risk prediction dashboard"
    ]

    for item in future:
        st.info(item)

    st.markdown("---")

    st.subheader("👨‍💻 Technologies Used")

    tech = pd.DataFrame({
        "Category": [
            "Programming",
            "Visualization",
            "Machine Learning",
            "Forecasting",
            "Dashboard"
        ],
        "Tools": [
            "Python",
            "Matplotlib, Seaborn",
            "Scikit-learn",
            "ARIMA",
            "Streamlit"
        ]
    })

    st.table(tech)

# ============================================================
# FOOTER — runs on every page (correct, intentional)
# ============================================================

st.markdown("---")
st.markdown(
    """
    <center>
    Built with ❤️ using Data Science & Machine Learning<br>
    Geopolitical Oil Impact Analysis Dashboard
    </center>
    """,
    unsafe_allow_html=True
)
