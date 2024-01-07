import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args

from project.app.schemas.CustomerSchema import CustomerSchema, update_customer_schema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.CustomerBLC import CustomerBLC
from project.app.repositories.CustomerRepository import CustomerRepository

bp = Blueprint("customer", __name__)


@bp.route("/api/add_customer", methods=["POST"])
@use_args(CustomerSchema, location="json")
def add_customer(args):
    """adding the customer"""
    cust = CustomerBLC.creating_customer(args)
    std = CustomerSchema()
    result = std.dump(cust)
    return result, HTTPStatus.CREATED


@bp.route("/api/get_single_customer", methods=["GET"])
@use_args({"_id": fields.Integer()}, location="query")
def get_single_customer(args):
    """getting a single customer by id"""
    try:
        cust = CustomerBLC.fetching_a_customer(args)

        return cust, HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/api/get_all_customer", methods=["GET"])
def get_all_customer():
    """Getting all customers"""
    cust = CustomerRepository.get_all_customer()
    std = CustomerSchema(many=True)
    result = std.dump(cust)
    return jsonify(result), HTTPStatus.OK


@bp.route("/api/update_customer", methods=["PUT"])
@use_args(update_customer_schema, location="json")
def update_customer(args):
    """Updating an existing user's information"""
    cust = CustomerBLC.Updating_customer(args)
    return cust, HTTPStatus.OK


@bp.route("/api/delete_customer", methods=["DELETE"])
@use_args({"_id": fields.Integer()}, location="query")
def delete_customer(args):
    """Deleting a customer by its ID"""
    res = CustomerBLC.deleting_customer(args)
    return res
