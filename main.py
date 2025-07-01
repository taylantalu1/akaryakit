from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/akaryakit", methods=["GET"])
def get_akaryakit():
    data = {
        "adana": {
            "aladag": [
                {
                    "Benzin": "₺49,98",
                    "Dagitici": "Petrol Ofisi",
                    "LPG": "₺24,99",
                    "Motorin": "₺51,20",
                    "Tarih": "17.06.2025"
                }
            ]
        }
    }
    return jsonify(data)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Akaryakıt API çalışıyor. Verilere /akaryakit yolundan ulaşabilirsiniz."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
