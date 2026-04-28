# 🔍 Phishing Email Analyzer
> An AI-powered phishing detection tool built with Claude + Streamlit

---

## ⚡ Quick Start (A to Z Guide)

---

### STEP 1 — Install Python

1. Go to https://python.org/downloads
2. Download Python 3.11 or higher
3. Run the installer — check **"Add Python to PATH"** during install
4. Verify: open a terminal and run:
   ```
   python --version
   ```
   You should see something like `Python 3.11.x`

---

### STEP 2 — Get Your Anthropic API Key (Free)

1. Go to https://console.anthropic.com
2. Sign up for a free account
3. Click **"API Keys"** in the left sidebar
4. Click **"Create Key"** → copy and save it somewhere safe
5. You get free credits to start — enough to test hundreds of emails

---

### STEP 3 — Set Up Your Project Folder

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

```bash
mkdir phishing-analyzer
cd phishing-analyzer
```

Copy the `app.py` and `requirements.txt` files into this folder.

---

### STEP 4 — Install Dependencies

In your terminal (inside the project folder):

```bash
pip install -r requirements.txt
```

This installs Streamlit and the Anthropic SDK. Takes 1-2 minutes.

---

### STEP 5 — Run Locally (Test It First)

```bash
streamlit run app.py
```

Your browser will open automatically at http://localhost:8501

- Enter your API key in the settings
- Click "Load sample email"
- Click "Analyze Email"
- You should see the risk score appear ✅

---

### STEP 6 — Push to GitHub (Required for deployment)

1. Go to https://github.com and create a free account
2. Click **"New repository"** → name it `phishing-analyzer` → set to Public → click Create
3. In your terminal:

```bash
git init
git add .
git commit -m "Initial commit - phishing analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/phishing-analyzer.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

### STEP 7 — Deploy to Streamlit Cloud (Free, Public URL)

1. Go to https://streamlit.io/cloud
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your `phishing-analyzer` repository
5. Main file path: `app.py`
6. Click **"Deploy"**

Wait 2-3 minutes → you get a live URL like:
`https://yourname-phishing-analyzer.streamlit.app`

**That's it! Your app is live on the internet. 🎉**

---

### STEP 8 — Share It and Get Clients

Post this on LinkedIn:

> "Just built an AI-powered phishing email analyzer using Claude AI.
> Paste any suspicious email and it gives you a risk score, red flags,
> and detailed breakdown in seconds.
> 
> Built this as a SOC intern to help security teams triage faster.
> Live demo: [your URL here]
> 
> Happy to set this up for your company's security team. DM me."

---

## 📁 Project Structure

```
phishing-analyzer/
├── app.py              ← Main Streamlit app
├── requirements.txt    ← Python dependencies
└── README.md           ← This file
```

---

## 💰 How to Monetize

| Method | How | Potential |
|--------|-----|-----------|
| Freelance | Offer to set this up for companies on Fiverr/Upwork | $100-500/project |
| Customize | Add company branding, extra features for clients | $200-1000/project |
| SaaS | Add Stripe paywall, charge $9-29/month | Recurring income |
| Job leverage | Show this in interviews as a portfolio project | Higher salary |

---

## 🔧 Ideas to Improve It Later

- Add URL scanning (check if links are in threat databases)
- Add email header analysis
- Export report as PDF
- Add history of analyzed emails
- Connect to a real SIEM like Splunk

---

## 📞 Questions?

Built by a SOC intern learning AI security automation.
