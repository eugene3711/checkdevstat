from flask import Flask, jsonify, request
import urlcheck
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getstatus', methods=['POST'])
def get_status():
    if request.method == 'POST':
        request_json = request.json
        dev_url = request_json.get('url')
        status = urlcheck.get_status(dev_url)
        answer = {'status': status}
        return jsonify(answer)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
