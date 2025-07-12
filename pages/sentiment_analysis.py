import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta
import json

def show_sentiment_analysis():
    st.header("😊 Sentiment Analysis")
    
    st.markdown("""
    Real-time sentiment analysis tracks customer emotions throughout conversations, 
    helping agents respond appropriately and identify potential escalations.
    """)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Live Demo", "📊 Analytics", "⚙️ Configuration", "🔌 API Usage"])
    
    with tab1:
        # Live Demo Section
        st.subheader("🎯 Real-time Sentiment Analysis")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📝 Conversation Input")
            
            # Input options
            input_method = st.radio(
                "Choose input method:",
                ["📝 Paste conversation", "📁 Upload file", "🎵 Use sample", "🔴 Live stream"]
            )
            
            if input_method == "📝 Paste conversation":
                conversation_text = st.text_area(
                    "Enter conversation for sentiment analysis:",
                    placeholder="Paste conversation transcript here...",
                    height=350
                )
            elif input_method == "📁 Upload file":
                uploaded_file = st.file_uploader(
                    "Upload conversation file",
                    type=['txt', 'csv', 'json'],
                    help="Supported formats: TXT, CSV, JSON"
                )
                if uploaded_file:
                    st.success(f"✅ File uploaded: {uploaded_file.name}")
                    conversation_text = "File content would be processed here..."
                else:
                    conversation_text = ""
            elif input_method == "🔴 Live stream":
                st.info("🔴 Live sentiment monitoring active")
                conversation_text = st.text_area(
                    "Live conversation stream:",
                    value="Agent: How can I help you today?\nCustomer: I'm really frustrated with...",
                    height=350
                )
                
                # Live monitoring controls
                col_live1, col_live2 = st.columns(2)
                with col_live1:
                    if st.button("▶️ Start Monitoring"):
                        st.success("Live monitoring started!")
                with col_live2:
                    if st.button("⏹️ Stop Monitoring"):
                        st.info("Live monitoring stopped.")
            else:  # Use sample
                conversation_text = """
Agent: Thank you for calling TechSupport Plus, this is Sarah. How can I help you today?

Customer: Hi Sarah, I'm really frustrated right now. I've been trying to access my account for three days and nothing is working! This is completely unacceptable.

Agent: I'm so sorry to hear about this frustration, Mr. Smith. I completely understand how inconvenient this must be for you. Let me help you resolve this right away.

Customer: Well, I hope you can actually help because the last person I spoke to was useless. My account number is AC-12345-6789.

Agent: I sincerely apologize for your previous experience. That's definitely not the level of service we strive for. I have your account pulled up now, and I can see exactly what's happening.

Customer: Finally! Someone who seems to know what they're doing. What's the problem?

Agent: I can see that your account was locked after multiple login attempts, which is a security feature. I'm going to unlock it right now and send you a temporary password via SMS.

Customer: Oh, that actually makes sense. I was getting pretty worried about security after all those failed attempts.

Agent: Absolutely understandable! Security is definitely a priority. I've unlocked your account and sent the temporary password to your phone ending in 4567.

Customer: Perfect! I just got the text and I'm able to log in now. Thank you so much, Sarah. You've been incredibly helpful and patient with me.

Agent: I'm so glad we got that resolved for you! Is there anything else I can help you with today?

Customer: No, that's everything. I really appreciate your excellent service. You've turned my day around!

Agent: That's wonderful to hear! Thank you for your patience, and please don't hesitate to contact us if you need anything else. Have a great day!

Customer: You too, Sarah. Thanks again!
                """
            
            st.text_area("Conversation text:", conversation_text, height=300, key="conversation_display")
            
            # Analysis options
            st.markdown("### ⚙️ Analysis Options")
            
            col_opt1, col_opt2 = st.columns(2)
            
            with col_opt1:
                sentiment_granularity = st.selectbox(
                    "Analysis Granularity",
                    ["Utterance-level", "Sentence-level", "Overall"]
                )
                
                emotion_detection = st.checkbox("Emotion Detection", value=True)
                speaker_separation = st.checkbox("Speaker Separation", value=True)
            
            with col_opt2:
                sentiment_model = st.selectbox(
                    "Sentiment Model",
                    ["BERT-Sentiment", "RoBERTa-Large", "DistilBERT", "Custom Model"]
                )
                
                confidence_display = st.checkbox("Show Confidence Scores", value=True)
                escalation_alerts = st.checkbox("Escalation Alerts", value=True)
            
            # Analyze button
            if st.button("📊 Analyze Sentiment", type="primary"):
                if conversation_text.strip():
                    with st.spinner("Analyzing sentiment... This may take a moment."):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Simulate processing steps
                        steps = [
                            "Tokenizing conversation...",
                            "Identifying speakers...",
                            "Running sentiment models...",
                            "Detecting emotions...",
                            "Calculating scores...",
                            "Generating insights..."
                        ]
                        
                        for i, step in enumerate(steps):
                            status_text.text(step)
                            progress_bar.progress((i + 1) / len(steps))
                            time.sleep(0.4)
                        
                        status_text.text("✅ Sentiment analysis complete!")
                        st.success("Sentiment analysis completed successfully!")
                else:
                    st.error("Please provide a conversation to analyze.")
        
        with col2:
            st.markdown("### 📈 Sentiment Timeline")
            
            if 'conversation_text' in locals() and conversation_text.strip():
                # Generate sample timeline data based on the conversation
                time_points = list(range(0, 300, 15))  # 5-minute call, 15-second intervals
                
                # Simulate sentiment progression that matches the conversation flow
                agent_sentiment = [0.8, 0.8, 0.9, 0.85, 0.9, 0.85, 0.9, 0.9, 0.85, 0.9, 0.9, 0.85, 0.9, 0.9, 0.8, 0.85, 0.9, 0.9, 0.85, 0.9]
                customer_sentiment = [-0.4, -0.6, -0.5, -0.3, -0.2, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 0.9, 0.9, 0.8, 0.9, 0.9]
                
                sentiment_df = pd.DataFrame({
                    'Time (seconds)': time_points,
                    'Agent Sentiment': agent_sentiment,
                    'Customer Sentiment': customer_sentiment
                })
                
                # Create sentiment timeline
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=sentiment_df['Time (seconds)'],
                    y=sentiment_df['Agent Sentiment'],
                    mode='lines+markers',
                    name='Agent',
                    line=dict(color='#667eea', width=3),
                    marker=dict(size=6)
                ))
                
                fig.add_trace(go.Scatter(
                    x=sentiment_df['Time (seconds)'],
                    y=sentiment_df['Customer Sentiment'],
                    mode='lines+markers', 
                    name='Customer',
                    line=dict(color='#28a745', width=3),
                    marker=dict(size=6)
                ))
                
                # Add reference lines
                fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Neutral")
                fig.add_hline(y=0.5, line_dash="dash", line_color="green", annotation_text="Positive")
                fig.add_hline(y=-0.5, line_dash="dash", line_color="red", annotation_text="Negative")
                
                fig.update_layout(
                    title='Real-time Sentiment Tracking',
                    xaxis_title='Time (seconds)',
                    yaxis_title='Sentiment Score',
                    yaxis=dict(range=[-1, 1]),
                    height=400,
                    showlegend=True
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Key moments annotation
                st.markdown("### 🎯 Key Sentiment Moments")
                
                moments = [
                    {"time": "0:00-0:45", "event": "Customer Initial Frustration", "sentiment": "Very Negative (-0.6)", "color": "🔴"},
                    {"time": "0:45-1:30", "event": "Agent Empathy & Acknowledgment", "sentiment": "Improving (-0.3)", "color": "🟡"},
                    {"time": "1:30-2:30", "event": "Problem Identification", "sentiment": "Neutral to Positive (+0.3)", "color": "🟢"},
                    {"time": "2:30-4:00", "event": "Solution Implementation", "sentiment": "Positive (+0.7)", "color": "🟢"},
                    {"time": "4:00-5:00", "event": "Customer Satisfaction", "sentiment": "Very Positive (+0.9)", "color": "🟢"}
                ]
                
                for moment in moments:
                    st.markdown(f"""
                    **{moment['time']}** {moment['color']} {moment['sentiment']}  
                    *{moment['event']}*
                    """)
            
            else:
                st.info("💡 Analyze a conversation to see the sentiment timeline")
                
                # Show sample visualization
                sample_data = pd.DataFrame({
                    'Time': list(range(0, 180, 10)),
                    'Sentiment': np.sin(np.linspace(0, 2*np.pi, 18)) * 0.5 + 0.2
                })
                
                fig_sample = px.line(sample_data, x='Time', y='Sentiment',
                                   title='Sample Sentiment Timeline',
                                   color_discrete_sequence=['#667eea'])
                fig_sample.add_hline(y=0, line_dash="dash", line_color="gray")
                fig_sample.update_layout(height=300)
                st.plotly_chart(fig_sample, use_container_width=True)
        
        # Detailed analysis results
        if 'conversation_text' in locals() and conversation_text.strip():
            st.markdown("### 📋 Detailed Analysis Results")
            
            col_res1, col_res2 = st.columns([2, 1])
            
            with col_res1:
                # Utterance-level analysis
                st.markdown("#### 💬 Utterance-level Sentiment")
                
                utterance_data = {
                    'Speaker': ['Agent', 'Customer', 'Agent', 'Customer', 'Agent', 'Customer', 'Agent', 'Customer'],
                    'Utterance': [
                        'Thank you for calling TechSupport Plus...',
                        'Hi Sarah, I\'m really frustrated right now...',
                        'I\'m so sorry to hear about this frustration...',
                        'Well, I hope you can actually help...',
                        'I sincerely apologize for your previous experience...',
                        'Finally! Someone who seems to know...',
                        'I can see that your account was locked...',
                        'Perfect! I just got the text and I\'m able to log in...'
                    ],
                    'Sentiment': ['Positive', 'Very Negative', 'Empathetic', 'Negative', 'Apologetic', 'Hopeful', 'Informative', 'Very Positive'],
                    'Score': [0.8, -0.6, 0.9, -0.3, 0.85, 0.4, 0.7, 0.9],
                    'Confidence': [0.92, 0.95, 0.88, 0.91, 0.89, 0.86, 0.93, 0.96],
                    'Emotions': ['Professional', 'Frustrated, Angry', 'Empathetic, Caring', 'Skeptical', 'Apologetic', 'Relieved', 'Helpful', 'Grateful, Happy']
                }
                
                utterance_df = pd.DataFrame(utterance_data)
                st.dataframe(utterance_df, use_container_width=True)
            
            with col_res2:
                st.markdown("#### 📊 Summary Metrics")
                
                st.metric("Overall Satisfaction", "8.7/10", "+6.3 improvement")
                st.metric("Agent Performance", "9.2/10", "Excellent")
                st.metric("Resolution Success", "✅ Yes", "First call")
                st.metric("Escalation Risk", "0%", "No risk detected")
                
                # Emotion distribution
                emotion_data = pd.DataFrame({
                    'Emotion': ['Happy', 'Grateful', 'Frustrated', 'Relieved', 'Professional'],
                    'Percentage': [35, 25, 15, 15, 10]
                })
                
                fig_emotion = px.pie(emotion_data, values='Percentage', names='Emotion',
                                   title='Emotion Distribution')
                fig_emotion.update_layout(height=300)
                st.plotly_chart(fig_emotion, use_container_width=True)
            
            # Insights and recommendations
            st.markdown("### 💡 AI Insights & Recommendations")
            
            insights_col1, insights_col2 = st.columns(2)
            
            with insights_col1:
                st.markdown("""
                **🎯 Key Insights:**
                - Customer started highly frustrated (-0.6) but ended very satisfied (+0.9)
                - Agent demonstrated excellent empathy and problem-solving skills
                - Sentiment trajectory shows consistent improvement throughout call
                - No escalation triggers detected
                - Resolution achieved within acceptable timeframe
                """)
            
            with insights_col2:
                st.markdown("""
                **📈 Recommendations:**
                - Use this call as a training example for empathy techniques
                - Agent Sarah shows best practices for handling frustrated customers
                - Consider recognition for excellent customer service performance
                - Document resolution process for knowledge base
                - Monitor similar account lockout issues for process improvement
                """)
    
    with tab2:
        # Analytics Section
        st.subheader("📊 Sentiment Analytics Dashboard")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Daily Conversations", "2,847", "+15%")
        with col2:
            st.metric("Average Satisfaction", "7.8/10", "+0.3")
        with col3:
            st.metric("Positive Sentiment", "72%", "+5%")
        with col4:
            st.metric("Escalation Rate", "3.2%", "-1.1%")
        
        # Sentiment trends
        st.markdown("### 📈 Sentiment Trends")
        
        # Generate sample analytics data
        dates = pd.date_range(start='2024-01-01', end='2024-07-12', freq='D')
        analytics_data = {
            'Date': dates,
            'Avg_Sentiment': np.random.uniform(0.3, 0.8, len(dates)),
            'Positive_Calls': np.random.uniform(0.65, 0.85, len(dates)),
            'Negative_Calls': np.random.uniform(0.05, 0.20, len(dates)),
            'Escalations': np.random.randint(5, 50, len(dates)),
            'Call_Volume': np.random.randint(1500, 3500, len(dates))
        }
        
        analytics_df = pd.DataFrame(analytics_data)
        
        # Average sentiment trend
        fig_sentiment_trend = px.line(analytics_df, x='Date', y='Avg_Sentiment',
                                     title='Average Daily Sentiment Score',
                                     color_discrete_sequence=['#667eea'])
        fig_sentiment_trend.update_layout(height=400)
        st.plotly_chart(fig_sentiment_trend, use_container_width=True)
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Sentiment distribution over time
            fig_dist = go.Figure()
            
            fig_dist.add_trace(go.Scatter(
                x=analytics_df['Date'],
                y=analytics_df['Positive_Calls'],
                mode='lines',
                name='Positive',
                line=dict(color='#28a745'),
                fill='tonexty'
            ))
            
            fig_dist.add_trace(go.Scatter(
                x=analytics_df['Date'],
                y=analytics_df['Negative_Calls'],
                mode='lines',
                name='Negative',
                line=dict(color='#dc3545'),
                fill='tozeroy'
            ))
            
            fig_dist.update_layout(
                title='Positive vs Negative Sentiment Distribution',
                height=350,
                yaxis_title='Percentage'
            )
            st.plotly_chart(fig_dist, use_container_width=True)
        
        with col_chart2:
            # Escalation correlation
            fig_escalation = px.scatter(analytics_df, x='Avg_Sentiment', y='Escalations',
                                       color='Call_Volume',
                                       title='Sentiment vs Escalations',
                                       color_continuous_scale='Viridis')
            fig_escalation.update_layout(height=350)
            st.plotly_chart(fig_escalation, use_container_width=True)
        
        # Department/Agent performance
        st.markdown("### 👥 Department & Agent Performance")
        
        # Department comparison
        dept_data = pd.DataFrame({
            'Department': ['Technical Support', 'Billing', 'Sales', 'Customer Service', 'Returns'],
            'Avg_Sentiment': [7.8, 6.9, 8.4, 7.2, 6.5],
            'Call_Volume': [2847, 1923, 1654, 2156, 892],
            'Satisfaction_Rate': [87, 79, 91, 82, 74]
        })
        
        fig_dept = px.bar(dept_data, x='Department', y='Avg_Sentiment',
                         color='Satisfaction_Rate',
                         title='Average Sentiment by Department',
                         color_continuous_scale='RdYlGn')
        fig_dept.update_layout(height=400)
        st.plotly_chart(fig_dept, use_container_width=True)
        
        # Top performing agents
        st.markdown("### 🏆 Top Performing Agents")
        
        agent_data = pd.DataFrame({
            'Agent': ['Sarah M.', 'Mike R.', 'Lisa K.', 'David P.', 'Anna L.'],
            'Avg_Sentiment': [8.9, 8.7, 8.5, 8.3, 8.1],
            'Calls_Handled': [245, 289, 267, 223, 198],
            'Resolution_Rate': [94, 91, 89, 87, 86],
            'Customer_Satisfaction': [9.2, 8.8, 8.9, 8.5, 8.7]
        })
        
        st.dataframe(agent_data, use_container_width=True)
        
        # Hourly sentiment patterns
        st.markdown("### 🕐 Hourly Sentiment Patterns")
        
        hours = list(range(9, 18))  # Business hours 9 AM to 5 PM
        hourly_sentiment = [7.2, 7.8, 8.1, 7.9, 7.4, 6.8, 7.1, 7.6, 7.9]
        
        hourly_df = pd.DataFrame({
            'Hour': [f"{h}:00" for h in hours],
            'Avg_Sentiment': hourly_sentiment
        })
        
        fig_hourly = px.bar(hourly_df, x='Hour', y='Avg_Sentiment',
                           title='Average Sentiment by Hour of Day',
                           color_discrete_sequence=['#ffc107'])
        fig_hourly.update_layout(height=350)
        st.plotly_chart(fig_hourly, use_container_width=True)
    
    with tab3:
        # Configuration Section
        st.subheader("⚙️ Sentiment Analysis Configuration")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🧠 Model Configuration")
            
            # Model selection
            sentiment_model = st.selectbox(
                "Primary Sentiment Model",
                ["BERT-Large-Uncased", "RoBERTa-Large", "DistilBERT", "XLNet", "Custom Model"],
                index=0
            )
            
            emotion_model = st.selectbox(
                "Emotion Detection Model",
                ["GoEmotions", "EmoRoBERTa", "BERT-Emotion", "Custom Emotions"],
                index=0
            )
            
            # Analysis settings
            st.markdown("### 📊 Analysis Settings")
            
            analysis_granularity = st.selectbox(
                "Default Granularity",
                ["Real-time (streaming)", "Utterance-level", "Sentence-level", "Turn-level", "Overall"],
                index=1
            )
            
            sentiment_scale = st.selectbox(
                "Sentiment Scale",
                ["5-point (-2 to +2)", "7-point (-3 to +3)", "10-point (1 to 10)", "Continuous (-1 to +1)"],
                index=3
            )
            
            # Thresholds
            st.markdown("### 🎯 Alert Thresholds")
            
            escalation_threshold = st.slider("Escalation Alert Threshold", -1.0, 0.0, -0.5, 0.1)
            satisfaction_threshold = st.slider("Low Satisfaction Alert", 0.0, 1.0, 0.3, 0.1)
            confidence_minimum = st.slider("Minimum Confidence Score", 0.5, 1.0, 0.75, 0.05)
            
            # Language settings
            languages = st.multiselect(
                "Supported Languages",
                ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Chinese", "Japanese"],
                default=["English"]
            )
        
        with col2:
            st.markdown("### 🎛️ Real-time Processing")
            
            # Real-time settings
            processing_mode = st.selectbox(
                "Processing Mode",
                ["Real-time streaming", "Batch processing", "Hybrid"],
                index=0
            )
            
            update_frequency = st.selectbox(
                "Update Frequency",
                ["Every utterance", "Every 5 seconds", "Every 10 seconds", "Every 30 seconds"],
                index=1
            )
            
            buffer_size = st.number_input("Audio Buffer Size (seconds)", 1, 30, 5)
            
            # Alert configuration
            st.markdown("### 🚨 Alert Configuration")
            
            alert_channels = st.multiselect(
                "Alert Channels",
                ["Dashboard", "Email", "SMS", "Slack", "Teams", "Webhook"],
                default=["Dashboard"]
            )
            
            escalation_actions = st.multiselect(
                "Escalation Actions",
                ["Supervisor notification", "Call recording", "Screen pop", "Agent coaching", "Transfer suggestion"],
                default=["Supervisor notification"]
            )
            
            # Custom emotions
            st.markdown("### 😊 Custom Emotions")
            
            default_emotions = ["Joy", "Sadness", "Anger", "Fear", "Surprise", "Disgust", "Trust", "Anticipation"]
            
            selected_emotions = st.multiselect(
                "Track Emotions",
                default_emotions + ["Frustration", "Satisfaction", "Confusion", "Gratitude"],
                default=default_emotions
            )
            
            custom_emotion = st.text_input("Add Custom Emotion", placeholder="e.g., Excitement")
            
            if st.button("➕ Add Custom Emotion"):
                if custom_emotion:
                    st.success(f"Custom emotion '{custom_emotion}' added!")
                else:
                    st.error("Please enter an emotion name")
            
            # Save configuration
            if st.button("💾 Save Configuration", type="primary"):
                config = {
                    "models": {
                        "sentiment_model": sentiment_model,
                        "emotion_model": emotion_model
                    },
                    "analysis": {
                        "granularity": analysis_granularity,
                        "sentiment_scale": sentiment_scale,
                        "languages": languages
                    },
                    "thresholds": {
                        "escalation": escalation_threshold,
                        "satisfaction": satisfaction_threshold,
                        "confidence": confidence_minimum
                    },
                    "real_time": {
                        "processing_mode": processing_mode,
                        "update_frequency": update_frequency,
                        "buffer_size": buffer_size
                    },
                    "alerts": {
                        "channels": alert_channels,
                        "escalation_actions": escalation_actions
                    },
                    "emotions": selected_emotions
                }
                
                st.success("Configuration saved successfully!")
                st.json(config)
        
        # Model performance comparison
        st.markdown("### 🏆 Model Performance Comparison")
        
        model_comparison = pd.DataFrame({
            'Model': ['BERT-Large', 'RoBERTa-Large', 'DistilBERT', 'XLNet', 'Custom Model'],
            'Accuracy': [91.2, 92.8, 89.5, 90.7, 94.1],
            'Speed (ms)': [145, 156, 98, 178, 112],
            'Memory (GB)': [3.2, 3.8, 1.2, 4.1, 2.1],
            'Languages': [104, 100, 104, 100, 25]
        })
        
        st.dataframe(model_comparison, use_container_width=True)
    
    with tab4:
        # API Usage Section
        st.subheader("🔌 API Usage & Integration")
        
        # API examples
        st.markdown("### 💻 Code Examples")
        
        api_tab1, api_tab2, api_tab3 = st.tabs(["Python", "cURL", "JavaScript"])
        
        with api_tab1:
            st.markdown("#### Python SDK Example")
            python_code = '''
import requests
import json
import websocket

# Sentiment Analysis API
url = "https://api.contactcenter.ai/v1/sentiment-analysis"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Single text analysis
payload = {
    "text": "I'm really frustrated with this service!",
    "options": {
        "granularity": "utterance",
        "include_emotions": True,
        "include_confidence": True,
        "language": "en"
    }
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

if response.status_code == 200:
    sentiment = result["sentiment"]
    emotions = result["emotions"]
    confidence = result["confidence"]
    
    print(f"Sentiment: {sentiment['label']} ({sentiment['score']})")
    print(f"Confidence: {confidence}")
    print(f"Emotions: {emotions}")
else:
    print(f"Error: {result['error']}")

# Conversation analysis
conversation_payload = {
    "conversation": [
        {"speaker": "agent", "text": "How can I help you today?", "timestamp": "2024-07-12T10:00:00Z"},
        {"speaker": "customer", "text": "I'm having issues with my account", "timestamp": "2024-07-12T10:00:15Z"}
    ],
    "options": {
        "track_sentiment_flow": True,
        "detect_escalation_risk": True,
        "speaker_specific_analysis": True
    }
}

conv_response = requests.post(
    url + "/conversation", 
    headers=headers, 
    json=conversation_payload
)

# Real-time sentiment monitoring
def on_sentiment_update(ws, message):
    data = json.loads(message)
    sentiment_score = data["sentiment"]["score"]
    
    if sentiment_score < -0.5:
        print("⚠️ Escalation risk detected!")
    
    print(f"Real-time sentiment: {sentiment_score}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

# Connect to real-time stream
ws = websocket.WebSocketApp(
    "wss://api.contactcenter.ai/v1/sentiment-analysis/stream",
    header={"Authorization": "Bearer YOUR_API_KEY"},
    on_message=on_sentiment_update,
    on_error=on_error
)

ws.run_forever()

# Batch processing
batch_payload = {
    "conversations": [
        {"id": "conv1", "messages": [...]},
        {"id": "conv2", "messages": [...]}
    ],
    "options": {
        "granularity": "utterance",
        "include_emotions": True
    }
}

batch_response = requests.post(
    url + "/batch",
    headers=headers,
    json=batch_payload
)
'''
            st.code(python_code, language='python')
        
        with api_tab2:
            st.markdown("#### cURL Example")
            curl_code = '''
# Single text sentiment analysis
curl -X POST https://api.contactcenter.ai/v1/sentiment-analysis \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "text": "I am really frustrated with this service!",
    "options": {
      "granularity": "utterance",
      "include_emotions": true,
      "include_confidence": true,
      "language": "en"
    }
  }'

# Response
{
  "job_id": "sent_12345",
  "status": "completed",
  "processing_time": 0.08,
  "sentiment": {
    "label": "negative",
    "score": -0.72,
    "confidence": 0.94
  },
  "emotions": {
    "primary": "frustration",
    "secondary": ["anger", "disappointment"],
    "scores": {
      "frustration": 0.85,
      "anger": 0.62,
      "disappointment": 0.48
    }
  },
  "escalation_risk": {
    "level": "medium", 
    "score": 0.68,
    "triggers": ["negative_sentiment", "frustration_keywords"]
  }
}

# Conversation analysis
curl -X POST https://api.contactcenter.ai/v1/sentiment-analysis/conversation \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "conversation": [
      {
        "speaker": "agent",
        "text": "How can I help you today?",
        "timestamp": "2024-07-12T10:00:00Z"
      },
      {
        "speaker": "customer", 
        "text": "I am having issues with my account",
        "timestamp": "2024-07-12T10:00:15Z"
      }
    ],
    "options": {
      "track_sentiment_flow": true,
      "detect_escalation_risk": true
    }
  }'

# Batch processing
curl -X POST https://api.contactcenter.ai/v1/sentiment-analysis/batch \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "conversations": [
      {"id": "conv1", "messages": [...]},
      {"id": "conv2", "messages": [...]}
    ]
  }'
'''
            st.code(curl_code, language='bash')
        
        with api_tab3:
            st.markdown("#### JavaScript/Node.js Example")
            js_code = '''
const axios = require('axios');
const WebSocket = require('ws');

class SentimentAnalyzer {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = 'https://api.contactcenter.ai/v1';
    }
    
    async analyzeSentiment(text, options = {}) {
        const payload = {
            text: text,
            options: {
                granularity: options.granularity || 'utterance',
                include_emotions: options.includeEmotions || true,
                include_confidence: options.includeConfidence || true,
                language: options.language || 'en'
            }
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/sentiment-analysis`,
                payload,
                {
                    headers: {
                        'Authorization': `Bearer ${this.apiKey}`,
                        'Content-Type': 'application/json'
                    }
                }
            );
            
            return response.data;
            
        } catch (error) {
            console.error('Sentiment analysis error:', error.response.data);
            throw error;
        }
    }
    
    async analyzeConversation(conversation, options = {}) {
        const payload = {
            conversation: conversation,
            options: {
                track_sentiment_flow: options.trackFlow || true,
                detect_escalation_risk: options.detectEscalation || true,
                speaker_specific_analysis: options.speakerAnalysis || true
            }
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/sentiment-analysis/conversation`,
                payload,
                {
                    headers: {
                        'Authorization': `Bearer ${this.apiKey}`,
                        'Content-Type': 'application/json'
                    }
                }
            );
            
            return response.data;
            
        } catch (error) {
            console.error('Conversation analysis error:', error.response.data);
            throw error;
        }
    }
    
    // Real-time sentiment monitoring
    startRealtimeMonitoring(onSentimentUpdate, onEscalationAlert) {
        const ws = new WebSocket('wss://api.contactcenter.ai/v1/sentiment-analysis/stream', {
            headers: {
                'Authorization': `Bearer ${this.apiKey}`
            }
        });
        
        ws.on('message', (data) => {
            const result = JSON.parse(data);
            
            // Handle sentiment updates
            if (result.type === 'sentiment_update') {
                onSentimentUpdate(result);
            }
            
            // Handle escalation alerts
            if (result.type === 'escalation_alert') {
                onEscalationAlert(result);
            }
        });
        
        ws.on('error', (error) => {
            console.error('WebSocket error:', error);
        });
        
        return ws;
    }
    
    // Send real-time text for analysis
    sendRealtimeText(ws, text, speaker, timestamp) {
        const message = {
            type: 'analyze_text',
            text: text,
            speaker: speaker,
            timestamp: timestamp || new Date().toISOString()
        };
        
        ws.send(JSON.stringify(message));
    }
}

// Usage example
const analyzer = new SentimentAnalyzer('YOUR_API_KEY');

async function analyzeCustomerInteraction() {
    const conversation = [
        {
            speaker: 'agent',
            text: 'How can I help you today?',
            timestamp: '2024-07-12T10:00:00Z'
        },
        {
            speaker: 'customer',
            text: 'I am really frustrated with this service!',
            timestamp: '2024-07-12T10:00:15Z'
        }
    ];
    
    try {
        // Analyze conversation
        const result = await analyzer.analyzeConversation(conversation);
        
        console.log('Conversation Analysis:', result);
        
        // Check for escalation risk
        if (result.escalation_risk && result.escalation_risk.level === 'high') {
            console.log('🚨 High escalation risk detected!');
        }
        
        // Start real-time monitoring
        const ws = analyzer.startRealtimeMonitoring(
            (sentimentData) => {
                console.log('Sentiment update:', sentimentData.sentiment);
            },
            (escalationData) => {
                console.log('🚨 Escalation alert:', escalationData);
            }
        );
        
        // Send real-time text
        analyzer.sendRealtimeText(ws, 'Thank you for your patience', 'agent');
        
    } catch (error) {
        console.error('Error analyzing interaction:', error);
    }
}

analyzeCustomerInteraction();
'''
            st.code(js_code, language='javascript')
        
        # Response format
        st.markdown("### 📄 API Response Format")
        
        sample_response = {
            "job_id": "sent_12345",
            "status": "completed",
            "processing_time": 0.08,
            "sentiment": {
                "label": "negative",
                "score": -0.72,
                "confidence": 0.94,
                "scale": "continuous"
            },
            "emotions": {
                "primary": "frustration",
                "secondary": ["anger", "disappointment"],
                "scores": {
                    "frustration": 0.85,
                    "anger": 0.62,
                    "disappointment": 0.48,
                    "joy": 0.02,
                    "sadness": 0.31
                }
            },
            "escalation_risk": {
                "level": "medium",
                "score": 0.68,
                "triggers": ["negative_sentiment", "frustration_keywords"],
                "recommendations": ["supervisor_notification", "empathy_response"]
            },
            "conversation_analysis": {
                "sentiment_trajectory": "declining",
                "overall_satisfaction": 3.2,
                "key_moments": [
                    {
                        "timestamp": "2024-07-12T10:00:15Z",
                        "event": "frustration_peak",
                        "sentiment_score": -0.72
                    }
                ]
            },
            "metadata": {
                "model_version": "v2.1.0",
                "language": "en",
                "processing_method": "real_time"
            }
        }
        
        st.json(sample_response)
        
        # Webhooks and integration
        st.markdown("### 🔔 Webhooks & Integration")
        
        col_webhook1, col_webhook2 = st.columns(2)
        
        with col_webhook1:
            st.markdown("""
            **Webhook Events**
            - `sentiment_analyzed`: New sentiment score
            - `escalation_detected`: High escalation risk
            - `satisfaction_low`: Low satisfaction alert
            - `emotion_change`: Significant emotion shift
            - `conversation_complete`: End of interaction
            """)
        
        with col_webhook2:
            st.markdown("""
            **Integration Options**
            - Real-time dashboards
            - CRM system updates
            - Agent coaching tools
            - Quality assurance
            - Business intelligence
            """)
