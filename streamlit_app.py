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
                    .sub-header {font-size: 24px; text-align:center; color: #8A17BF;}
                  </style>
                  ''', unsafe_allow_html = True)
# Sidebar
st.sidebar.title('🌌 Navigation')
page = st.sidebar.radio('Go To:',
                        ['🏠 Home', '🌟 About', '💼 Projects', '🔨 Skills', '📄 Resume', '📩 Contract' ])

# Home Page 
if page == '🏠 Home':
  st.markdown('<p class="main-header">Tahara Gibbs</p>', unsafe_allow_html=True)  
  st.markdown('<p class="sub-header">Aspiring Astronaut | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Colums for stats
  col1, col2, col3 = st.columns(3)
  
  with col1:
    st.metric('GPA', '2.1', '📚')
  with col2:
    st.metric('Projects', '6', '💼')
  with col3:
    st.metric('Skills', '10+', '🚀')
    
  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a Business Administration student who is passionate about Entrepreneurship and Business Development. I am currnetly 
                learning HTML, CSS, JavaScript, and Python to build innovative solutions.

                🎯 **Current Focus:** Building interactive web applications with Streamlit

                📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)

                🚀 **Fun Fact:** I can make complex edits on Adobe After Effects!
            ''')
  with col2:
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/TaharaGibbs/CIS211_PROJECT_1/refs/heads/main/pngtree-astronaut-waving-in-space-suit-illustration-png-image_15736057.avif', use_column_width=True)

# About Page
elif page == '🌟 About':
  st.title('About Me')

  # Timeline of my Professional Journey 
  st.subheader('My Journey 📍')

  with st.expander('2024 - Present: Medgar Evers Colle'):
    st.write('''
              - Major: Business Administration
              - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, A.I
              - Activities: Baseball, Volleyball, and Art Club participant
            ''')

  with st.expander('2024 - 2025: NYC Art School'):
    st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
              ''')

  st.subheader('Interests & Hobbies 🏓')
  Interests = ['Web Development', 'A.I/Machine Learning', 'Art', 'Baseball', 'Volleyball', 'Japanese Animations']
