import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }

        [data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
            border-right: 1px solid #333;
        }
        
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span {
            color: #ffffff !important;
        }

        [data-testid="stFileUploadDropzone"] {
            background-color: #ffffff !important;
            border: 2px dashed #00ffcc !important;
            border-radius: 15px !important;
            padding: 15px !important;
        }
        
        [data-testid="stFileUploadDropzone"] div,
        [data-testid="stFileUploadDropzone"] span,
        [data-testid="stFileUploadDropzone"] small {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            font-weight: bold !important;
        }
        
        [data-testid="stFileUploadDropzone"] svg {
            fill: #000000 !important;
        }

        .stChatInputContainer {
            background-color: white !important;
            border-radius: 20px !important;
            padding-bottom: 5px !important;
        }
        .stChatInput textarea {
            color: black !important;
        }

        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.8) !important;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        [data-testid="stChatMessage"] p {
            color: white !important;
        }

        header { background: transparent !important; }
        footer { visibility: hidden; }
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; }
        </style>
        """, unsafe_allow_html=True)

    def render_header(self, version):
        st.markdown(f'''
        <div style="text-align: center; padding: 30px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({version})</div>
            <div style="color: white; font-size: 45px; font-weight: 900;">AKYLMAN</div>
        </div>
        ''', unsafe_allow_html=True)
