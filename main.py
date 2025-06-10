from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/akaryakit", methods=["GET"])
def get_akaryakit():
    with open("tum_akaryakit.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Akaryakıt API çalışıyor. Verilere /akaryakit yolundan ulaşabilirsiniz."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
