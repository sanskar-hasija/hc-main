import streamlit as st

# Set page configuration to center content
st.set_page_config(layout="centered")

# Custom CSS to center the text and style the links
st.markdown("""
    <style>
    .centered-text {
        text-align: center;
        padding: 10px 0;
    }
    .centered-text a {
        color: #4A90E2;
        text-decoration: none;
        font-weight: bold;
    }
    .centered-text a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Create centered hyperlinks
st.markdown('<div class="centered-text">'
            '<a href="https://www.google.com" target="_blank">Occupany Dashboard</a>'
            '</div>', unsafe_allow_html=True)

st.markdown('<div class="centered-text">'
            '<a href="https://hc-vis.streamlit.app/" target="_blank">Daily Pickup Dashboard</a>'
            '</div>', unsafe_allow_html=True)

st.markdown('<div class="centered-text">'
            '<a href="https://www.google.com" target="_blank">Reservation Spike Analysis Dashboard</a>'
            '</div>', unsafe_allow_html=True)