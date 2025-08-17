from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ ESP32 OTA Update Server is Running!"

@app.route("/firmware", methods=["GET"])
def firmware():
    return send_file("firmware.bin", as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file uploaded", 400
    file = request.files["file"]
    file.save("firmware.bin")
    return "Firmware uploaded successfully ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
