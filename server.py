from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

# ✅ Root check
@app.route("/")
def home():
    return "✅ ESP32 OTA Server is running on Render!"

# ✅ Serve firmware file for OTA
@app.route("/firmware", methods=["GET"])
def firmware():
    try:
        return send_file("firmware.bin", as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Upload new firmware file from web
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save as firmware.bin
    file.save("firmware.bin")
    return jsonify({"message": "Firmware uploaded successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
