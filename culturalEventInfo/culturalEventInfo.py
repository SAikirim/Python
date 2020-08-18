from flask      import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text

## Default JSON encoder는 set를 JSON으로 변환할 수 없다.
## 그럼으로 커스텀 엔코더를 작성해서 set을 list로 변환하여
## JSON으로 변환 가능하게 해주어야 한다.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


def get_prefernce(user_id):
    user = current_app.database.execute(text("""
        SELECT
            gender,
            codename,
            desired_date,
            time,
            use_trgt,
            use_fee,
            gcode,
            keyword
        FROM preference
        WHERE id = :user_id
    """), {
        'user_id' : user_id
    }).fetchone()

    return {
        'gender'        : user['gender'],
        'codename'      : user['codename'],
        'desired_date'  : user['desired_date'],
        'time'          : user['time'],
        'use_trgt'      : user['use_trgt],
        'use_fee'       : user['use_fee'],
        'gcode'         : user['gcode'],
        'keyword'       : user['keyword']
    } if user else None

def insert_prefernce(user):
    return current_app.database.execute(text("""
        INSERT INTO preference (
            age,
            gender,
            desired_date,
            time,
            jenre,
            keyword
        ) VALUES (
            :age,
            :gender,
            :desired_date,
            :time,
            :jenre,
            :keyword
        )
    """), user).lastrowid

def create_app(test_config = None):
    app = Flask(__name__)
    app.run(host = '0.0.0.0', port = 8080)

    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database     = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
    app.database = database

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"

    @app.route("/preference", methods=['POST'])
    def preference():
        new_prefernce    = request.json
        new_prefernce_id = insert_prefernce(new_prefernce)
        new_prefernce    = get_prefernce(new_prefernce_id)

        return jsonify(new_prefernce)

    return app

