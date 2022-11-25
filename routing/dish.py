from entities import User
from main import app, db
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@login_required
@app.route('/dish', methods=['UPDATE'])
def update_dish():
    body = json.loads(request.data)

    user = User.query.filter_by(id=current_user.id).first_or_404()
    user_dishes = []
    for rest in user.restaurants:
        for menu in rest.menu:
            for dish in menu.dishes:
                user_dishes.append(dish)
    filtered_dish = list(filter(lambda dish: dish.id == body.get('id'), user_dishes))
    if len(filtered_dish) == 0:
        return json.dumps({'result': 'You do not have access to this resource'}, indent=4), 404
    dish = filtered_dish[0]

    for k, v in dish.__dict__:
        dish[k] = body.get(k)
    db.session.commit()

    return json.dumps({'result': 'Success', 'updated_item': dish.to_dict()}), 200

