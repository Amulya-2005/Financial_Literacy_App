import streamlit as st
import pandas as pd

# Hide Sidebar
st.set_page_config(page_title="Financial Literacy App", page_icon="💰", layout="wide")

st.markdown("""
    <style>
        section[data-testid="stSidebar"] { display: none !important; }
        body {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stSuccess {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
        }
        .title-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .button-container {
            text-align: left;
            margin-left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for feature selection
if "selected_feature" not in st.session_state:
    st.session_state.selected_feature = "Home"

# Function to update selected feature
def set_feature(feature):
    st.session_state.selected_feature = feature

# Home Page with Feature Selection
if st.session_state.selected_feature == "Home":
    st.markdown("""
        <div class='title-container'>
            <h1>Financial Literacy App💸</h1>
        </div>
    """, unsafe_allow_html=True)
    st.write("Empowering Women through Financial Education and Tools!")
    
    # Navigation Buttons with callbacks
    with st.container():
        st.markdown("<div class='button-container'>", unsafe_allow_html=True)
        st.button("📊 Budgeting", on_click=set_feature, args=("Budgeting",))
        st.button("📈 Financial Planning", on_click=set_feature, args=("Financial Planning",))
        st.button("📊 SIP Calculator", on_click=set_feature, args=("SIP Calculator",))
        st.button("🏠 EMI Calculator", on_click=set_feature, args=("EMI Calculator",))
        st.button("📈 Investment Portfolio", on_click=set_feature, args=("Investment Portfolio",))
        st.markdown("</div>", unsafe_allow_html=True)

# Feature Pages
else:
    st.title(f"{st.session_state.selected_feature} 🚀")

    if st.session_state.selected_feature == "Budgeting":
        income = st.number_input("Enter your Monthly Income (₹):", min_value=0)
        expenses = st.number_input("Enter your Monthly Expenses (₹):", min_value=0)
        if st.button("Calculate Savings"):
            savings = income - expenses
            if savings > 0:
                st.markdown(f"<div class='stSuccess'>Great! You are saving ₹{savings} per month. 🎉</div>", unsafe_allow_html=True)
            else:
                st.warning("Your expenses are exceeding your income. Consider reducing spending!")

    elif st.session_state.selected_feature == "Financial Planning":
        goal = st.text_input("Enter your Financial Goal:")
        goal_amount = st.number_input("Target Amount (₹):", min_value=0)
        years = st.slider("Timeframe (years):", 1, 30, 5)
        if st.button("Calculate Monthly Saving Needed"):
            monthly_saving = goal_amount / (years * 12)
            st.markdown(f"<div class='stSuccess'>To achieve '{goal}', you need to save ₹{monthly_saving:.2f} per month.</div>", unsafe_allow_html=True)

    elif st.session_state.selected_feature == "SIP Calculator":
        sip_amount = st.number_input("Monthly SIP Amount (₹):", min_value=0)
        years = st.slider("Investment Duration (years):", 1, 30, 5)
        rate = st.slider("Expected Annual Return (%):", 5, 20, 12)
        if st.button("Calculate SIP Future Value"):
            months = years * 12
            r = rate / 100 / 12
            future_value = sip_amount * (((1 + r) ** months - 1) / r) * (1 + r)
            st.markdown(f"<div class='stSuccess'>Estimated Future Value: ₹{future_value:.2f}</div>", unsafe_allow_html=True)

    elif st.session_state.selected_feature == "EMI Calculator":
        loan_amount = st.number_input("Loan Amount (₹):", min_value=0)
        interest_rate = st.slider("Annual Interest Rate (%):", 1.0, 20.0, 10.0)
        tenure = st.sl