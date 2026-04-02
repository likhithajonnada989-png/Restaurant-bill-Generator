import streamlit as st
from menu import menu
from model import predict_order

# Page config
st.set_page_config(page_title="Smart Restaurant", layout="wide")
st.markdown("""
<style>

/* Background image (Food theme) */
.stApp {
    background: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836") no-repeat center center fixed;
    background-size: cover;
}

/* Blur + dark overlay */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(6px);
    background-color: rgba(0,0,0,0.5);
    z-index: -1;
}

/* Main content box */
.block-container {
    background-color: rgba(0, 0, 0, 0.7);
    padding: 25px;
    border-radius: 12px;
}

/* Text color */
h1, h2, h3, h4, p, label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# Custom CSS (MAIN MAGIC)
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        color: #ff9933;
        font-size: 40px;
        font-weight: bold;
    }
    .card {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .total {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🍽 Smart Restaurant System</div>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

selected_items = []

# LEFT SIDE MENU
with col1:
    st.subheader("📋 Menu")

    for item, price in menu.items():
        if st.checkbox(f"{item} - ₹{price}"):
            selected_items.append(item)

# RIGHT SIDE BILL
with col2:
    st.subheader("🧾 Your Bill")

    total = 0

    if selected_items:
        for item in selected_items:
            st.markdown(f"<div class='card'>{item} - ₹{menu[item]}</div>", unsafe_allow_html=True)
            total += menu[item]

        st.markdown(f"<div class='total'>Total Bill: ₹{total}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please select items")

# RECOMMENDATION SECTION
if selected_items:
    st.markdown("---")
    st.subheader("🤖 Recommended Items")

    recs = predict_order(selected_items)

    if recs:
        for item in recs:
            st.success(f"👉 {item}")
    else:
        st.info("No recommendations available")