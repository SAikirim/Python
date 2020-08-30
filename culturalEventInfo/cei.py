from flask import Flask, request, jsonify
from flask.json import JSONEncoder
import json
from os import system

## Default JSON encoder는 set를 JSON으로 변환할 수 없음
## 그러므로 커스텀 엔코더를 작성하여 set를 list로 변환 후
## JSON으로 변환 가능하게 만들어줌

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.id_count = 1
app.users    = {}
app.tweets  = []
app.json_encoder = CustomJSONEncoder

@app.route("/ping", methods=['GET', 'post'])
def ping():
    return "pong\n"

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    system('export GOOGLE_APPLICATION_CREDENTIALS="/root/ce.json"; curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d  @static/save.txt https://automl.googleapis.com/v1beta1/projects/saiki-200813/locations/us-central1/models/TBL4476826519234150400:predict > static/result.json')

    return "request good\n"

@app.route("/upload", methods=['POST'])
def upload():
    data   = request.json
    with open("static/save.json","w", encoding='utf-8') as f:
        json.dump(data, f)

    return jsonify(data)

@app.route("/download", methods=['GET', 'POST'])
def download():
    with open("static/result.json","r", encoding='utf-8') as f:
        json_data = json.load(f)

    return jsonify(json_data)

@app.route("/download2/<int:num>", methods=['GET', 'POST'])
def download2(num):
    with open("static/result.json","r", encoding='utf-8') as f:
        json_data = json.load(f)
        json_list = [[data["tables"]["score"], data["tables"]["value"]] for data in json_data["payload"]]
        json_list.sort(reverse=True)
        if num > 0 and num <= len(json_list):
            jlist = [json_list[i][1] for i in range(num)]
        else:
            jlist = [json_list[i][1] for i in range(len(json_list))]

        jdict = [{"value": i} for i in jlist]
        res = app.response_class(
            response = json.dumps(jdict, ensure_ascii=False),
            mimetype='application/json'
        )
    return res # jsonify(jlist)

if __name__ == '__main__':
        app.run('0.0.0.0', port=5000, debug=True)
