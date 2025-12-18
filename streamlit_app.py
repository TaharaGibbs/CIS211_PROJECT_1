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
                    .sub-header {font-size: 24px; text-align:center; color: #3AA9AE;}
                  </style>
                  ''', unsafe_allow_html = True)
# Sidebar
st.sidebar.title('🌌 Navigation')
page = st.sidebar.radio('Go To:',
                        ['🏠 Home', '🌟 About', '💼 Projects', '🔨 Skills', '📄 Resume', '📩 Contract' ])

# Home Page 
if page == '🏠 Home':
  st.markdown('<p class="main-header">Tahara Gibbs</p>', unsafe_allow_html=True)  
  st.markdown('<p class="sub-header">Aspiring Corporate Attorney | Medgar Evers College</p>', unsafe_allow_html=True)

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
    st.image('https://raw.githubusercontent.com/TaharaGibbs/CIS211_PROJECT_1/refs/heads/main/somos.jfif', use_column_width=True)

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
                - AP Management (Score: 5)
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
  st.write('Here are some projects I have worked on!')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('https://th.bing.com/th/id/R.f1b7e8eab63689611376b0b7f23d4fea?rik=cuYCuq2bGsAPBQ&riu=http%3a%2f%2fwww.pngall.com%2fwp-content%2fuploads%2f5%2fDigital-Marketing-PNG.png&ehk=1zUcafp%2fggRj2H8Rw%2fXijbJLed2QWcKIpX31ZlhXbKo%3d&risl=&pid=ImgRaw&r=0')
    
    with col2:
      st.subheader('🧮 Marketing Plan')
      st.write("A comprehensive document that was created as a means of outlining and tracking a companies' goals, desired achievements, strategies, and projections for their marketing department")
      st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  # Project 2
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://raw.githubusercontent.com/TaharaGibbs/CIS211_PROJECT_1/refs/heads/main/Complaint-Box.bak.avif')
    with col2:
      st.subheader('Employee Complaint Box')
      st.write('📥 Interactive Web App for staff, faculty, managers and supervisors to document any grievances they wish for the company to address')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🔨 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
      'Python' : 85,
      'HTML/CSS' : 70,
      'JavaScript' : 60,
      'SQL' : 50,
      'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('Powerpoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')

  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')

elif page == '📄 Resume':
  st.title('Resume')

  # Read PDF from Github repositiory
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

  st.download_button(
    label ='🔽 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contract':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** tahara.gibbs@student.mec.cuny.edu
        
        🔗 **LinkedIn:** [linkedin.com/in/taharagibbs](https://linkedin.com)

        👩🏾‍💻 **Github:** [https://github.com/TaharaGibbs](https://github.com)

        📸 **Instagram:** [@t._.thespacecadet](https://instagram.com)
    ''')

    
    # Fun interactive element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '⌨️ Coding',
            '📚 Studing',
            '☕ On a coffee break',
            '🎮 Gaming',
            '💤 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer 
    st.write('---')
    st.markdown(
      f'<center>Made with 💝 using Streamlit | @ {datetime.now().year} Tahara Gibbs </center>',
      unsafe_allow_html = Ture
    )
    
