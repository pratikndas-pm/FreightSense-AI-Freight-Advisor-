
# Deploy — FreightSense Online (All Free)

## 0) Push to GitHub
git init && git add . && git commit -m "FreightSense online demo"
git branch -M main
git remote add origin https://github.com/<you>/freightsense-online.git
git push -u origin main

## 1) LLM on Hugging Face Spaces (Free CPU)
Create Python Space → upload /llm-space (app.py, requirements.txt, README.md) → Deploy → enable API.
Endpoint: https://<your-space>.hf.space/generate

## 2) Backend on Render (Free)
Root: /backend
Build: pip install -r requirements.txt
Start: uvicorn main:app --host 0.0.0.0 --port $PORT
Env: LLM_URL=https://<your-space>.hf.space/generate

## 3) Frontend on Vercel (Free)
Root: /frontend
Env: NEXT_PUBLIC_API_URL=https://<your-render>.onrender.com

## Extra
- Vector RAG: POST /chat/docs_vector
- Quote PDF: POST /export/quote_pdf_from_data
