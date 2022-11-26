from main import app
from flask_cors import cross_origin
import json
from flask_login import login_required, logout_user


@cross_origin(origin='*')
@login_required
@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return json.dumps({'result': 'Success'}), 200

