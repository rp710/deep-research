---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Deep Research

## Deploy on Render for free

Create a Render **Web Service** connected to this repository with:

- Root directory: `2_openai/deep_research`
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`

Add the following environment variables in Render. Keep secrets out of the repository:

```text
OPENAI_API_KEY
DEFAULT_MODEL_NAME=gpt-5.4-mini
USE_EMAIL=false
EMAIL_ADDRESS
EMAIL_SMTP_SERVER
EMAIL_APP_PASSWORD
PUSHOVER_USER
PUSHOVER_TOKEN
```

Set `USE_EMAIL=true` only after configuring the SMTP variables. With `USE_EMAIL=false`,
the email agent uses the Pushover fallback instead.

The app reads Render's `PORT` variable automatically and continues to use port `7860`
when run locally. Render's free services sleep after inactivity, so the first request
after a quiet period can take a little longer.
