import streamlit as st
from groq import Groq
import json

st.set_page_config(page_title="Phishing Email Analyzer", page_icon="🔍", layout="centered")

st.markdown("""
<style>
    .score-box { padding:1rem 1.5rem; border-radius:12px; margin-bottom:1rem; font-size:1.1rem; font-weight:600; }
    .score-safe    { background:#EAF3DE; color:#3B6D11; border:1px solid #C0DD97; }
    .score-low     { background:#FAEEDA; color:#854F0B; border:1px solid #FAC775; }
    .score-medium  { background:#FAEEDA; color:#854F0B; border:1px solid #FAC775; }
    .score-high    { background:#FCEBEB; color:#A32D2D; border:1px solid #F09595; }
    .score-critical{ background:#FCEBEB; color:#A32D2D; border:1px solid #F09595; }
    .flag-tag { display:inline-block; padding:3px 12px; border-radius:100px; font-size:0.8rem; margin:3px; }
</style>
""", unsafe_allow_html=True)

SAMPLE_EMAIL = """From: security-alert@paypa1.support
Subject: URGENT: Your account has been suspended - Verify immediately

Dear Valued Customer,

We have detected suspicious activity on your PayPal account. Your account has been
temporarily suspended for security reasons.

You must verify your identity within 24 HOURS or your account will be permanently
closed and funds frozen.

Click here to verify now: http://paypa1-secure-verify.xyz/login?ref=urgent

You will need to provide:
- Full name
- Credit card number
- Social Security Number
- Password

Failure to act immediately will result in permanent account closure.

PayPal Security Team
© PayPal Inc. 2024"""

def score_class(score):
    if score <= 2: return "score-safe"
    if score <= 4: return "score-low"
    if score <= 6: return "score-medium"
    if score <= 8: return "score-high"
    return "score-critical"

def score_emoji(score):
    if score <= 2: return "✅"
    if score <= 4: return "⚠️"
    if score <= 6: return "🟠"
    return "🚨"

def analyze_email(email_text, api_key):
    client = Groq(api_key=api_key)
    prompt = f"""You are a cybersecurity expert specializing in phishing detection.
Analyze this email and respond ONLY with a JSON object — no markdown, no backticks, no extra text, no explanation.
Start your response with {{ and end with }}

Email to analyze:
{email_text}

Return this exact JSON structure:
{{
  "score": <number 1-10>,
  "verdict": "<Safe | Low Risk | Suspicious | Likely Phishing | Definite Phishing>",
  "flags": ["<short flag label>", ...],
  "analysis": "<2-3 paragraph analysis explaining indicators found, tactics used, and what the recipient should do>"
}}

Score guide: 1-2=safe, 3-4=low risk, 5-6=suspicious, 7-8=likely phishing, 9-10=definite phishing.
Flags: short labels like Urgency tactics, Suspicious sender domain, Requests sensitive data. Max 6 flags."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1024,
    )
    raw = response.choices[0].message.content.strip()
    # Extract JSON object regardless of extra text
    start = raw.find("{")
    end = raw.rfind("}") + 1
    if start != -1 and end > start:
        raw = raw[start:end]
    return json.loads(raw)

st.title("🔍 Phishing Email Analyzer")
st.markdown("Paste a suspicious email below to detect phishing indicators and get an AI-powered risk score.")
st.divider()

with st.expander("⚙️ API Key Settings"):
    api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...", help="Get your free key at console.groq.com")
    st.caption("Your key is never stored — it's only used for this session.")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("Load sample email", use_container_width=True):
        st.session_state["email_input"] = SAMPLE_EMAIL

email_text = st.text_area("Email content", value=st.session_state.get("email_input", ""), placeholder="Paste the full email here (subject, sender, body, links...)", height=220, key="email_input")

analyze_clicked = st.button("🔎 Analyze Email", type="primary", use_container_width=True)

if analyze_clicked:
    if not api_key:
        st.error("Please enter your Groq API key in the settings above.")
    elif not email_text.strip():
        st.warning("Please paste an email to analyze.")
    else:
        with st.spinner("Analyzing for phishing indicators..."):
            try:
                result = analyze_email(email_text, api_key)
                score    = result.get("score", 0)
                verdict  = result.get("verdict", "Unknown")
                flags    = result.get("flags", [])
                analysis = result.get("analysis", "")

                st.divider()
                st.subheader("Analysis Result")
                css_cls = score_class(score)
                emoji   = score_emoji(score)
                st.markdown(f'<div class="score-box {css_cls}">{emoji} Risk Score: <strong>{score}/10</strong> — {verdict}</div>', unsafe_allow_html=True)

                if flags:
                    st.markdown("**Red flags detected:**")
                    flag_html = ""
                    for flag in flags:
                        color      = "#FCEBEB" if score >= 7 else "#FAEEDA" if score >= 4 else "#EAF3DE"
                        text_color = "#A32D2D" if score >= 7 else "#854F0B" if score >= 4 else "#3B6D11"
                        border     = "#F09595" if score >= 7 else "#FAC775" if score >= 4 else "#C0DD97"
                        flag_html += f'<span class="flag-tag" style="background:{color};color:{text_color};border:1px solid {border};">{flag}</span>'
                    st.markdown(flag_html, unsafe_allow_html=True)
                    st.markdown("")

                st.markdown("**Detailed analysis:**")
                st.markdown(analysis)
                st.divider()
                if score >= 7:
                    st.error("⛔ Do NOT click any links or provide any information from this email.")
                elif score >= 4:
                    st.warning("⚠️ Be cautious. Verify the sender through official channels before taking action.")
                else:
                    st.success("✅ This email appears legitimate, but always stay vigilant.")

            except json.JSONDecodeError:
                st.error("Failed to parse the AI response. Please try again.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.divider()
st.caption("Built with Groq + Llama 3 · For educational and professional use · Always verify with your security team")