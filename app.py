import json
from models import User, Order, Offer
from setup_db import db
from utils import get_all, insert_data_user, get_all_users_by_id, get_all_orders_by_id, get_all_offers_by_id, \
    update_universal, delete_universal, insert_data_order, insert_data_offer, init_db
from flask import Flask
from flask import request


app = Flask(__name__)

# Конфиги
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mybase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

# Добавляем контекст приложения
db.init_app(app)
app.app_context().push()
init_db()


# Вьюшки
@app.route("/users/", methods=['GET', 'POST'])
def get_all_users():
    """
    Вьюшка обрабатывает GET-запросы получения всех пользователей
    и POST-запросы (создание пользователей)
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User)),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Неверный тип данных")

        return app.response_class(
            response=json.dumps(request.json),
            status=200,
            mimetype="application.json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    """
    Вьюшка обрабатывает GET-запросы получения пользователей по id,
    PUT-запросы на изменение пользователей и DELETE-запросы - удаление
    пользователей
    """
    if request.method == 'GET':
        data = get_all_users_by_id(user_id)

        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps("OK"),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps("ПОЛЬЗОВАТЕЛЬ УДАЛЁН"),
            status=200,
            mimetype="application.json"
        )

@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    """
    Вьюшка обрабатывает GET-запросы получения всех заказов
    и POST-запросы (создание заказов)
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order)),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Неверный тип данных")

        return app.response_class(
            response=json.dumps(request.json),
            status=200,
            mimetype="application.json"
        )


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(order_id):
    """
    Вьюшка обрабатывает GET-запросы получения заказов по id,
    PUT-запросы на изменение заказов и DELETE-запросы - удаление
    заказов
    """
    if request.method == 'GET':
        data = get_all_orders_by_id(order_id)

        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'PUT':
        update_universal(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps("OK"),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'DELETE':
        delete_universal(Order, order_id)
        return app.response_class(
            response=json.dumps("ЗАКАЗ УДАЛЁН"),
            status=200,
            mimetype="application.json"
        )

@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    """
    Вьюшка обрабатывает GET-запросы получения всех предложений
    и POST-запросы (создание предложений)
    """
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer)),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Неверный тип данных")

        return app.response_class(
            response=json.dumps(request.json),
            status=200,
            mimetype="application.json"
        )


@app.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(offer_id):
    """
    Вьюшка обрабатывает GET-запросы получения предложений по id,
    PUT-запросы на изменение предложений и DELETE-запросы - удаление
    предложений
    """
    if request.method == 'GET':
        data = get_all_offers_by_id(offer_id)

        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'PUT':
        update_universal(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps("OK"),
            status=200,
            mimetype="application.json"
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, offer_id)
        return app.response_class(
            response=json.dumps("ПРЕДЛОЖЕНИЕ УДАЛЕНО"),
            status=200,
            mimetype="application.json"
        )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

