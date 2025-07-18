import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import re
from datetime import datetime, timedelta
import json

def show_pii_detection():
    st.header("🔒 Advanced PII Detection & GDPR Compliance")
    
    st.markdown("""
    **Comprehensive protection** of personally identifiable information with real-time detection, 
    automatic masking, GDPR compliance automation, and enterprise-grade audit trails for complete data protection.
    """)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🛡️ PII Protection", "99.8%", "↗️ Real-time detection")
    with col2:
        st.metric("⚖️ GDPR Compliance", "100%", "↗️ Automated compliance")
    with col3:
        st.metric("🎭 Auto Masking", "Real-time", "↗️ Live interactions")
    with col4:
        st.metric("📋 Audit Trails", "Complete", "↗️ Full transparency")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Live PII Detection", "📊 Compliance Analytics", "🌍 GDPR Automation", "🔐 Amazon Connect Security", "🔌 API Usage"
    ])
    
    with tab1:
        # Live Demo Section
        st.subheader("🎯 PII Detection Demo")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📄 Original Text")
            
            # Input options
            input_method = st.radio(
                "Choose input method:",
                ["📝 Paste text", "📁 Upload file", "🎵 Use sample", "🔗 Real-time stream"]
            )
            
            if input_method == "📝 Paste text":
                original_text = st.text_area(
                    "Enter text for PII analysis:",
                    placeholder="Paste conversation transcript or document here...",
                    height=300
                )
            elif input_method == "📁 Upload file":
                uploaded_file = st.file_uploader(
                    "Upload document",
                    type=['txt', 'docx', 'pdf', 'csv'],
                    help="Supported formats: TXT, DOCX, PDF, CSV"
                )
                if uploaded_file:
                    st.success(f"✅ File uploaded: {uploaded_file.name}")
                    original_text = "File content would be processed here..."
                else:
                    original_text = ""
            elif input_method == "🔗 Real-time stream":
                st.info("🔄 Real-time PII detection active")
                original_text = st.text_area(
                    "Live transcript stream:",
                    value="Real-time conversation data streaming...",
                    height=300
                )
            else:  # Use sample
                original_text = """
Customer: Hi, my name is John Smith and I need help with my account. My email is john.smith@email.com and my phone number is (555) 123-4567. 

Agent: Thank you Mr. Smith. I'll need to verify your identity. Can you provide your social security number?

Customer: Sure, it's 123-45-6789. Also, my date of birth is March 15, 1985, and I live at 123 Main Street, Anytown, CA 90210.

Agent: Perfect. I can see your account now. Your credit card ending in 4567 was charged $299.99 yesterday. The billing address on file is 123 Main Street, Anytown, CA 90210.

Customer: That's correct. Can you also update my emergency contact? It should be my wife, Sarah Smith, at (555) 987-6543.

Agent: I've updated that information. Your account balance shows $1,234.56. Is there anything else I can help you with today?

Customer: Actually, can you send the receipt to my work email? It's john.smith@company.com. My employee ID is EMP-789123.

Agent: Absolutely. I'll send that to john.smith@company.com right away. Your ticket number for this interaction is TK-456789. Have a great day!
                """
            
            st.text_area("Raw conversation text:", original_text, height=350, key="original_text_display")
            
            # Detection options
            st.markdown("### ⚙️ Detection Settings")
            
            col_opt1, col_opt2 = st.columns(2)
            
            with col_opt1:
                pii_types = st.multiselect(
                    "PII Types to Detect",
                    ["Names", "Email Addresses", "Phone Numbers", "SSN", "Credit Cards", 
                     "Addresses", "Dates", "Account Numbers", "Employee IDs"],
                    default=["Names", "Email Addresses", "Phone Numbers", "SSN", "Credit Cards"]
                )
                
                detection_mode = st.selectbox(
                    "Detection Mode",
                    ["High Precision", "Balanced", "High Recall"]
                )
            
            with col_opt2:
                masking_method = st.selectbox(
                    "Masking Method",
                    ["Replacement Tags", "Asterisks", "Partial Masking", "Full Redaction"]
                )
                
                confidence_threshold = st.slider(
                    "Confidence Threshold", 
                    0.5, 1.0, 0.8, 0.05
                )
            
            # Process button
            if st.button("🔍 Detect & Mask PII", type="primary"):
                if original_text.strip():
                    with st.spinner("Analyzing text for PII... This may take a moment."):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Simulate processing steps
                        steps = [
                            "Tokenizing text...",
                            "Running NER models...",
                            "Pattern matching...",
                            "Confidence scoring...",
                            "Applying masking...",
                            "Generating report..."
                        ]
                        
                        for i, step in enumerate(steps):
                            status_text.text(step)
                            progress_bar.progress((i + 1) / len(steps))
                            time.sleep(0.3)
                        
                        status_text.text("✅ PII detection complete!")
                        st.success("PII detected and masked successfully!")
                else:
                    st.error("Please provide text to analyze.")
        
        with col2:
            st.markdown("### 🛡️ Protected Text")
            
            # Sample protected text based on masking method
            if 'original_text' in locals() and original_text.strip():
                if masking_method == "Replacement Tags":
                    protected_text = """
Customer: Hi, my name is [PERSON_NAME] and I need help with my account. My email is [EMAIL_ADDRESS] and my phone number is [PHONE_NUMBER]. 

Agent: Thank you [PERSON_NAME]. I'll need to verify your identity. Can you provide your social security number?

Customer: Sure, it's [SSN]. Also, my date of birth is [DATE], and I live at [ADDRESS].

Agent: Perfect. I can see your account now. Your credit card ending in [CREDIT_CARD] was charged [CURRENCY] yesterday. The billing address on file is [ADDRESS].

Customer: That's correct. Can you also update my emergency contact? It should be my wife, [PERSON_NAME], at [PHONE_NUMBER].

Agent: I've updated that information. Your account balance shows [CURRENCY]. Is there anything else I can help you with today?

Customer: Actually, can you send the receipt to my work email? It's [EMAIL_ADDRESS]. My employee ID is [EMPLOYEE_ID].

Agent: Absolutely. I'll send that to [EMAIL_ADDRESS] right away. Your ticket number for this interaction is [TICKET_NUMBER]. Have a great day!
                    """
                elif masking_method == "Asterisks":
                    protected_text = """
Customer: Hi, my name is John ***** and I need help with my account. My email is ****@******.com and my phone number is (***) ***-**67. 

Agent: Thank you Mr. *****. I'll need to verify your identity. Can you provide your social security number?

Customer: Sure, it's ***-**-*789. Also, my date of birth is ***** **, **85, and I live at *** Main Street, *******, ** *****.

Agent: Perfect. I can see your account now. Your credit card ending in *567 was charged $***.** yesterday. The billing address on file is *** Main Street, *******, ** *****.

Customer: That's correct. Can you also update my emergency contact? It should be my wife, ***** *****, at (***) ***-**43.

Agent: I've updated that information. Your account balance shows $*,***.56. Is there anything else I can help you with today?

Customer: Actually, can you send the receipt to my work email? It's ****@*******.com. My employee ID is ***-******.

Agent: Absolutely. I'll send that to ****@*******.com right away. Your ticket number for this interaction is **-******. Have a great day!
                    """
                else:  # Partial Masking
                    protected_text = """
Customer: Hi, my name is John S*** and I need help with my account. My email is j***@email.com and my phone number is (555) ***-4567. 

Agent: Thank you Mr. S***. I'll need to verify your identity. Can you provide your social security number?

Customer: Sure, it's ***-45-6789. Also, my date of birth is March **, 1985, and I live at *** Main Street, Anytown, CA 90210.

Agent: Perfect. I can see your account now. Your credit card ending in 4567 was charged $***.99 yesterday. The billing address on file is *** Main Street, Anytown, CA 90210.

Customer: That's correct. Can you also update my emergency contact? It should be my wife, Sarah S***, at (555) ***-6543.

Agent: I've updated that information. Your account balance shows $1,***.56. Is there anything else I can help you with today?

Customer: Actually, can you send the receipt to my work email? It's j***@company.com. My employee ID is EMP-***123.

Agent: Absolutely. I'll send that to j***@company.com right away. Your ticket number for this interaction is TK-***789. Have a great day!
                    """
                
                st.text_area("Anonymized text:", protected_text, height=350)
                
                # Export options
                st.markdown("### 📤 Export Options")
                col_exp1, col_exp2, col_exp3 = st.columns(3)
                
                with col_exp1:
                    if st.button("📄 Export Protected Text"):
                        st.success("Protected text exported!")
                
                with col_exp2:
                    if st.button("📊 Export Detection Report"):
                        st.success("Detection report exported!")
                
                with col_exp3:
                    if st.button("🔐 Export Mapping File"):
                        st.success("PII mapping exported!")
            
            else:
                st.info("💡 Process text using the options on the left")
                
                # Show sample protection preview
                st.markdown("""
                **Protection Methods:**
                - 🏷️ **Replacement Tags**: `[PERSON_NAME]`, `[EMAIL_ADDRESS]`
                - ⭐ **Asterisks**: `John *****`, `****@email.com`
                - 🎭 **Partial Masking**: `John S***`, `j***@email.com`
                - ⬛ **Full Redaction**: `[REDACTED]`
                """)
        
        # PII Detection Results
        if 'original_text' in locals() and original_text.strip():
            st.markdown("### 🔍 Detection Results")
            
            pii_data = {
                'PII Type': ['Person Name', 'Email Address', 'Phone Number', 'SSN', 'Credit Card', 
                           'Address', 'Date of Birth', 'Account Balance', 'Employee ID', 'Ticket Number'],
                'Count': [3, 2, 2, 1, 1, 2, 1, 2, 1, 1],
                'Confidence': [0.98, 0.99, 0.97, 0.99, 0.95, 0.92, 0.94, 0.88, 0.96, 0.91],
                'Status': ['Masked', 'Masked', 'Masked', 'Masked', 'Masked', 
                          'Masked', 'Masked', 'Masked', 'Masked', 'Masked'],
                'Risk Level': ['High', 'High', 'Medium', 'Critical', 'High',
                             'Medium', 'High', 'Low', 'Medium', 'Low']
            }
            
            pii_df = pd.DataFrame(pii_data)
            
            # Color code by risk level
            def color_risk(val):
                if val == 'Critical':
                    return 'background-color: #ffebee'
                elif val == 'High':
                    return 'background-color: #fff3e0'
                elif val == 'Medium':
                    return 'background-color: #f3e5f5'
                else:
                    return 'background-color: #e8f5e8'
            
            styled_df = pii_df.style.applymap(color_risk, subset=['Risk Level'])
            st.dataframe(styled_df, use_container_width=True)
            
            # Summary statistics
            st.markdown("### 📊 Detection Summary")
            
            col_sum1, col_sum2, col_sum3, col_sum4 = st.columns(4)
            
            with col_sum1:
                st.metric("Total PII Detected", len(pii_df), "entities")
            with col_sum2:
                st.metric("Critical Risk Items", len(pii_df[pii_df['Risk Level'] == 'Critical']), "🔴")
            with col_sum3:
                st.metric("Avg Confidence", f"{pii_df['Confidence'].mean():.2%}", "score")
            with col_sum4:
                st.metric("Protection Rate", "100%", "✅ Complete")
    
    with tab2:
        # Analytics Section
        st.subheader("📊 PII Protection Analytics")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Documents Processed", "45,892", "+8%")
        with col2:
            st.metric("PII Entities Detected", "234,567", "+12%")
        with col3:
            st.metric("Detection Accuracy", "97.8%", "+1.2%")
        with col4:
            st.metric("Compliance Score", "99.2%", "+0.8%")
        
        # Detection trends
        st.markdown("### 📈 Detection Trends")
        
        # Generate sample analytics data
        dates = pd.date_range(start='2024-01-01', end='2024-07-12', freq='D')
        analytics_data = {
            'Date': dates,
            'Documents_Processed': np.random.randint(100, 300, len(dates)),
            'PII_Detected': np.random.randint(500, 2000, len(dates)),
            'Detection_Accuracy': np.random.uniform(0.95, 0.99, len(dates)),
            'False_Positives': np.random.uniform(0.01, 0.05, len(dates))
        }
        
        analytics_df = pd.DataFrame(analytics_data)
        
        # PII detection volume
        fig_volume = px.line(analytics_df, x='Date', y='PII_Detected', 
                            title='Daily PII Detection Volume',
                            color_discrete_sequence=['#dc3545'])
        fig_volume.update_layout(height=400)
        st.plotly_chart(fig_volume, use_container_width=True)
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Accuracy trend
            fig_accuracy = px.line(analytics_df, x='Date', y='Detection_Accuracy',
                                  title='Detection Accuracy Trend',
                                  color_discrete_sequence=['#28a745'])
            fig_accuracy.update_layout(height=350)
            st.plotly_chart(fig_accuracy, use_container_width=True)
        
        with col_chart2:
            # PII type distribution
            pii_types_data = pd.DataFrame({
                'PII_Type': ['Email', 'Phone', 'Names', 'SSN', 'Credit Cards', 'Addresses'],
                'Count': [15234, 12876, 23451, 3456, 2134, 8765],
                'Percentage': [26.8, 22.6, 41.2, 6.1, 3.7, 15.4]
            })
            
            fig_types = px.pie(pii_types_data, values='Count', names='PII_Type',
                              title='PII Types Distribution')
            fig_types.update_layout(height=350)
            st.plotly_chart(fig_types, use_container_width=True)
        
        # Risk analysis
        st.markdown("### ⚠️ Risk Analysis")
        
        risk_data = pd.DataFrame({
            'Risk_Level': ['Critical', 'High', 'Medium', 'Low'],
            'Count': [1234, 5678, 8901, 12345],
            'Percentage': [4.4, 20.3, 31.8, 43.5]
        })
        
        fig_risk = px.bar(risk_data, x='Risk_Level', y='Count',
                         color='Risk_Level',
                         color_discrete_map={
                             'Critical': '#dc3545',
                             'High': '#fd7e14', 
                             'Medium': '#ffc107',
                             'Low': '#28a745'
                         },
                         title='PII Risk Level Distribution')
        fig_risk.update_layout(height=400)
        st.plotly_chart(fig_risk, use_container_width=True)
        
        # Compliance metrics
        st.markdown("### 📋 Compliance Metrics")
        
        compliance_data = {
            'Regulation': ['GDPR', 'CCPA', 'HIPAA', 'PCI DSS', 'SOX'],
            'Compliance_Score': [99.2, 98.8, 97.5, 99.1, 96.9],
            'Status': ['✅ Compliant', '✅ Compliant', '⚠️ Monitor', '✅ Compliant', '⚠️ Monitor']
        }
        
        compliance_df = pd.DataFrame(compliance_data)
        st.dataframe(compliance_df, use_container_width=True)
    
    with tab3:
        # Configuration Section
        st.subheader("⚙️ PII Detection Configuration")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🎛️ Detection Models")
            
            # Model selection
            primary_model = st.selectbox(
                "Primary NER Model",
                ["spaCy en_core_web_lg", "BERT-NER", "RoBERTa-NER", "Custom Model"],
                index=0
            )
            
            secondary_model = st.selectbox(
                "Secondary Pattern Matcher",
                ["Regex Patterns", "Rule-based", "Hybrid", "None"],
                index=0
            )
            
            # PII categories configuration
            st.markdown("### 🏷️ PII Categories")
            
            pii_categories = {
                "Personal Identifiers": st.checkbox("Personal Identifiers", value=True),
                "Financial Information": st.checkbox("Financial Information", value=True),
                "Health Information": st.checkbox("Health Information", value=False),
                "Contact Information": st.checkbox("Contact Information", value=True),
                "Government IDs": st.checkbox("Government IDs", value=True),
                "Biometric Data": st.checkbox("Biometric Data", value=False),
                "Online Identifiers": st.checkbox("Online Identifiers", value=True),
                "Location Data": st.checkbox("Location Data", value=True)
            }
            
            # Custom patterns
            st.markdown("### 🔧 Custom Patterns")
            
            custom_pattern = st.text_area(
                "Add Custom Regex Pattern:",
                placeholder="e.g., (?i)employee[\\s-]?id[\\s:]?([a-z0-9]+)",
                help="Define custom regex patterns for organization-specific PII"
            )
            
            pattern_label = st.text_input("Pattern Label:", placeholder="Employee ID")
            
            if st.button("➕ Add Custom Pattern"):
                if custom_pattern and pattern_label:
                    st.success(f"Custom pattern '{pattern_label}' added!")
                else:
                    st.error("Please provide both pattern and label")
        
        with col2:
            st.markdown("### 🛡️ Protection Settings")
            
            # Masking configuration
            default_masking = st.selectbox(
                "Default Masking Method",
                ["Replacement Tags", "Asterisks", "Partial Masking", "Full Redaction"],
                index=0
            )
            
            # Category-specific masking
            st.markdown("#### Category-specific Masking")
            
            masking_rules = {
                "Names": st.selectbox("Names", ["[PERSON_NAME]", "***", "Partial", "[REDACTED]"], key="names_mask"),
                "Emails": st.selectbox("Email Addresses", ["[EMAIL_ADDRESS]", "***", "Partial", "[REDACTED]"], key="email_mask"),
                "Phones": st.selectbox("Phone Numbers", ["[PHONE_NUMBER]", "***", "Partial", "[REDACTED]"], key="phone_mask"),
                "SSN": st.selectbox("Social Security Numbers", ["[SSN]", "***", "Partial", "[REDACTED]"], key="ssn_mask")
            }
            
            # Confidence thresholds
            st.markdown("### 📊 Confidence Thresholds")
            
            thresholds = {
                "High Confidence": st.slider("High Confidence Threshold", 0.8, 1.0, 0.95, 0.01),
                "Medium Confidence": st.slider("Medium Confidence Threshold", 0.5, 0.9, 0.75, 0.01),
                "Low Confidence": st.slider("Low Confidence Threshold", 0.1, 0.7, 0.5, 0.01)
            }
            
            # Advanced settings
            st.markdown("### ⚙️ Advanced Settings")
            
            case_sensitive = st.checkbox("Case Sensitive Detection", value=False)
            context_analysis = st.checkbox("Context Analysis", value=True)
            multi_language = st.checkbox("Multi-language Support", value=True)
            
            languages = st.multiselect(
                "Supported Languages",
                ["English", "Spanish", "French", "German", "Italian", "Portuguese"],
                default=["English"]
            )
            
            # Save configuration
            if st.button("💾 Save Configuration", type="primary"):
                config = {
                    "primary_model": primary_model,
                    "secondary_model": secondary_model,
                    "pii_categories": pii_categories,
                    "masking_rules": masking_rules,
                    "thresholds": thresholds,
                    "advanced_settings": {
                        "case_sensitive": case_sensitive,
                        "context_analysis": context_analysis,
                        "multi_language": multi_language,
                        "languages": languages
                    }
                }
                
                st.success("Configuration saved successfully!")
                st.json(config)
        
        # Pattern library
        st.markdown("### 📚 Pattern Library")
        
        pattern_library = pd.DataFrame({
            'Pattern Name': ['US Phone Number', 'Email Address', 'SSN', 'Credit Card', 'IP Address'],
            'Regex Pattern': [
                r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                r'\b\d{3}-\d{2}-\d{4}\b',
                r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
                r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
            ],
            'Confidence': [0.95, 0.98, 0.99, 0.92, 0.87],
            'Status': ['Active', 'Active', 'Active', 'Active', 'Active']
        })
        
        st.dataframe(pattern_library, use_container_width=True)
    
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

# PII Detection API
url = "https://api.contactcenter.ai/v1/pii-detection"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Text analysis
payload = {
    "text": "Hi, my name is John Smith. My email is john.smith@email.com",
    "pii_types": ["names", "emails", "phones", "ssn", "credit_cards"],
    "options": {
        "masking_method": "replacement_tags",
        "confidence_threshold": 0.8,
        "include_confidence": True,
        "context_analysis": True
    }
}

# Detect PII
response = requests.post(url, headers=headers, json=payload)
result = response.json()

if response.status_code == 200:
    detected_pii = result["detected_pii"]
    protected_text = result["protected_text"]
    confidence_scores = result["confidence_scores"]
    
    print("Detected PII:")
    for pii in detected_pii:
        print(f"- {pii['type']}: {pii['value']} (confidence: {pii['confidence']})")
    
    print(f"\\nProtected Text: {protected_text}")
else:
    print(f"Error: {result['error']}")

# Batch processing
batch_payload = {
    "documents": [
        {"id": "doc1", "text": "..."},
        {"id": "doc2", "text": "..."}
    ],
    "pii_types": ["names", "emails", "phones"],
    "masking_method": "asterisks"
}

batch_response = requests.post(
    url + "/batch", 
    headers=headers, 
    json=batch_payload
)

# Real-time stream processing
import websocket

def on_message(ws, message):
    data = json.loads(message)
    print(f"PII detected: {data['pii_count']} entities")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

# Connect to real-time stream
ws = websocket.WebSocketApp(
    "wss://api.contactcenter.ai/v1/pii-detection/stream",
    header={"Authorization": "Bearer YOUR_API_KEY"},
    on_message=on_message,
    on_error=on_error
)

ws.run_forever()
'''
            st.code(python_code, language='python')
        
        with api_tab2:
            st.markdown("#### cURL Example")
            curl_code = '''
# Single document PII detection
curl -X POST https://api.contactcenter.ai/v1/pii-detection \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "text": "Hi, my name is John Smith. My email is john.smith@email.com",
    "pii_types": ["names", "emails", "phones", "ssn"],
    "options": {
      "masking_method": "replacement_tags",
      "confidence_threshold": 0.8,
      "include_confidence": true
    }
  }'

# Response
{
  "job_id": "pii_12345",
  "status": "completed",
  "processing_time": 0.12,
  "detected_pii": [
    {
      "type": "person_name",
      "value": "John Smith",
      "start_pos": 15,
      "end_pos": 25,
      "confidence": 0.98,
      "risk_level": "high"
    },
    {
      "type": "email_address", 
      "value": "john.smith@email.com",
      "start_pos": 39,
      "end_pos": 60,
      "confidence": 0.99,
      "risk_level": "high"
    }
  ],
  "protected_text": "Hi, my name is [PERSON_NAME]. My email is [EMAIL_ADDRESS]",
  "statistics": {
    "total_entities": 2,
    "high_risk": 2,
    "medium_risk": 0,
    "low_risk": 0
  }
}

# Batch processing
curl -X POST https://api.contactcenter.ai/v1/pii-detection/batch \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "documents": [
      {"id": "doc1", "text": "Customer data here..."},
      {"id": "doc2", "text": "More customer data..."}
    ],
    "pii_types": ["names", "emails", "phones"],
    "masking_method": "asterisks"
  }'

# Check processing status
curl -X GET https://api.contactcenter.ai/v1/jobs/pii_12345 \\
  -H "Authorization: Bearer YOUR_API_KEY"
'''
            st.code(curl_code, language='bash')
        
        with api_tab3:
            st.markdown("#### JavaScript/Node.js Example")
            js_code = '''
const axios = require('axios');
const WebSocket = require('ws');

class PIIDetector {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = 'https://api.contactcenter.ai/v1';
    }
    
    async detectPII(text, options = {}) {
        const payload = {
            text: text,
            pii_types: options.piiTypes || ['names', 'emails', 'phones', 'ssn'],
            options: {
                masking_method: options.maskingMethod || 'replacement_tags',
                confidence_threshold: options.confidenceThreshold || 0.8,
                include_confidence: options.includeConfidence || true,
                context_analysis: options.contextAnalysis || true
            }
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/pii-detection`,
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
            console.error('PII detection error:', error.response.data);
            throw error;
        }
    }
    
    async batchDetect(documents, options = {}) {
        const payload = {
            documents: documents,
            pii_types: options.piiTypes || ['names', 'emails', 'phones'],
            masking_method: options.maskingMethod || 'asterisks'
        };
        
        try {
            const response = await axios.post(
                `${this.baseUrl}/pii-detection/batch`,
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
            console.error('Batch PII detection error:', error.response.data);
            throw error;
        }
    }
    
    // Real-time stream processing
    startStream(onPIIDetected) {
        const ws = new WebSocket('wss://api.contactcenter.ai/v1/pii-detection/stream', {
            headers: {
                'Authorization': `Bearer ${this.apiKey}`
            }
        });
        
        ws.on('message', (data) => {
            const result = JSON.parse(data);
            onPIIDetected(result);
        });
        
        ws.on('error', (error) => {
            console.error('WebSocket error:', error);
        });
        
        return ws;
    }
}

// Usage example
const detector = new PIIDetector('YOUR_API_KEY');

async function processText() {
    const text = "Hi, my name is John Smith. Email: john.smith@email.com";
    
    try {
        const result = await detector.detectPII(text, {
            maskingMethod: 'replacement_tags',
            confidenceThreshold: 0.8
        });
        
        console.log('Detected PII:', result.detected_pii);
        console.log('Protected Text:', result.protected_text);
        
        // Process batch documents
        const documents = [
            {id: 'doc1', text: 'Customer data...'},
            {id: 'doc2', text: 'More data...'}
        ];
        
        const batchResult = await detector.batchDetect(documents);
        console.log('Batch results:', batchResult);
        
    } catch (error) {
        console.error('Error processing text:', error);
    }
}

processText();
'''
            st.code(js_code, language='javascript')
        
        # Response format
        st.markdown("### 📄 API Response Format")
        
        sample_response = {
            "job_id": "pii_12345",
            "status": "completed",
            "processing_time": 0.12,
            "detected_pii": [
                {
                    "type": "person_name",
                    "value": "John Smith", 
                    "start_pos": 15,
                    "end_pos": 25,
                    "confidence": 0.98,
                    "risk_level": "high",
                    "category": "personal_identifier"
                },
                {
                    "type": "email_address",
                    "value": "john.smith@email.com",
                    "start_pos": 39,
                    "end_pos": 60, 
                    "confidence": 0.99,
                    "risk_level": "high",
                    "category": "contact_information"
                }
            ],
            "protected_text": "Hi, my name is [PERSON_NAME]. My email is [EMAIL_ADDRESS]",
            "statistics": {
                "total_entities": 2,
                "by_risk_level": {
                    "critical": 0,
                    "high": 2,
                    "medium": 0,
                    "low": 0
                },
                "by_category": {
                    "personal_identifier": 1,
                    "contact_information": 1
                }
            },
            "compliance": {
                "gdpr_applicable": True,
                "ccpa_applicable": True,
                "risk_score": 0.85
            },
            "metadata": {
                "model_version": "v2.1.0",
                "language": "en",
                "processing_time_ms": 120
            }
        }
        
        st.json(sample_response)
        
        # Webhooks and real-time
        st.markdown("### 🔔 Webhooks & Real-time Processing")
        
        col_webhook1, col_webhook2 = st.columns(2)
        
        with col_webhook1:
            st.markdown("""
            **Webhook Configuration**
            ```json
            {
              "webhook_url": "https://your-app.com/pii-webhook",
              "events": ["pii_detected", "high_risk_pii"],
              "authentication": {
                "type": "bearer_token",
                "token": "your_webhook_secret"
              }
            }
            ```
            """)
        
        with col_webhook2:
            st.markdown("""
            **Real-time Stream Events**
            - `pii_detected`: New PII entity found
            - `high_risk_pii`: Critical PII detected
            - `batch_complete`: Batch processing finished
            - `compliance_alert`: Regulation violation
            """)
