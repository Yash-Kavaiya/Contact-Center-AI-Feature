import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time

# Import page modules
from pages.speaker_diarization import show_speaker_diarization
from pages.call_summarization import show_call_summarization
from pages.pii_detection import show_pii_detection
from pages.sentiment_analysis import show_sentiment_analysis
from pages.responsible_ai import show_responsible_ai

# Page configuration
st.set_page_config(
    page_title="Contact Center AI Solutions",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .success-text {
        color: #28a745;
        font-weight: bold;
    }
    .warning-text {
        color: #ffc107;
        font-weight: bold;
    }
    .danger-text {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Future of Contact Center AI Powered Solutions</h1>
    <p>Advanced AI capabilities transforming customer service operations</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
feature_selection = st.sidebar.selectbox(
    "Choose a Feature",
    ["Overview", "Speaker Diarization", "Call Summarization", "PII Detection", "Sentiment Analysis", "Responsible AI"]
)

# Generate sample data
@st.cache_data
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'date': dates,
        'calls_processed': np.random.randint(100, 500, len(dates)),
        'speaker_accuracy': np.random.uniform(0.85, 0.98, len(dates)),
        'sentiment_positive': np.random.uniform(0.6, 0.8, len(dates)),
        'sentiment_negative': np.random.uniform(0.1, 0.3, len(dates)),
        'pii_detected': np.random.randint(5, 50, len(dates)),
        'summary_quality': np.random.uniform(0.8, 0.95, len(dates))
    }
    return pd.DataFrame(data)

def generate_call_transcript():
    return """
Agent: Thank you for calling TechSupport Plus, this is Sarah. How can I help you today?

Customer: Hi Sarah, I'm having trouble with my account. My name is John Smith, and my account number is AC-12345-6789. I can't access my dashboard.

Agent: I'm sorry to hear you're having trouble accessing your dashboard, Mr. Smith. Let me help you with that. I can see your account here. Can you tell me what specific error message you're seeing when you try to log in?

Customer: It says "Invalid credentials" but I'm sure I'm using the right password. I've been using the same one for months.

Agent: I understand your frustration. Let me check your account status. It looks like there might have been a security update that requires a password reset. For your security, I'll send a password reset link to your registered email address ending in ...@gmail.com. Is that still the correct email?

Customer: Yes, that's correct. How long will it take?

Agent: You should receive the email within the next 2-3 minutes. Once you reset your password, you'll be able to access your dashboard normally. Is there anything else I can help you with today?

Customer: No, that should do it. Thank you for your help, Sarah.

Agent: You're very welcome, Mr. Smith. Thank you for calling TechSupport Plus, and have a great day!
"""

# Main content based on selection
if feature_selection == "Overview":
    # Overview page with metrics and charts
    st.markdown("## 📊 AI Solutions Overview")
    
    # Sample data
    df = generate_sample_data()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📞 Total Calls Processed",
            value="1.2M+",
            delta="15.3% vs last month"
        )
    
    with col2:
        st.metric(
            label="🎯 Speaker Accuracy",
            value="94.7%",
            delta="2.1% improvement"
        )
    
    with col3:
        st.metric(
            label="😊 Positive Sentiment",
            value="72.3%",
            delta="5.8% increase"
        )
    
    with col4:
        st.metric(
            label="🔒 PII Protected",
            value="99.8%",
            delta="0.2% improvement"
        )
    
    # Charts
    st.markdown("### 📈 Performance Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Calls processed over time
        fig_calls = px.line(df.tail(30), x='date', y='calls_processed',
                           title='Daily Calls Processed (Last 30 Days)',
                           labels={'calls_processed': 'Number of Calls', 'date': 'Date'})
        fig_calls.update_layout(showlegend=False)
        st.plotly_chart(fig_calls, use_container_width=True)
    
    with col2:
        # Speaker accuracy
        fig_accuracy = px.line(df.tail(30), x='date', y='speaker_accuracy',
                              title='Speaker Diarization Accuracy (Last 30 Days)',
                              labels={'speaker_accuracy': 'Accuracy (%)', 'date': 'Date'})
        fig_accuracy.update_layout(showlegend=False)
        st.plotly_chart(fig_accuracy, use_container_width=True)
    
    # Feature highlights
    st.markdown("### 🌟 AI Features")
    
    features = [
        {
            "title": "🎤 Speaker Diarization",
            "description": "Advanced AI that identifies and separates different speakers in audio conversations with 95%+ accuracy.",
            "benefits": ["Real-time speaker identification", "Multi-language support", "Noise reduction", "Quality assurance"]
        },
        {
            "title": "📝 Call Summarization",
            "description": "Intelligent summarization of customer conversations using state-of-the-art NLP models.",
            "benefits": ["Automatic key point extraction", "Customizable summary formats", "Action item identification", "Performance analytics"]
        },
        {
            "title": "🔒 PII Detection",
            "description": "Comprehensive protection of personally identifiable information with real-time detection and masking.",
            "benefits": ["GDPR compliance", "Real-time masking", "Custom pattern detection", "Audit trails"]
        },
        {
            "title": "😊 Sentiment Analysis",
            "description": "Real-time emotional intelligence to understand customer satisfaction and agent performance.",
            "benefits": ["Real-time emotion tracking", "Customer satisfaction scoring", "Agent coaching insights", "Escalation detection"]
        },
        {
            "title": "⚖️ Responsible AI",
            "description": "Ethical AI framework ensuring fairness, transparency, and accountability in all AI operations.",
            "benefits": ["Bias detection and mitigation", "Explainable AI decisions", "Compliance monitoring", "Ethical guidelines enforcement"]
        }
    ]
    
    # Display features in a 2-column layout
    col1, col2 = st.columns(2)
    for i, feature in enumerate(features):
        current_col = col1 if i % 2 == 0 else col2
        with current_col:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
                <ul>
                    {''.join([f'<li>{benefit}</li>' for benefit in feature['benefits']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

# Speaker Diarization page
elif feature_selection == "Speaker Diarization":
    show_speaker_diarization()

# Call Summarization page
elif feature_selection == "Call Summarization":
    show_call_summarization()

# PII Detection page
elif feature_selection == "PII Detection":
    show_pii_detection()

# Sentiment Analysis page
elif feature_selection == "Sentiment Analysis":
    show_sentiment_analysis()

# Responsible AI page
elif feature_selection == "Responsible AI":
    show_responsible_ai()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 <strong>Contact Center AI Solutions</strong> | Powered by Advanced Machine Learning</p>
    <p>Transforming customer service with responsible AI technology</p>
</div>
""", unsafe_allow_html=True)
