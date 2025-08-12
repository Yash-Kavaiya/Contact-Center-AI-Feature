import streamlit as st

def show_header():
    """Display the common header with three hyperlinks"""
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #e0e0e0; margin-bottom: 20px;">
        <div style="flex: 1; text-align: left;">
            <a href="https://easy-ai-labs.lovable.app/" target="_blank" style="text-decoration: none; color: #667eea; font-weight: bold;">
                Easy AI Labs
            </a>
        </div>
        <div style="flex: 1; text-align: center;">
            <a href="https://www.linkedin.com/in/yashkavaiya" target="_blank" style="text-decoration: none; color: #667eea; font-weight: bold;">
                Yash Kavaiya
            </a>
        </div>
        <div style="flex: 1; text-align: right;">
            <a href="https://www.linkedin.com/company/genai-guru" target="_blank" style="text-decoration: none; color: #667eea; font-weight: bold;">
                Gen AI Guru
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)