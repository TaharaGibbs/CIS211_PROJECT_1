import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title = "Tahara | Portfolio",
  page_icon= "🚀",
  layout = 'wide'
)


# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header{font-size: 42px; font-weight: bold; text-align:center;}
                    .subheader {font_size: 24px; text-align:center; color: #9F2B68;}
                  </style>
                  ''', unsafe_allow_html = True)
# sidebar
st.sidebar.title('🌌Navigation')
page = st.sidebar.radio('Go To:',
                        ['🏠Home', '🌟About', '💼Projects', '🔨Skills', '📄Resume', '📩Contract' ])

# Home Page 
if page == '🏠Home':
  st.markdown('<p class="main-header">Tahara Gibbs</p>', unsafe_allow_html=True)  
  st.markdown('<p class="sub-header">Aspiring Astronaut | Medgar Evers College</p', unsafe_allow_html=True)
