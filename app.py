import streamlit as st
import requests
from streamlit_lottie import st_lottie
import urllib.parse

# Set up page configuration with theme
st.set_page_config(
    page_title="Demo Sales Agent Call App",
    page_icon="🚀",
    layout="wide",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: white;
        color: black;
        border: 2px solid #00bfff;
        padding: 12px;
        border-radius: 15px;
        font-size: 16px;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        box-shadow: 0 0 10px #00bfff;
    }
    h1 {
        color: #00bfff;
        text-align: center;
        font-size: 48px;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    label {
        color: silver !important;
    }
    .email-link {
        color: #00bfff;
        text-decoration: none;
        font-weight: bold;
    }
    .email-link:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Function to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to make the API call
def make_call(call_number, first_message):
    url = "https://api.vapi.ai/call"
    payload = {
        "name": "SalesDemo",
        "assistantId": "d92a058d-19f0-41bf-8cda-6178a42ed773",
        "phoneNumberId": "ff514eca-1666-49bf-9359-defc2df305e3",
        "customer": {
            "numberE164CheckEnabled": True,
            "number": call_number,
            "name": "Andre"
        },
        "assistantOverrides": {
            "transcriber": {"provider": "deepgram"},
            "model": {
                "provider": "openai",
                "model": "gpt-4o-mini-2024-07-18"
            },
            "voice": {
                "provider": "openai",
                "voiceId": "alloy",
                "speed": None
            },
            "firstMessageMode": "assistant-speaks-first",
            "backgroundSound": "office",
            "name": "Sarah",
            "firstMessage": first_message,
        }
    }
    headers = {
        "Authorization": "Bearer c031c0fd-76b4-440b-96a1-42ec699789fe",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text

# Function to create a mailto link
def create_mailto_link(message):
    email = "bryan.stewart@druidpro.com"
    subject = urllib.parse.quote("Developer Notes")
    body = urllib.parse.quote(message)
    return f"mailto:{email}?subject={subject}&body={body}"

# Load Lottie animation
lottie_phone = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_5tl1xxnz.json")

# Streamlit UI
st.title("🚀 Demo Sales Agent Call App")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Send A Sales Call")
    call_number = st.text_input("📞 Enter Call Number", "enter number here")
    first_message = st.text_input("💬 Enter First Message", "Hello, is this Mr. Castro?")

    if st.button("🌟 Initiate Sales Call"):
        with st.spinner("Connecting to the future..."):
            response = make_call(call_number, first_message)
        st.success("Call initiated successfully!")
        st.json(response)

    st.markdown("### Developer Notes")
    dev_notes = st.text_area("✍️ Write your notes for the developer", height=150)
    if dev_notes:
        mailto_link = create_mailto_link(dev_notes)
        st.markdown(f'<a href="{mailto_link}" class="email-link">📧 Click here to send notes to the developer</a>', unsafe_allow_html=True)

with col2:
    st_lottie(lottie_phone, key="phone_animation", height=300)

# Footer
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px; color: #00bfff;'>
        Made  by Bryan
    </div>
    """,
    unsafe_allow_html=True
)
