from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/akaryakit", methods=["GET"])
def get_akaryakit():
    try:
        # Dosya mevcut mu kontrol et
        if not os.path.exists("tum_akaryakit.json"):
            return jsonify({"error": "Veri dosyası bulunamadı"}), 404
        
        # Dosyayı oku
        with open("tum_akaryakit.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # JSON olarak dön
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Hata oluştu: {str(e)}"}), 500

@app.route("/", methods=["GET"])
def home():
    return {"message": "Akaryakıt API çalışıyor. Verilere /akaryakit yolundan ulaşabilirsiniz."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
