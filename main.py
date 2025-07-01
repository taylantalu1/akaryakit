from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/akaryakit", methods=["GET"])
def get_akaryakit():
    try:
        # Dosya var mı kontrol et
        if not os.path.exists("tum_akaryakit.json"):
            return jsonify({"error": "Veri dosyası bulunamadı"}), 404

        # Dosyayı oku
        with open("tum_akaryakit.json", "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return jsonify({"error": "Dosya boş"}), 500
            data = json.loads(content)

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Hata: {str(e)}"}), 500

@app.route("/", methods=["GET"])
def home():
    return {"message": "Akaryakıt API çalışıyor. Verilere /akaryakit yolundan ulaşabilirsiniz."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
