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

def get_user(user_id):
    user = current_app.database.execute(text("""
        SELECT
            id,
            name,
            email,
            profile
        FROM users
        WHERE id = :user_id
    """), {
        'user_id' : user_id
    }).fetchone()

    return {
        'id'      : user['id'],
        'name'    : user['name'],
        'email'   : user['email'],
        'profile' : user['profile']
    } if user else None

def insert_user(user):
    return current_app.database.execute(text("""
        INSERT INTO users (
            name,
            email,
            profile,
            hashed_password
        ) VALUES (
            :name,
            :email,
            :profile,
            :password
        )
    """), user).lastrowid


def create_app(test_config = None):
    app = Flask(__name__)

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

    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        new_user    = request.json
        new_user_id = insert_user(new_user)
        new_user    = get_user(new_user_id)

        return jsonify(new_user)

