import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta
import json

def show_call_summarization():
    st.header("📝 Call Summarization")
    
    st.markdown("""
    Our AI-powered call summarization automatically generates concise, actionable summaries 
    of customer interactions, extracting key information and identifying action items.
    """)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Live Demo", "📊 Analytics", "⚙️ Templates", "🔌 API Usage"])
    
    with tab1:
        # Live Demo Section
        st.subheader("🎯 Call Summarization Demo")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📞 Original Conversation")
            
            # Input options
            input_method = st.radio(
                "Choose input method:",
                ["📝 Paste transcript", "📁 Upload file", "🎵 Use sample"]
            )
            
            if input_method == "📝 Paste transcript":
                user_transcript = st.text_area(
                    "Enter conversation transcript:",
                    placeholder="Paste your conversation transcript here...",
                    height=300
                )
            elif input_method == "📁 Upload file":
                uploaded_file = st.file_uploader(
                    "Upload transcript file",
                    type=['txt', 'docx', 'pdf'],
                    help="Supported formats: TXT, DOCX, PDF"
                )
                if uploaded_file:
                    st.success(f"✅ File uploaded: {uploaded_file.name}")
                    user_transcript = "File content would be processed here..."
                else:
                    user_transcript = ""
            else:  # Use sample
                user_transcript = """
Agent: Thank you for calling TechSupport Plus, this is Sarah speaking. How can I assist you today?

Customer: Hi Sarah, I'm John Smith and I'm having a really frustrating issue with my account. My account number is AC-12345-6789, and I haven't been able to access my dashboard for the past three days. Every time I try to log in, it says my password is incorrect, but I know I'm using the right one.

Agent: I'm sorry to hear about this frustration, Mr. Smith. I completely understand how inconvenient this must be for you. Let me pull up your account right away using the number AC-12345-6789. I can see your account here. For security purposes, could you please verify the email address associated with this account?

Customer: Sure, it's john.smith@email.com. I've tried resetting my password multiple times, but I'm not receiving any reset emails. I've checked my spam folder too.

Agent: Thank you for confirming that email address. I can see the issue now - your account was automatically locked after multiple failed login attempts as a security measure. I also notice that our password reset emails were being blocked by your email provider's security settings. Let me unlock your account right now and send you a new temporary password through SMS instead.

Customer: Oh, that makes sense! I did try logging in quite a few times yesterday. My phone number is (555) 123-4567.

Agent: Perfect, I've unlocked your account and sent a temporary password to your phone ending in 4567. You should receive it within the next minute. Once you log in with this temporary password, the system will prompt you to create a new permanent password.

Customer: Great! I just received the text message. Let me try logging in now... Yes! It worked perfectly. Thank you so much for your help, Sarah. You've been incredibly patient and helpful.

Agent: Wonderful! I'm so glad we got that resolved for you, Mr. Smith. To prevent this from happening again, I've also updated your email settings to ensure you receive our communications properly. Is there anything else I can help you with today?

Customer: No, that covers everything. I really appreciate your excellent service. Have a great day!

Agent: Thank you so much, Mr. Smith. You have a great day as well, and please don't hesitate to contact us if you need any further assistance!
                """
            
            st.text_area("Full transcript:", user_transcript, height=400, key="transcript_display")
            
            # Summarization options
            st.markdown("### ⚙️ Summarization Options")
            
            col_opt1, col_opt2 = st.columns(2)
            
            with col_opt1:
                summary_length = st.selectbox(
                    "Summary Length",
                    ["Brief", "Standard", "Detailed"]
                )
                include_sentiment = st.checkbox("Include Sentiment Analysis", value=True)
            
            with col_opt2:
                summary_format = st.selectbox(
                    "Output Format", 
                    ["Structured", "Narrative", "Bullet Points"]
                )
                include_actions = st.checkbox("Extract Action Items", value=True)
            
            # Generate summary button
            if st.button("🚀 Generate Summary", type="primary"):
                if user_transcript.strip():
                    with st.spinner("Analyzing conversation... This may take a moment."):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Simulate processing steps
                        steps = [
                            "Parsing conversation structure...",
                            "Identifying key topics...",
                            "Extracting customer information...",
                            "Analyzing sentiment...",
                            "Identifying action items...",
                            "Generating summary..."
                        ]
                        
                        for i, step in enumerate(steps):
                            status_text.text(step)
                            progress_bar.progress((i + 1) / len(steps))
                            time.sleep(0.5)
                        
                        status_text.text("✅ Summary generated!")
                        st.success("Call summary generated successfully!")
                else:
                    st.error("Please provide a transcript to summarize.")
        
        with col2:
            st.markdown("### 🤖 AI-Generated Summary")
            
            # Sample generated summary
            if 'user_transcript' in locals() and user_transcript.strip():
                summary_content = f"""
**Call Summary Report**
*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*

---

**📋 Basic Information**
- **Customer:** John Smith
- **Account:** AC-12345-6789  
- **Contact:** john.smith@email.com, (555) 123-4567
- **Agent:** Sarah
- **Call Duration:** ~5 minutes
- **Call Type:** Technical Support

---

**🎯 Issue Summary**
Customer unable to access account dashboard for 3 days due to login failures. Password reset emails not being received.

**🔧 Root Cause**
1. Account automatically locked after multiple failed login attempts
2. Email provider blocking password reset emails

**✅ Resolution**
1. Account unlocked by agent
2. Temporary password sent via SMS
3. Email delivery settings updated
4. Customer successfully logged in

---

**😊 Sentiment Analysis**
- **Initial Sentiment:** Frustrated (2/10)
- **Final Sentiment:** Very Satisfied (9/10)
- **Sentiment Trajectory:** ↗️ Improving throughout call
- **Agent Performance:** Excellent (Patient, helpful, professional)

---

**📋 Action Items**
- ✅ Account unlocked and access restored
- ✅ Temporary password sent via SMS  
- ✅ Email delivery settings updated
- 📧 Follow-up email with security tips (automated)

---

**🏷️ Key Topics**
- Account access issues
- Password reset problems
- Email delivery issues
- Security verification
- Customer authentication

---

**📊 Call Metrics**
- **Resolution Time:** 5 minutes
- **First Call Resolution:** ✅ Yes
- **Customer Satisfaction:** 9/10
- **Issue Complexity:** Medium
- **Escalation Required:** ❌ No

---

**💡 Insights & Recommendations**
1. **Process Improvement:** Consider implementing SMS as primary password reset method
2. **Proactive Monitoring:** Set up alerts for email delivery failures
3. **Customer Education:** Provide guidance on email security settings
4. **Agent Recognition:** Sarah demonstrated excellent customer service skills
                """
                
                st.markdown(summary_content)
                
                # Export options
                st.markdown("### 📤 Export Options")
                col_exp1, col_exp2, col_exp3 = st.columns(3)
                
                with col_exp1:
                    if st.button("📄 Export PDF"):
                        st.success("Summary exported as PDF!")
                
                with col_exp2:
                    if st.button("📊 Export Excel"):
                        st.success("Summary exported as Excel!")
                
                with col_exp3:
                    if st.button("📋 Copy to Clipboard"):
                        st.success("Summary copied to clipboard!")
            
            else:
                st.info("💡 Generate a summary using the conversation on the left")
                
                # Show sample summary structure
                st.markdown("""
                **Summary will include:**
                - 📋 Basic call information
                - 🎯 Issue description and resolution
                - 😊 Sentiment analysis
                - ✅ Action items and follow-ups
                - 🏷️ Key topics and tags
                - 📊 Performance metrics
                - 💡 Insights and recommendations
                """)
        
        # Summary quality metrics
        if 'user_transcript' in locals() and user_transcript.strip():
            st.markdown("### 📊 Summary Quality Metrics")
            
            col_q1, col_q2, col_q3, col_q4 = st.columns(4)
            
            with col_q1:
                st.metric("Accuracy Score", "94%", "+2%")
            with col_q2:
                st.metric("Completeness", "91%", "+1%")
            with col_q3:
                st.metric("Relevance", "96%", "stable")
            with col_q4:
                st.metric("Conciseness", "89%", "+3%")
    
    with tab2:
        # Analytics Section
        st.subheader("📊 Summarization Analytics")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Summaries Generated", "15,247", "+12%")
        with col2:
            st.metric("Avg Processing Time", "2.3s", "-0.4s")
        with col3:
            st.metric("Quality Score", "93.2%", "+1.8%")
        with col4:
            st.metric("User Satisfaction", "4.7/5", "+0.2")
        
        # Performance trends
        st.markdown("### 📈 Performance Trends")
        
        # Generate sample data
        dates = pd.date_range(start='2024-01-01', end='2024-07-12', freq='D')
        analytics_data = {
            'Date': dates,
            'Summaries_Generated': np.random.randint(200, 800, len(dates)),
            'Quality_Score': np.random.uniform(0.85, 0.98, len(dates)),
            'Processing_Time': np.random.uniform(1.5, 4.0, len(dates)),
            'User_Rating': np.random.uniform(4.0, 5.0, len(dates))
        }
        
        analytics_df = pd.DataFrame(analytics_data)
        
        # Quality score trend
        fig_quality = px.line(analytics_df, x='Date', y='Quality_Score', 
                             title='Summary Quality Score Over Time',
                             color_discrete_sequence=['#667eea'])
        fig_quality.update_layout(height=400)
        st.plotly_chart(fig_quality, use_container_width=True)
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Processing time distribution
            fig_time = px.histogram(analytics_df, x='Processing_Time', 
                                   title='Processing Time Distribution',
                                   color_discrete_sequence=['#28a745'])
            fig_time.update_layout(height=350)
            st.plotly_chart(fig_time, use_container_width=True)
        
        with col_chart2:
            # Summary length distribution
            length_data = pd.DataFrame({
                'Length_Category': ['Brief', 'Standard', 'Detailed'],
                'Percentage': [25, 60, 15]
            })
            
            fig_length = px.pie(length_data, values='Percentage', names='Length_Category',
                               title='Summary Length Preferences')
            fig_length.update_layout(height=350)
            st.plotly_chart(fig_length, use_container_width=True)
        
        # Topic analysis
        st.markdown("### 🏷️ Topic Analysis")
        
        topic_data = pd.DataFrame({
            'Topic': ['Account Issues', 'Technical Support', 'Billing Inquiries', 
                     'Product Information', 'Complaints', 'General Inquiries'],
            'Frequency': [2847, 2156, 1923, 1654, 892, 1234],
            'Avg_Quality': [94.2, 91.8, 96.1, 89.5, 87.3, 92.4]
        })
        
        fig_topic = px.bar(topic_data, x='Topic', y='Frequency', 
                          color='Avg_Quality', title='Topics by Frequency and Quality',
                          color_continuous_scale='RdYlGn')
        fig_topic.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_topic, use_container_width=True)
    
    with tab3:
        # Templates Section
        st.subheader("⚙️ Summary Templates & Configuration")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📋 Template Library")
            
            # Template selection
            template_type = st.selectbox(
                "Choose Template Type",
                ["Customer Support", "Sales Call", "Technical Issue", "Billing Inquiry", "Complaint", "Custom"]
            )
            
            # Template configuration
            if template_type == "Customer Support":
                template_config = {
                    "sections": ["Customer Info", "Issue Summary", "Resolution", "Action Items", "Sentiment"],
                    "include_metrics": True,
                    "sentiment_analysis": True,
                    "action_extraction": True
                }
            elif template_type == "Sales Call":
                template_config = {
                    "sections": ["Lead Info", "Products Discussed", "Customer Needs", "Next Steps", "Follow-up"],
                    "include_metrics": True,
                    "sentiment_analysis": True,
                    "deal_scoring": True
                }
            else:
                template_config = {
                    "sections": ["Basic Info", "Main Topics", "Key Points", "Actions"],
                    "include_metrics": False,
                    "sentiment_analysis": True,
                    "action_extraction": True
                }
            
            st.json(template_config)
            
            # Custom template builder
            if template_type == "Custom":
                st.markdown("### 🛠️ Custom Template Builder")
                
                custom_sections = st.multiselect(
                    "Select sections to include:",
                    ["Customer Info", "Issue Summary", "Resolution", "Action Items", 
                     "Sentiment", "Key Topics", "Metrics", "Recommendations", "Follow-up"],
                    default=["Customer Info", "Issue Summary", "Action Items"]
                )
                
                custom_format = st.selectbox("Output Format", ["Structured", "Narrative", "Bullet Points"])
                include_timestamps = st.checkbox("Include Timestamps", value=False)
                include_confidence = st.checkbox("Include Confidence Scores", value=True)
                
                if st.button("💾 Save Custom Template"):
                    st.success("Custom template saved successfully!")
        
        with col2:
            st.markdown("### 🎛️ Summarization Settings")
            
            # Model settings
            model_type = st.selectbox(
                "Summarization Model",
                ["BART-Large", "T5-Base", "Pegasus", "GPT-3.5"],
                index=0
            )
            
            max_length = st.slider("Maximum Summary Length (words)", 50, 500, 200)
            min_length = st.slider("Minimum Summary Length (words)", 20, 200, 50)
            
            # Advanced settings
            st.markdown("#### Advanced Settings")
            
            extractiveness = st.slider("Extractiveness vs Abstractiveness", 0.0, 1.0, 0.5, 0.1,
                                     help="0 = More abstractive, 1 = More extractive")
            
            focus_keywords = st.text_input(
                "Focus Keywords (comma-separated)",
                placeholder="account, password, billing, technical",
                help="Keywords to prioritize in summary"
            )
            
            language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian"])
            
            # Quality thresholds
            st.markdown("#### Quality Thresholds")
            
            min_quality_score = st.slider("Minimum Quality Score", 0.5, 1.0, 0.8, 0.05)
            confidence_threshold = st.slider("Confidence Threshold", 0.5, 1.0, 0.75, 0.05)
            
            if st.button("🔄 Apply Settings", type="primary"):
                st.success("Settings applied successfully!")
        
        # Template preview
        st.markdown("### 👁️ Template Preview")
        
        if template_type == "Customer Support":
            preview_template = """
**Customer Support Call Summary**

**📋 Customer Information**
- Name: [Customer Name]
- Account: [Account Number]
- Contact: [Email/Phone]

**🎯 Issue Summary**
[Brief description of the customer's issue]

**🔧 Resolution**
[Steps taken to resolve the issue]

**✅ Action Items**
- [Action item 1]
- [Action item 2]

**😊 Sentiment Analysis**
- Initial: [Sentiment]
- Final: [Sentiment]
- Overall Experience: [Rating]

**📊 Metrics**
- Call Duration: [Duration]
- Resolution: [First Call Resolution]
- Satisfaction: [Score]
            """
        else:
            preview_template = """
**Call Summary**

**📋 Basic Information**
[Customer/Contact details]

**🎯 Main Topics**
[Key discussion points]

**✅ Action Items**
[Next steps and follow-ups]

**📊 Summary**
[Overall call summary]
            """
        
        st.code(preview_template, language='markdown')
    
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

# Call Summarization API
url = "https://api.contactcenter.ai/v1/call-summarization"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Prepare transcript data
payload = {
    "transcript": "Agent: Thank you for calling...",
    "template": "customer_support",
    "options": {
        "length": "standard",
        "format": "structured",
        "include_sentiment": True,
        "include_actions": True,
        "language": "en"
    }
}

# Generate summary
response = requests.post(url, headers=headers, json=payload)
result = response.json()

if response.status_code == 200:
    summary = result["summary"]
    quality_score = result["quality_score"]
    action_items = result["action_items"]
    sentiment = result["sentiment_analysis"]
    
    print(f"Summary Quality: {quality_score}")
    print(f"Summary: {summary}")
    print(f"Action Items: {action_items}")
    print(f"Sentiment: {sentiment}")
else:
    print(f"Error: {result['error']}")

# Batch processing example
batch_payload = {
    "transcripts": [
        {"id": "call_001", "transcript": "..."},
        {"id": "call_002", "transcript": "..."}
    ],
    "template": "customer_support"
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
# Single call summarization
curl -X POST https://api.contactcenter.ai/v1/call-summarization \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "transcript": "Agent: Thank you for calling TechSupport Plus...",
    "template": "customer_support",
    "options": {
      "length": "standard",
      "format": "structured",
      "include_sentiment": true,
      "include_actions": true
    }
  }'

# Response
{
  "job_id": "sum_12345",
  "status": "completed",
  "summary": "Customer John Smith called regarding...",
  "quality_score": 0.94,
  "processing_time": 2.3,
  "action_items": [
    "Account unlocked",
    "Follow-up email sent"
  ],
  "sentiment_analysis": {
    "initial": "frustrated",
    "final": "satisfied",
    "overall_score": 0.85
  }
}

# Batch processing
curl -X POST https://api.contactcenter.ai/v1/call-summarization/batch \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "transcripts": [
      {"id": "call_001", "transcript": "..."},
      {"id": "call_002", "transcript": "..."}
    ],
    "template": "customer_support"
  }'
'''
            st.code(curl_code, language='bash')
        
        with api_tab3:
            st.markdown("#### JavaScript/Node.js Example")
            js_code = '''
const axios = require('axios');

class CallSummarizer {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = 'https://api.contactcenter.ai/v1';
    }
    
    async summarizeCall(transcript, options = {}) {
        const payload = {
            transcript: transcript,
            template: options.template || 'customer_support',
            options: {
                length: options.length || 'standard',
                format: options.format || 'structured',
                include_sentiment: options.includeSentiment || true,
                include_actions: options.includeActions || true,
                language: options.language || 'en'
            }
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/call-summarization`,
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
            console.error('Summarization error:', error.response.data);
            throw error;
        }
    }
    
    async batchSummarize(transcripts) {
        const payload = {
            transcripts: transcripts,
            template: 'customer_support'
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/call-summarization/batch`,
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
            console.error('Batch summarization error:', error.response.data);
            throw error;
        }
    }
}

// Usage example
const summarizer = new CallSummarizer('YOUR_API_KEY');

async function processCalls() {
    const transcript = "Agent: Thank you for calling...";
    
    try {
        const result = await summarizer.summarizeCall(transcript, {
            template: 'customer_support',
            length: 'standard',
            includeSentiment: true
        });
        
        console.log('Summary:', result.summary);
        console.log('Quality Score:', result.quality_score);
        console.log('Action Items:', result.action_items);
        
    } catch (error) {
        console.error('Error processing call:', error);
    }
}

processCalls();
'''
            st.code(js_code, language='javascript')
        
        # Response format
        st.markdown("### 📄 API Response Format")
        
        sample_response = {
            "job_id": "sum_12345",
            "status": "completed",
            "processing_time": 2.3,
            "summary": {
                "customer_info": {
                    "name": "John Smith",
                    "account": "AC-12345-6789",
                    "contact": "john.smith@email.com"
                },
                "issue_summary": "Customer unable to access account dashboard for 3 days",
                "resolution": "Account unlocked, temporary password sent via SMS",
                "action_items": [
                    "Account unlocked and access restored",
                    "Email delivery settings updated",
                    "Follow-up email with security tips scheduled"
                ]
            },
            "sentiment_analysis": {
                "initial_sentiment": "frustrated",
                "final_sentiment": "satisfied", 
                "sentiment_score": 0.85,
                "sentiment_trajectory": "improving"
            },
            "quality_metrics": {
                "accuracy": 0.94,
                "completeness": 0.91,
                "relevance": 0.96,
                "conciseness": 0.89
            },
            "metadata": {
                "model_version": "v2.1.0",
                "template_used": "customer_support",
                "language": "en",
                "word_count": 187
            }
        }
        
        st.json(sample_response)
        
        # Rate limits and pricing
        st.markdown("### 📊 API Limits & Pricing")
        
        col_limit1, col_limit2, col_limit3 = st.columns(3)
        
        with col_limit1:
            st.markdown("""
            **Rate Limits**
            - Free Tier: 100 calls/day
            - Basic: 1,000 calls/day  
            - Pro: 10,000 calls/day
            - Enterprise: Unlimited
            """)
        
        with col_limit2:
            st.markdown("""
            **Pricing**
            - Free: $0/month
            - Basic: $29/month
            - Pro: $99/month
            - Enterprise: Custom
            """)
        
        with col_limit3:
            st.markdown("""
            **Features**
            - Real-time processing
            - Batch processing
            - Custom templates
            - Multi-language support
            """)
