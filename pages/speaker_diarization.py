import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from io import BytesIO
import base64

def show_speaker_diarization():
    st.header("🎤 Speaker Diarization")
    
    st.markdown("""
    Speaker Diarization is the process of partitioning an audio stream into homogeneous segments 
    according to the speaker identity. Our AI system can identify "who spoke when" in conversations.
    """)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Live Demo", "📊 Analytics", "⚙️ Configuration", "📋 API Usage"])
    
    with tab1:
        # Live Demo Section
        st.subheader("🎯 Audio Processing Demo")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # File upload section
            st.markdown("### 📁 Upload Audio File")
            uploaded_file = st.file_uploader(
                "Choose an audio file", 
                type=['wav', 'mp3', 'flac', 'm4a'],
                help="Supported formats: WAV, MP3, FLAC, M4A"
            )
            
            if uploaded_file is not None:
                st.success(f"✅ File uploaded: {uploaded_file.name}")
                
                # Processing options
                st.markdown("### ⚙️ Processing Options")
                col_opt1, col_opt2 = st.columns(2)
                
                with col_opt1:
                    min_speakers = st.slider("Minimum speakers", 1, 5, 2)
                    enable_vad = st.checkbox("Voice Activity Detection", value=True)
                
                with col_opt2:
                    max_speakers = st.slider("Maximum speakers", 2, 10, 5)
                    quality_mode = st.selectbox("Quality Mode", ["Fast", "Balanced", "High Quality"])
                
                # Process button
                if st.button("🚀 Process Audio", type="primary"):
                    with st.spinner("Processing audio... This may take a few moments."):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Simulate processing steps
                        steps = [
                            "Loading audio file...",
                            "Extracting features...",
                            "Applying voice activity detection...",
                            "Clustering speaker embeddings...",
                            "Generating speaker timeline...",
                            "Creating transcript..."
                        ]
                        
                        for i, step in enumerate(steps):
                            status_text.text(step)
                            progress_bar.progress((i + 1) / len(steps))
                            time.sleep(0.5)
                        
                        status_text.text("✅ Processing complete!")
                        st.success("Audio processing completed successfully!")
            
            else:
                # Sample data when no file is uploaded
                st.info("💡 Upload an audio file above or use our sample conversation below")
                
                if st.button("🎵 Use Sample Audio", type="secondary"):
                    st.success("Sample audio loaded!")
            
            # Sample transcript with speaker labels
            st.markdown("### 📝 Diarized Transcript")
            
            sample_transcript = """
🟦 **Speaker 1 (Agent)** [00:00 - 00:15]
Thank you for calling TechSupport Plus, this is Sarah. How can I help you today?

🟩 **Speaker 2 (Customer)** [00:15 - 00:45]
Hi Sarah, I'm having trouble with my account. My name is John Smith, and my account number is AC-12345-6789. I can't access my dashboard.

🟦 **Speaker 1 (Agent)** [00:45 - 01:18]
I understand your frustration, Mr. Smith. Let me look up your account using the number AC-12345-6789. Can you also provide your email address for verification?

🟩 **Speaker 2 (Customer)** [01:18 - 02:00]
Sure, it's john.smith@email.com. I've been trying to log in for the past hour and it keeps saying my password is incorrect.

🟦 **Speaker 1 (Agent)** [02:00 - 02:45]
I see the issue here. It looks like your account was temporarily locked due to multiple failed login attempts. I can unlock it for you right now. For security purposes, I'll need to verify your phone number ending in 4567.

🟩 **Speaker 2 (Customer)** [02:45 - 03:05]
Yes, that's correct. Thank you so much for your help, Sarah!

🟦 **Speaker 1 (Agent)** [03:05 - 03:25]
You're welcome! I've unlocked your account. You should be able to log in now. Is there anything else I can help you with today?

🟩 **Speaker 2 (Customer)** [03:25 - 03:35]
No, that's perfect. Thank you again!

🟦 **Speaker 1 (Agent)** [03:35 - 03:45]
Have a great day, Mr. Smith!
            """
            
            st.text_area("Speaker-labeled conversation:", sample_transcript, height=400)
            
            # Export options
            st.markdown("### 📤 Export Results")
            col_exp1, col_exp2, col_exp3 = st.columns(3)
            
            with col_exp1:
                if st.button("📄 Export TXT"):
                    st.success("Transcript exported as TXT!")
            
            with col_exp2:
                if st.button("📊 Export CSV"):
                    st.success("Data exported as CSV!")
            
            with col_exp3:
                if st.button("🔊 Export Audio Segments"):
                    st.success("Audio segments exported!")
        
        with col2:
            st.markdown("### ⏱️ Speaker Timeline")
            
            # Generate sample timeline data
            timeline_data = {
                'Speaker': ['Agent', 'Customer', 'Agent', 'Customer', 'Agent', 'Customer', 'Agent', 'Customer', 'Agent'],
                'Start_Time': [0, 15, 45, 78, 120, 165, 185, 205, 215],
                'End_Time': [15, 45, 78, 120, 165, 185, 205, 215, 225],
                'Duration': [15, 30, 33, 42, 45, 20, 20, 10, 10]
            }
            
            timeline_df = pd.DataFrame(timeline_data)
            
            # Create timeline visualization
            fig = px.timeline(timeline_df, x_start="Start_Time", x_end="End_Time", y="Speaker", 
                             color="Speaker", title="Speaker Timeline",
                             color_discrete_map={'Agent': '#667eea', 'Customer': '#28a745'})
            fig.update_layout(height=500, showlegend=True)
            st.plotly_chart(fig, use_container_width=True)
            
            # Speaker statistics
            st.markdown("### 📈 Speaker Statistics")
            
            agent_time = timeline_df[timeline_df['Speaker'] == 'Agent']['Duration'].sum()
            customer_time = timeline_df[timeline_df['Speaker'] == 'Customer']['Duration'].sum()
            total_time = agent_time + customer_time
            
            col_stat1, col_stat2 = st.columns(2)
            
            with col_stat1:
                st.metric("👨‍💼 Agent Talk Time", f"{agent_time}s", f"{agent_time/total_time*100:.1f}%")
                st.metric("🎯 Speaker Accuracy", "94.2%", "+2.1%")
            
            with col_stat2:
                st.metric("👤 Customer Talk Time", f"{customer_time}s", f"{customer_time/total_time*100:.1f}%")
                st.metric("🔄 Speaker Changes", len(timeline_df), "optimal")
    
    with tab2:
        # Analytics Section
        st.subheader("📊 Performance Analytics")
        
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Speaker Accuracy", "94.2%", "+2.1%")
        with col2:
            st.metric("Processing Speed", "1.2x real-time", "+0.3x")
        with col3:
            st.metric("Average Speakers", "2.3", "per call")
        with col4:
            st.metric("Error Rate", "0.8%", "-0.2%")
        
        # Historical performance
        st.markdown("### 📈 Historical Performance")
        
        # Generate sample performance data
        dates = pd.date_range(start='2024-01-01', end='2024-07-12', freq='D')
        performance_data = {
            'Date': dates,
            'Accuracy': np.random.uniform(0.88, 0.96, len(dates)),
            'Processing_Speed': np.random.uniform(1.0, 1.5, len(dates)),
            'Calls_Processed': np.random.randint(100, 500, len(dates))
        }
        
        perf_df = pd.DataFrame(performance_data)
        
        # Accuracy trend
        fig_acc = px.line(perf_df, x='Date', y='Accuracy', 
                         title='Speaker Diarization Accuracy Over Time',
                         color_discrete_sequence=['#667eea'])
        fig_acc.update_layout(height=400)
        st.plotly_chart(fig_acc, use_container_width=True)
        
        # Processing speed vs calls processed
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            fig_speed = px.scatter(perf_df, x='Calls_Processed', y='Processing_Speed',
                                  title='Processing Speed vs Call Volume',
                                  color_discrete_sequence=['#28a745'])
            fig_speed.update_layout(height=350)
            st.plotly_chart(fig_speed, use_container_width=True)
        
        with col_chart2:
            # Speaker distribution
            speaker_dist = pd.DataFrame({
                'Speaker_Count': [1, 2, 3, 4, 5],
                'Call_Percentage': [5, 78, 15, 2, 0.5]
            })
            
            fig_dist = px.bar(speaker_dist, x='Speaker_Count', y='Call_Percentage',
                             title='Speaker Count Distribution',
                             color_discrete_sequence=['#ffc107'])
            fig_dist.update_layout(height=350)
            st.plotly_chart(fig_dist, use_container_width=True)
    
    with tab3:
        # Configuration Section
        st.subheader("⚙️ Model Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎛️ Processing Parameters")
            
            # Processing settings
            embedding_model = st.selectbox(
                "Embedding Model",
                ["wavlm-base-plus", "ecapa-tdnn", "x-vector", "speakerbeam"],
                index=0
            )
            
            clustering_method = st.selectbox(
                "Clustering Method",
                ["Spectral Clustering", "Agglomerative", "K-means", "DBSCAN"],
                index=0
            )
            
            vad_threshold = st.slider("VAD Threshold", 0.1, 0.9, 0.5, 0.1)
            overlap_threshold = st.slider("Overlap Threshold", 0.0, 1.0, 0.5, 0.1)
            
            min_segment_duration = st.number_input("Min Segment Duration (s)", 0.1, 5.0, 1.0, 0.1)
            
        with col2:
            st.markdown("### 🔧 Advanced Settings")
            
            # Advanced settings
            enable_speaker_verification = st.checkbox("Enable Speaker Verification", value=True)
            enable_emotion_detection = st.checkbox("Enable Emotion Detection", value=False)
            enable_language_detection = st.checkbox("Enable Language Detection", value=False)
            
            sample_rate = st.selectbox("Sample Rate", ["8kHz", "16kHz", "44.1kHz", "48kHz"], index=1)
            audio_format = st.selectbox("Output Format", ["WAV", "MP3", "FLAC"], index=0)
            
            confidence_threshold = st.slider("Confidence Threshold", 0.5, 1.0, 0.8, 0.05)
            
            # Save configuration
            if st.button("💾 Save Configuration", type="primary"):
                st.success("Configuration saved successfully!")
                
                # Show saved config
                config = {
                    "embedding_model": embedding_model,
                    "clustering_method": clustering_method,
                    "vad_threshold": vad_threshold,
                    "overlap_threshold": overlap_threshold,
                    "min_segment_duration": min_segment_duration,
                    "confidence_threshold": confidence_threshold
                }
                
                st.json(config)
        
        # Model performance comparison
        st.markdown("### 🏆 Model Performance Comparison")
        
        model_comparison = pd.DataFrame({
            'Model': ['WavLM-Base-Plus', 'ECAPA-TDNN', 'X-Vector', 'SpeakerBeam'],
            'Accuracy': [94.2, 91.8, 89.5, 92.1],
            'Speed (RTF)': [1.2, 0.8, 0.6, 1.0],
            'Memory (GB)': [2.1, 1.5, 0.8, 1.8]
        })
        
        st.dataframe(model_comparison, use_container_width=True)
    
    with tab4:
        # API Usage Section
        st.subheader("📋 API Usage & Integration")
        
        # API examples
        st.markdown("### 🔌 REST API Examples")
        
        api_tab1, api_tab2, api_tab3 = st.tabs(["Python", "cURL", "JavaScript"])
        
        with api_tab1:
            st.markdown("#### Python SDK Example")
            python_code = '''
import requests
import json

# Speaker Diarization API
url = "https://api.contactcenter.ai/v1/speaker-diarization"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Upload audio file
with open("audio_file.wav", "rb") as audio_file:
    files = {"audio": audio_file}
    payload = {
        "min_speakers": 2,
        "max_speakers": 5,
        "quality_mode": "high",
        "enable_vad": True
    }
    
    response = requests.post(url, headers=headers, files=files, data=payload)
    result = response.json()

# Process results
if response.status_code == 200:
    speakers = result["speakers"]
    timeline = result["timeline"]
    transcript = result["transcript"]
    
    print(f"Detected {len(speakers)} speakers")
    for segment in timeline:
        print(f"Speaker {segment['speaker']}: {segment['start']}-{segment['end']}")
        print(f"Text: {segment['text']}")
else:
    print(f"Error: {result['error']}")
'''
            st.code(python_code, language='python')
        
        with api_tab2:
            st.markdown("#### cURL Example")
            curl_code = '''
# Upload and process audio file
curl -X POST https://api.contactcenter.ai/v1/speaker-diarization \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: multipart/form-data" \\
  -F "audio=@audio_file.wav" \\
  -F "min_speakers=2" \\
  -F "max_speakers=5" \\
  -F "quality_mode=high" \\
  -F "enable_vad=true"

# Response
{
  "job_id": "diar_12345",
  "status": "processing",
  "estimated_time": 120
}

# Check job status
curl -X GET https://api.contactcenter.ai/v1/jobs/diar_12345 \\
  -H "Authorization: Bearer YOUR_API_KEY"

# Get results
curl -X GET https://api.contactcenter.ai/v1/jobs/diar_12345/results \\
  -H "Authorization: Bearer YOUR_API_KEY"
'''
            st.code(curl_code, language='bash')
        
        with api_tab3:
            st.markdown("#### JavaScript/Node.js Example")
            js_code = '''
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

async function diarizeAudio(audioFilePath) {
    const form = new FormData();
    form.append('audio', fs.createReadStream(audioFilePath));
    form.append('min_speakers', '2');
    form.append('max_speakers', '5');
    form.append('quality_mode', 'high');
    form.append('enable_vad', 'true');
    
    try {
        const response = await axios.post(
            'https://api.contactcenter.ai/v1/speaker-diarization',
            form,
            {
                headers: {
                    ...form.getHeaders(),
                    'Authorization': 'Bearer YOUR_API_KEY'
                }
            }
        );
        
        const result = response.data;
        console.log('Speakers detected:', result.speakers.length);
        
        // Process timeline
        result.timeline.forEach(segment => {
            console.log(`Speaker ${segment.speaker}: ${segment.text}`);
        });
        
        return result;
        
    } catch (error) {
        console.error('Error:', error.response.data);
    }
}

// Usage
diarizeAudio('./audio_file.wav');
'''
            st.code(js_code, language='javascript')
        
        # Response format
        st.markdown("### 📄 API Response Format")
        
        sample_response = {
            "job_id": "diar_12345",
            "status": "completed",
            "processing_time": 45.2,
            "audio_duration": 180.5,
            "speakers": [
                {"id": "spk_001", "label": "Agent", "total_duration": 85.2},
                {"id": "spk_002", "label": "Customer", "total_duration": 95.3}
            ],
            "timeline": [
                {
                    "speaker": "spk_001",
                    "start": 0.0,
                    "end": 15.2,
                    "confidence": 0.94,
                    "text": "Thank you for calling TechSupport Plus..."
                },
                {
                    "speaker": "spk_002", 
                    "start": 15.2,
                    "end": 45.8,
                    "confidence": 0.91,
                    "text": "Hi, I'm having trouble with my account..."
                }
            ],
            "metadata": {
                "model_version": "v2.1.0",
                "accuracy_score": 0.942,
                "processing_speed": "1.2x"
            }
        }
        
        st.json(sample_response)
        
        # SDK installation
        st.markdown("### 📦 SDK Installation")
        
        col_sdk1, col_sdk2, col_sdk3 = st.columns(3)
        
        with col_sdk1:
            st.markdown("**Python**")
            st.code("pip install contactcenter-ai", language='bash')
        
        with col_sdk2:
            st.markdown("**Node.js**")
            st.code("npm install contactcenter-ai", language='bash')
        
        with col_sdk3:
            st.markdown("**Go**")
            st.code("go get github.com/contactcenter/ai-go", language='bash')
