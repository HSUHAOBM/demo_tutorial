from flask import Flask, render_template
from redis import Redis
from datetime import datetime

app = Flask(__name__)
redis = Redis(host='myredis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    redis.expire('hits', 6600)
    num = redis.get('hits').decode("utf-8")
    return 'server 1 - 你好! 我們見過 %s 次面。' % num

@app.route('/test')
def index():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5800)
