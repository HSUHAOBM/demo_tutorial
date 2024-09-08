from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message='Hello from Docker and Flask!')


# Webhook 接收的請求方法為 POST
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    # 取得接收到的 JSON 資料
    data = request.get_json()

    # 在這裡處理接收到的資料，可以根據你的需求進行相應的處理
    # 這裡只是簡單地印出接收到的資料
    print("Received Webhook Data:")
    print(data)

    # 回應表示成功接收資料
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)