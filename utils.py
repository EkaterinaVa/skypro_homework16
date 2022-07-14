# Файл с основными функциями приложения

import json
from models import *


# Пользовательские функции
def insert_data_user(input_data):
    """Функция добавления пользователя"""
    for data in input_data:
        db.session.add(
            User(
                id=data.get("id"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                age=data.get("age"),
                email=data.get("email"),
                role=data.get("role"),
                phone=data.get("phone")
            )
        )

    db.session.commit()


def get_all_users_by_id(user_id):
    """Функция получения пользователя по id"""
    return db.session.query(User).filter(User.id==user_id).all()[0].to_dict()


# Функции заказов
def insert_data_order(input_data):
    """Функция добавления заказа"""
    for data in input_data:
        db.session.add(
            Order(
                id=data.get("id"),
                name=data.get("name"),
                description=data.get("description"),
                start_date=data.get("start_date"),
                end_date=data.get("end_date"),
                address=data.get("address"),
                price=data.get("price"),
                customer_id=data.get("customer_id"),
                executor_id=data.get("executor_id")
            )
        )

    db.session.commit()


def get_all_orders_by_id(order_id):
    """Функция получения заказа по id"""
    return db.session.query(Order).filter(Order.id==order_id).all()[0].to_dict()


# Функции предложений (Offers)
def insert_data_offer(input_data):
    """Функция добавления предложения"""
    for data in input_data:
        db.session.add(
            Offer(
                id=data.get("id"),
                order_id=data.get("order_id"),
                executor_id=data.get("executor_id")
            )
        )

    db.session.commit()


def get_all_offers_by_id(offer_id):
    """Функция получения заказа по id"""
    return db.session.query(Offer).filter(Offer.id==offer_id).all()[0].to_dict()


def init_db():
    """Инициализация db"""
    db.drop_all()
    db.create_all()

    with open("./data/users.json", encoding='utf-8') as f:
        insert_data_user(json.load(f))

    with open("./data/orders.json", encoding='utf-8') as f:
        insert_data_order(json.load(f))

    with open("./data/offers.json", encoding='utf-8') as f:
        insert_data_offer(json.load(f))


# Универсальные функции
def update_universal(model, user_id, values):
    """Обновление данных"""
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception:
        return {}


def delete_universal(model, user_id):
    """Удаление данных"""
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception:
        return {}


def get_all(model):
    """Универсальная функция - получение всех экземпляров модели. Возвращает список."""
    result = []
    for i in db.session.query(model).all():
        result.append(i.to_dict())

    return result
