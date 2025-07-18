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
# Import new revolutionary AI features
from pages.agentic_ai import show_agentic_ai
from pages.real_time_coaching import show_real_time_coaching
from pages.omnichannel_integration import show_omnichannel_integration
from pages.voice_biometrics import show_voice_biometrics

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
    /* Sidebar button styling */
    .stButton > button {
        width: 100%;
        margin-bottom: 5px;
        border-radius: 8px;
        border: 1px solid #ddd;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #667eea;
        color: white;
        border-color: #667eea;
    }
    /* Active button indicator */
    .nav-section {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Contact Center AI Revolution: 2024-2025 Innovation Landscape</h1>
    <p>Agentic AI systems that autonomously resolve 80% of customer issues with 400% productivity gains</p>
    <p><strong>Leading the transformation from reactive cost centers to proactive revenue drivers</strong></p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")

# Initialize session state for selected feature
if 'selected_feature' not in st.session_state:
    st.session_state.selected_feature = "📊 Overview"

# Show current page indicator
st.sidebar.markdown(f"**Current Page:** {st.session_state.selected_feature}")
st.sidebar.markdown("---")

# Sidebar buttons for navigation
if st.sidebar.button("📊 Overview", use_container_width=True):
    st.session_state.selected_feature = "📊 Overview"

if st.sidebar.button("🤖 Agentic AI", use_container_width=True):
    st.session_state.selected_feature = "🤖 Agentic AI Revolution"

if st.sidebar.button("🎯 Real-Time Coaching", use_container_width=True):
    st.session_state.selected_feature = "🎯 Real-Time Coaching"

if st.sidebar.button("🌐 Omnichannel Integration", use_container_width=True):
    st.session_state.selected_feature = "🌐 Omnichannel Integration"

if st.sidebar.button("🔐 Voice Biometrics", use_container_width=True):
    st.session_state.selected_feature = "🔐 Voice Biometrics"

if st.sidebar.button("🎤 Speaker Diarization", use_container_width=True):
    st.session_state.selected_feature = "🎤 Speaker Diarization"

if st.sidebar.button("📝 Call Summarization", use_container_width=True):
    st.session_state.selected_feature = "📝 Call Summarization"

if st.sidebar.button("🔒 PII Detection", use_container_width=True):
    st.session_state.selected_feature = "🔒 PII Detection"

if st.sidebar.button("😊 Sentiment Analysis", use_container_width=True):
    st.session_state.selected_feature = "😊 Sentiment Analysis"

if st.sidebar.button("⚖️ Responsible AI", use_container_width=True):
    st.session_state.selected_feature = "⚖️ Responsible AI"

# Get the selected feature
feature_selection = st.session_state.selected_feature

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
if feature_selection == "📊 Overview":
    # Overview page with metrics and charts
    st.markdown("## 📊 AI Solutions Overview")
    
    # Sample data
    df = generate_sample_data()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🤖 Agentic AI Resolution",
            value="80%",
            delta="Target by 2029"
        )
    
    with col2:
        st.metric(
            label="🚀 Productivity Gains",
            value="400%",
            delta="Industry leading results"
        )
    
    with col3:
        st.metric(
            label="� Market Value",
            value="$19.5B",
            delta="By 2034 (18.2% CAGR)"
        )
    
    with col4:
        st.metric(
            label="🎯 Customer Interactions",
            value="95%",
            delta="AI-handled by 2025"
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
    st.markdown("### 🌟 Revolutionary AI Features")
    
    features = [
        {
            "title": "🤖 Agentic AI Systems",
            "description": "Autonomous AI that resolves 80% of customer issues without human intervention by 2029, featuring non-deterministic intelligence with configurable guardrails.",
            "benefits": ["Autonomous decision-making", "400% productivity gains", "$100M+ revenue generation", "Genesys Cloud AI Studio"]
        },
        {
            "title": "🎯 Real-Time Coaching",
            "description": "Google Cloud AI Trainer with Gemini-powered coaching providing personalized training and contextual guidance during customer interactions.",
            "benefits": ["5X conversation growth", "68% sales improvement", "$20M operational savings", "Mood insights and prediction"]
        },
        {
            "title": "🌐 Omnichannel Integration",
            "description": "Salesforce + Amazon Connect partnership delivering seamless voice, chat, email integration with complete context preservation across 26 languages.",
            "benefits": ["Zero context loss", "Dynamic language switching", "Mobile-first authentication", "Unified agent desktop"]
        },
        {
            "title": "🔐 Voice Biometrics Security",
            "description": "Pindrop's revolutionary deepfake warranty achieving 99% detection accuracy with behavioral biometrics projected to reach $14B market by 2032.",
            "benefits": ["99% deepfake detection", "<1% false positives", "34.8% ATO reduction", "Real-time fraud prevention"]
        },
        {
            "title": "🎤 Advanced Speaker Diarization",
            "description": "Enhanced AI that identifies and separates different speakers in audio conversations with 95%+ accuracy and real-time processing.",
            "benefits": ["Real-time speaker identification", "Multi-language support", "Noise reduction", "Quality assurance"]
        },
        {
            "title": "📝 Intelligent Call Summarization",
            "description": "State-of-the-art NLP models for automatic conversation summarization with action item identification and performance analytics.",
            "benefits": ["Automatic key point extraction", "Customizable summary formats", "Action item identification", "Performance analytics"]
        },
        {
            "title": "🔒 Advanced PII Detection",
            "description": "Comprehensive protection of personally identifiable information with real-time detection, masking, and GDPR compliance automation.",
            "benefits": ["GDPR compliance", "Real-time masking", "Custom pattern detection", "Audit trails"]
        },
        {
            "title": "😊 Emotional Intelligence",
            "description": "Real-time sentiment analysis with emotional intelligence to understand customer satisfaction and provide agent coaching insights.",
            "benefits": ["Real-time emotion tracking", "Customer satisfaction scoring", "Agent coaching insights", "Escalation detection"]
        },
        {
            "title": "⚖️ Responsible AI Framework",
            "description": "Ethical AI ensuring fairness, transparency, and accountability with bias detection and explainable AI decisions.",
            "benefits": ["Bias detection and mitigation", "Explainable AI decisions", "Compliance monitoring", "Ethical guidelines enforcement"]
        }
    ]
    
    # Display features in a 3-column layout for better organization
    col1, col2, col3 = st.columns(3)
    for i, feature in enumerate(features):
        current_col = [col1, col2, col3][i % 3]
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

    # Market insights and projections
    st.markdown("### 📈 Market Transformation Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🚀 **Breakthrough Achievements**
        - **Genesys Cloud:** 40% of customers using AI capabilities
        - **IONOS Group:** 68% improvement in sales conversions  
        - **Bell Canada:** $20 million in operational savings
        - **Best Buy:** 90 seconds reduction in resolution time
        """)
        
        st.markdown("""
        #### 🎯 **Gartner 2029 Predictions**
        - 80% autonomous issue resolution
        - 30% reduction in operational costs
        - 95% AI-handled customer interactions
        - $19.5B market size by 2034
        """)
    
    with col2:
        st.markdown("""
        #### 🏆 **Industry Leadership**
        - **Amazon Connect:** Unlimited AI usage with predictable pricing
        - **NICE CXone:** 100% interaction analysis vs 20% sampling
        - **Microsoft Copilot:** Real-time suggestions across 26 languages
        - **Pindrop Security:** 99% deepfake detection accuracy
        """)
        
        st.markdown("""
        #### 💡 **Innovation Impact**
        - Conversational AI: 24% CAGR growth
        - Behavioral Biometrics: $14B market by 2032
        - Voice Recognition: 3x faster than typing
        - Emotional Intelligence: Real-time mood insights
        """)

# Agentic AI Revolution page
elif feature_selection == "🤖 Agentic AI Revolution":
    show_agentic_ai()

# Real-Time Coaching page
elif feature_selection == "🎯 Real-Time Coaching":
    show_real_time_coaching()

# Omnichannel Integration page
elif feature_selection == "🌐 Omnichannel Integration":
    show_omnichannel_integration()

# Voice Biometrics page
elif feature_selection == "🔐 Voice Biometrics":
    show_voice_biometrics()

# Speaker Diarization page
elif feature_selection == "🎤 Speaker Diarization":
    show_speaker_diarization()

# Call Summarization page
elif feature_selection == "📝 Call Summarization":
    show_call_summarization()

# PII Detection page
elif feature_selection == "🔒 PII Detection":
    show_pii_detection()

# Sentiment Analysis page
elif feature_selection == "😊 Sentiment Analysis":
    show_sentiment_analysis()

# Responsible AI page
elif feature_selection == "⚖️ Responsible AI":
    show_responsible_ai()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 <strong>Contact Center AI Revolution: 2024-2025</strong> | Powered by Advanced Machine Learning & Agentic AI</p>
    <p>Transforming customer service with autonomous AI systems that resolve 80% of issues</p>
    <p><small>Market projected to reach $19.5B by 2034 | Leading organizations achieving 400% productivity gains</small></p>
</div>
""", unsafe_allow_html=True)
