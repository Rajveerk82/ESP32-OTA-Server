# ESP32 OTA Update Server

This is a simple Flask-based server for hosting **ESP32 OTA updates**.

## 🚀 Deploy on Render
1. Fork/clone this repo.
2. Push to your GitHub.
3. Create a **Web Service** on Render.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn server:app`

## 📡 API Endpoints
- `/` → Check if server is running
- `/firmware` → Download firmware.bin (used by ESP32 for OTA update)
- `/upload` (POST) → Upload new firmware.bin from your PC

## 📥 Example Upload with CURL
```bash
curl -X POST -F "file=@firmware.bin" https://your-render-url/upload
