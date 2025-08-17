from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 ESP32 OTA Server is running on Render!"

# Serve firmware to ESP32
@app.route("/firmware.bin", methods=["GET"])
def firmware():
    return send_file("firmware.bin", as_attachment=True)

# Simple upload page
@app.route("/upload", methods=["POST"])
def upload_firmware():
    file = request.files["file"]
    file.save("firmware.bin")
    return "✅ Firmware uploaded successfully!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
