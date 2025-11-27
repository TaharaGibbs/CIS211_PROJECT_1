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

                🚀 **Fun Fact:** I can make complex edited videos on Adobe After Effects!
            ''')
  with col2:
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/TaharaGibbs/CIS211_PROJECT_1/refs/heads/main/pngtree-astronaut-waving-in-space-suit-illustration-png-image_15736057.avif', use_column_width=True)

# About Page
elif page == '🌟 About':
  st.title('About Me')

  # Timeline of my Professional Journey 
  st.subheader('My Journey 📍')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
              - Major: Business Administration
              - Relevant Coursework: Introduction to Business, Management, Internet & Emerging Technologies, Programming, Database Systems, A.I
              - Activities: Baseball, Volleyball, and Art Club participant
            ''')

  with st.expander('2023 - 2025: NYC School of Business'):
    st.write('''
                - Graduated with honors
                - AP Management A (Score: 5)
                - Founded the Art Club
              ''')

  st.subheader('Interests & Hobbies 🏓')
  interests = ['Web Development', 'A.I/Machine Learning', 'Art', 'Baseball', 'Volleyball', 'Japanese Animations']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🧩{interest}')

elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:!')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('https://th.bing.com/th/id/R.f1b7e8eab63689611376b0b7f23d4fea?rik=cuYCuq2bGsAPBQ&riu=http%3a%2f%2fwww.pngall.com%2fwp-content%2fuploads%2f5%2fDigital-Marketing-PNG.png&ehk=1zUcafp%2fggRj2H8Rw%2fXijbJLed2QWcKIpX31ZlhXbKo%3d&risl=&pid=ImgRaw&r=0')
    
