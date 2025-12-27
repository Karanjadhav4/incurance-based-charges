import streamlit as st
import numpy as np
import joblib

# =============================
# Load ML Model
# =============================
model = joblib.load("model.pkl")

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="💰",
    layout="centered"
)

# =============================
# CSS STYLING
# =============================
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #ffecd2, #fcb69f);
}

/* Remove default Streamlit header gap a bit */
[data-testid="stMainBlockContainer"] {
    padding-top: 1.5rem;
}

/* Top nav-style bar */
.top-bar {
    width: 100%;
    padding: 10px 18px;
    border-radius: 0 0 18px 18px;
    background: rgba(0,0,0,0.15);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 12px;
}
.top-bar-left {
    font-weight: 700;
    font-size: 20px;
}
.top-bar-right {
    font-size: 12px;
    opacity: 0.9;
}

/* Header */
.header {
    font-size: 40px;
    font-weight: 700;
    color: #ffffff;
    padding: 18px 10px;
    text-align: center;
    border-radius: 18px;
    background: linear-gradient(135deg, #6b0489, #b517d1);
    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
    margin-bottom: 10px;
}

/* Card wrapper for form */
.card {
    background:#ffffff;
    padding:25px 30px;
    border-radius:20px;
    box-shadow:0 6px 16px rgba(0,0,0,0.18);
    margin-top:20px;
}

/* Result box */
.result-box {
    margin-top:30px;
    padding:30px;
    border-radius:20px;
    color:white;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    box-shadow:0 4px 14px rgba(0,0,0,0.25);
}

/* Make labels slightly bolder */
.stSlider label, .stSelectbox label, .stNumberInput label {
    font-weight: 600;
}

/* Center the predict button and style it */
.stButton > button {
    width: 100%;
    border-radius: 999px;
    background: linear-gradient(135deg, #6b0489, #b517d1);
    color: #ffffff;
    border: none;
    font-weight: 700;
    font-size: 18px;
    padding: 0.6rem 0;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #b517d1, #6b0489);
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

/* Custom footer */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background: rgba(0,0,0,0.12);
    backdrop-filter: blur(8px);
    color: #222;
    text-align: center;
    padding: 6px 4px;
    font-size: 12px;
}
.footer a {
    color: #6b0489;
    text-decoration: none;
    font-weight: 600;
}
.footer a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# =============================
# TOP NAV-STYLE BAR
# =============================
st.markdown(
    """
    <div class="top-bar">
        <div class="top-bar-left">🏥 InsureSmart</div>
        <div class="top-bar-right">Medical Cost Estimator • v1.0</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =============================
# HEADER
# =============================
st.markdown('<div class="header">💰 Insurance Charges Prediction 💸</div>', unsafe_allow_html=True)
st.write("##### 🧠 Predict estimated medical insurance cost based on your details")

# =============================
# SIDEBAR
# =============================
st.sidebar.title("⚙️ Controls")
st.sidebar.info("Fill details and click Predict")
st.sidebar.markdown("---")
st.sidebar.write("👑 Developed by **Karan Jadhav**")

# =============================
# INPUT FORM (inside card)
# =============================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("👶 Age", 0, 120, 25)
        bmi = st.slider("⚖️ BMI (Body Mass Index)", 10.0, 60.0, 22.5)
        children = st.number_input("👨‍👦‍👦 Children", 0, 10, 0)

    with col2:
        sex = st.selectbox("🧑 Sex", ("Male", "Female"))
        smoker = st.selectbox("🚬 Do You Smoke?", ("Yes", "No"))
        region = st.selectbox("📍 Region", ("Southeast", "Other"))

    # Convert to numeric
    sex = 1 if sex == "Male" else 0
    smoker = 1 if smoker == "Yes" else 0
    region = 1 if region == "Southeast" else 0

    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# PREDICT BUTTON
# =============================
if st.button("🔮 Predict Insurance Charges"):
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)[0]

    if prediction < 15000:
        msg = "🎉 Amazing! Your insurance cost is **very LOW**. Keep rocking with a healthy lifestyle!"
        bg = "linear-gradient(135deg, #4CAF50, #81C784)"
    elif prediction < 30000:
        msg = "🙂 Your expected insurance charge is **average**. Keep maintaining good habits!"
        bg = "linear-gradient(135deg, #FFC107, #FFD54F)"
    else:
        msg = "⚠️ The cost seems **high!** Try maintaining diet, exercise & avoid smoking 🚑"
        bg = "linear-gradient(135deg, #E53935, #EF5350)"

    st.markdown(f"""
    <div class="result-box" style="background:{bg};">
        💰 Estimated Charges:<br>
        <span style="font-size:45px;">${prediction:,.2f}</span><br><br>
        {msg}
    </div>
    """, unsafe_allow_html=True)

    st.toast("Prediction generated successfully 🎯")

# =============================
# FOOTER
# =============================
