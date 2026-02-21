from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    """Generate response from Gemini Pro Vision model"""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    """Prepare image data for Gemini Pro model input"""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Civil Engineering Insight Studio", page_icon="🏗️", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        padding: 20px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 15px 40px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .stTextInput>div>div>input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
    }
    .uploadedFile {
        border-radius: 15px;
        border: 2px dashed #667eea;
        padding: 20px;
    }
    div[data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .stImage {
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    div[data-testid="stMarkdownContainer"] > p {
        font-size: 16px;
        line-height: 1.6;
    }
    .stAlert {
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏗️ Civil Engineering Insight Studio</h1>", unsafe_allow_html=True)

# Project Overview Section
st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 15px; 
    box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 30px;'>
        <h3 style='color: #667eea; margin-top: 0;'>📋 About This Project</h3>
        <p style='font-size: 16px; line-height: 1.8; color: #2c3e50;'>
            Welcome to the <strong>Civil Engineering Insight Studio</strong> - an AI-powered tool designed to analyze 
            civil engineering structures from images. Using Google's advanced Gemini AI model, this application provides 
            detailed insights into construction materials, structural components, and engineering features.
        </p>
        <p style='font-size: 16px; line-height: 1.8; color: #2c3e50;'>
            <strong>Key Features:</strong><br>
            🔹 Automatic structure type identification<br>
            🔹 Material composition analysis<br>
            🔹 Structural component detection<br>
            🔹 Construction progress assessment<br>
            🔹 Engineering insights and recommendations
        </p>
    </div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Input Section")
    # Text input field
    input_text = st.text_input("Additional Prompt (Optional):", key="input", placeholder="Enter any specific questions...")
    
    # File uploader
    uploaded_file = st.file_uploader("📤 Upload Structure Image", type=["jpg", "jpeg", "png"])
    
    # Submit button
    submit = st.button("🔍 Analyze Structure")

with col2:
    st.markdown("### 🖼️ Image Preview")
    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
    else:
        st.info("👆 Upload an image to see preview")

# Input prompt for the model
input_prompt = """
You are an expert civil engineer. Analyze this structure and provide a balanced overview:

1. Type of Structure: Identify what type it is
2. Materials Used: Main construction materials visible
3. Structural Components: Key structural elements
4. Construction Stage: Current progress or completion status
5. Notable Features: Any significant engineering aspects

Provide a clear, medium-length analysis with relevant details.
"""

# Process user input and generate description
if submit:
    try:
        if uploaded_file is not None:
            with st.spinner("🔄 Analyzing structure..."):
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(input_text, image_data, input_prompt)
            
            st.markdown("---")
            st.markdown("### 📊 Structure Analysis Report")
            st.markdown(f"""
                <div style='background-color: white; padding: 25px; border-radius: 15px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px;'>
                    {response}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please upload an image to analyze.")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
