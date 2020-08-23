from flask import Flask, request, jsonify
from flask.json import JSONEncoder
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

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/test", methods=['POST'])
def test():
    data    = request.json
    system('export GOOGLE_APPLICATION_CREDENTIALS="/root/ce.json"')
    test1 = system('export GOOGLE_APPLICATION_CREDENTIALS="/root/ce.json"; curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @test2.json https://automl.googleapis.com/v1beta1/projects/saiki-200813/locations/us-central1/models/TBL4476826519234150400:predict')
    #system('export GOOGLE_APPLICATION_CREDENTIALS="/root/ce.json"')
    #test1   = system('/root/Python/culturalEventInfo/test.sh')

    return jsonify(test1)

def sign_up():
    new_user    = request.json
    new_user["id"]  = app.id_count
    app.users[app.id_count] = new_user
    app.id_count            = app.id_count + 1

    return jsonify(new_user)

@app.route("/tweet", methods = ['POST'])
def tweet():
    payload = request.json
    user_id = int(payload['id'])
    tweet   = payload['tweet']

    if user_id not in app.users:
        return '사용자가 존재하지 않습니다', 400
    if len(tweet) > 300:
        return '300자를 조과하였습니다', 400

    app.tweets.append({
        'user_id'   : user_id,
        'tweet'     : tweet
    })

    return '', 200

@app.route("/follow", methods = ['POST'])
def follow():
    payload = request.json
    user_id = int(payload['id'])
    follow  = int(payload['follow'])

    if user_id not in app.users or follow not in app.users:
        return '사용자가 존재하지 않습니다', 400

    user = app.users[user_id]
    user.setdefault('follow', set()).add(follow)

    return jsonify(user)

@app.route("/unfollow", methods = ['POST'])
def unfollow():
    payload = request.json
    user_id = int(payload['id'])
    follow  = int(payload['unfollow'])

    if user_id not in app.users or follow not in app.users:
        return '사용자가 존재하지 않습니다', 400

    user = app.users[user_id]
    user.setdefault('follow', set()).discard(follow)
    # discard() 대신 remove() 사용시 지우려는 엘리먼트가 존재하지 않으면 KeyError가 발생
    return jsonify(user)


@app.route("/timeline/<int:user_id>", methods = ['GET'])
def timeline(user_id):
    if user_id not in app.users:
        return '사용자가 존재하지 않습니다', 400
    follow_list = app.users[user_id].get('follow', set())
    follow_list.add(user_id)
    timeline = [tweet for tweet in app.tweets if tweet['user_id'] in follow_list]

    return jsonify({
        'user_id'   : user_id,
        'timeline'  : timeline
    })

if __name__ == '__main__':
        app.run('0.0.0.0', port=80)
