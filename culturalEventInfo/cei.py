from flask      import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text
import requests

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
        'use_trgt'      : user['use_trgt'],
        'use_fee'       : user['use_fee'],
        'gcode'         : user['gcode'],
        'keyword'       : user['keyword']
    } if user else None

def get_origin(user_id):
    user = current_app.database.execute(text("""
        SELECT
            CODENAME,
            TITLE,
            DATE,
            PLACE,
            ORG_NAME,
            USE_TRGT,
            USE_FEE,
            PLAYER,
            PROGRAM,
            ETC_DESC,
            ORG_LINK,
            MAIN_IMG,
            RGSTDATE,
            TICKET,
            STRTDATE,
            END_DATE,
            THEMECODE
        FROM origin_cultural_event_info
        WHERE id = :user_id
    """), {
        'user_id' : user_id
    }).fetchone()

    return {
        'CODENAME'  : user['CODENAME'],
        'TITLE'     : user['TITLE'],
        'DATE'  : user['DATE']
        'PLACE' : user['PLACE'],
        'ORG_NAME'  : user['ORG_NAME'],
        'USE_TRGT'  : user['USE_TRGT'],
        'USE_FEE'   : user['USE_FEE'],
        'PLAYER'    : user['PLAYER],
        'PROGRAM'    : user['PROGRAM'],
        'ETC_DESC'   : user['ETC_DESC'],
        'ORG_LINK'   : user['ORG_LINK'],
        'MAIN_IMG'   : user['MAIN_IMG'],
        'RGSTDATE'   : user['RGSTDATE'],
        'TICKET' : user['TICKET'],
        'STRTDATE'   : user['TICKET'],
        'END_DATE'   : user['END_DATE'],
        'THEMECODE'  : user['THEMECODE']']
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

def insert_origin(user):
    return current_app.database.execute(text("""
        INSERT INTO preference (
            CODENAME,
            TITLE,
            DATE,
            PLACE,
            ORG_NAME,
            USE_TRGT,
            USE_FEE,
            PLAYER,
            PROGRAM,
            ETC_DESC,
            ORG_LINK,
            MAIN_IMG,
            RGSTDATE,
            TICKET,
            STRTDATE,
            END_DATE,
            THEMECODE
        ) VALUES (
            :CODENAME,
            :TITLE,
            :DATE,
            :PLACE,
            :ORG_NAME,
            :USE_TRGT,
            :USE_FEE,
            :PLAYER,
            :PROGRAM,
            :ETC_DESC,
            :ORG_LINK,
            :MAIN_IMG,
            :RGSTDATE,
            :TICKET,
            :STRTDATE,
            :END_DATE,
            :THEMECODE
        )
    """), user).rowcount

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

    @app.route("/update", methods=['POST'])
    def update():
        req = requests.get('http://openapi.seoul.go.kr:8088/414a5975666b796a3132324142416376/json/culturalEventInfo/1/1')
        originList = req.json
        info = insert_origin(originList)
        cinfo    = get_origin(info)

        return jsonify(cinfo)

    @app.route("/preference", methods=['POST'])
    def preference():
        new_prefernce    = request.json
        new_prefernce_id = insert_prefernce(new_prefernce)
        new_prefernce    = get_prefernce(new_prefernce_id)

        return jsonify(new_prefernce)

    return app

