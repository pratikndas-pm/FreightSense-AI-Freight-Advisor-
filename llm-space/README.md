---
title: FreightSense-LLM
emoji: 🚢
colorFrom: indigo
colorTo: blue
sdk: fastapi
app_file: app.py
pinned: false
---

# FreightSense – LLM Microservice (Free)

This Space hosts a small FastAPI app wrapping the **Qwen 0.5B Instruct** model for the FreightSense demo.

### 🔗 Endpoints

- **GET /** → health check (`{"ok": true}`)
- **POST /generate** → generate a concise answer  
  **Example**
  ```bash
  curl -X POST https://<your-space>.hf.space/generate \
       -H "Content-Type: application/json" \
       -d '{"prompt":"Summarize: Freight quote DXB→HAM", "temperature":0.2}'
