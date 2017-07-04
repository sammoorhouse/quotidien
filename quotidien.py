from flask import Flask, render_template, request, send_from_directory
import redis
import datetime
import os

app = Flask(__name__)
r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ["REDIS_PORT"], db=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg', methods=['POST'])
def register():
    name = request.form['name']
    date = datetime.datetime.now()

    useragent = request.headers.get('User-Agent')
    print "saving [" + name + " " + date + " " + useragent + "]"
    r.set((name, date), useragent)
    return render_template('done.html')

@app.route('/css/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')