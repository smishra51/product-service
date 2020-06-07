from flask import request, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Product
from flask import jsonify


@app.route('/', methods=['GET'])
def healthcheck():
    return make_response(jsonify({"health": "ok"}), 200)


@app.route("/product", methods=['POST'])
def add():
    product: Product = request.json
    if product:
        existing_product = Product.query.filter(
            Product.productName == product["productName"] and Product.productBrand == product["productBrand"]).first()
        if existing_product:
            return make_response(jsonify({"productName": product["productName"]}), 409)
        newproduct = Product(productName=product["productName"],
                             productBrand=product["productBrand"],
                             created=dt.now(),
                             amount=product["amount"],
                             quantity=product["quantity"])
        db.session.add(newproduct)
        db.session.commit()
        return make_response(jsonify(data=[e.serialize() for e in Product.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/product", methods=['GET'])
def get():
    data = Product.query.all()
    if data:
        return make_response(jsonify(data=[e.serialize() for e in Product.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 203)


@app.route("/product/<int:productid>", methods=['GET'])
def findbyid(productid):
    if productid:
        product = Product.query.filter(Product.productId == productid).first()
        if product:
            return make_response(jsonify(data=product.serialize()), 200)
        return make_response(jsonify({"resp": "Not found"}), 404)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/product", methods=['PUT'])
def update():
    product: Product = request.json
    if product:
        existing_product: Product = Product.query.filter(Product.productId == product["productId"]).first()
        if not existing_product:
            return make_response(jsonify({"productName": product["productName"]}), 404)
        existing_product.productName = product["productName"]
        existing_product.amount = product["amount"]
        existing_product.quantity = product["quantity"]
        existing_product.productBrand = product["productBrand"]
        db.session.add(existing_product)
        db.session.commit()
        return make_response(jsonify(data=existing_product.serialize()), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/product", methods=['DELETE'])
def delete():
    product: Product = request.json
    if product:
        existing_product: Product = Product.query.filter(Product.productId == product["productId"]).first()
        if not existing_product:
            return make_response(jsonify({"productId": product["productId"]}), 404)
        db.session.delete(existing_product)
        db.session.commit()
        return make_response(jsonify({"resp": "Successfully deleted"}), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)
