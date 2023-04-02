import streamlit as st
import requests
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define the form
st.set_page_config(
    page_title="Contact Us Form",
    page_icon="notes.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.sidebar.title('Contact Information')
st.sidebar.text('Developed by Farneet Singh')
st.sidebar.text('\n')
st.sidebar.text('\n')


with st.sidebar:

    html = """
        <img src="https://www.transparentpng.com/thumb/instagram-logo-icon/16WUcW-instagram-logo-icon-png.png" alt="Instagram Icon" height = "30px" style="margin-right: 10px;">    <a href="https://www.instagram.com/farneet.singh/" style="color: grey;  text-decoration: none;">Farneet Singh</a>
        <br>
        <br>
        <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-512x512-vkm0drb1.png" alt="LinkedIn Icon" height = "30px" style="margin-right: 10px;">    <a style="color: grey;  text-decoration: none;" href="https://www.linkedin.com/in/farneet-singh-6b155b208/">Farneet Singh</a>
        <br>
        <br>
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Icon" height = "30px" style="margin-right: 10px;">    <a href="https://github.com/farneet24" style="color: grey;  text-decoration: none;">farneet24</a>

       
        """
    
    st.markdown(html, unsafe_allow_html=True)
        


st.success("Got a question? We'd love to hear from you. Send us a message and we'll respond as soon as possible.")

st.markdown("<h1 style='text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)

with st.form(key='my_form'):

    occupation = st.selectbox(label='What can we help you with?', options=['Select', 'I want to report a bug', 'I have a suggestion', 'Other'])

    name = st.text_input(label='Name')
    email = st.text_input(label='Email')
    text = st.text_area("Message")
    submit_button = st.form_submit_button(label='Submit')

# Process the form data
if submit_button:

    if occupation == 'Select':
            st.error("Please select the reason")
    if not name:
            st.error('Please enter your name')
    if not email:
            st.error('Please enter your email')
    if not text:
            st.error('Please enter a message')

    if name and email and text and occupation != 'Select':
    # Send the form data to FormsPree
        data = {'Name': name, 'Email': email, 'Purpose': occupation, 'Message' : text}
        response = requests.post('https://formspree.io/f/xdovznoy', data=data)

        if email and not re.match(email_regex, email):
            st.error('Please enter a valid email address')
        # Display a success message
        if response.status_code == 200:
            st.success('Form submitted successfully.')
        else:
            st.error('Error submitting form.')

