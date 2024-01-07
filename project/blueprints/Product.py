import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args
from project.app.db import mongo
from project.app.schemas.ProductSchema import ProductSchema, product_SC
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.ProductBLC import ProductBLC
from project.app.repositories.ProductRepository import ProductRepository

bp = Blueprint("product", __name__)


@bp.route("/api/add_product", methods=["POST"])
@use_args(ProductSchema, location="json")
def add_supplier(args):
    """adding the product in db"""
    category = ProductBLC.adding_product(args)
    std = ProductSchema()
    result = std.dump(category)
    return result, HTTPStatus.CREATED


@bp.route("/api/get_single_product", methods=["GET"])
@use_args({"_id": fields.Integer()}, location="query")
def get_single_product(args):
    """getting single product by id from db"""
    with mongo.db.client.start_session() as session:
        data = ProductRepository.get_by_id(args, session)
        if not data:
            return (
                jsonify({"message", f"product{args.get('_id')} not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        # std = product_SC()
        # res = std.dump(data)
        return jsonify(data), HTTPStatus.OK
