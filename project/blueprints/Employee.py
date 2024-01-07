import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args
from project.app.db import mongo
from project.app.schemas.EmployeeSchema import EmployeeSchema, employee_ESD_schema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.EmployeeBLC import EmployeeBLC
from project.app.repositories.EmployeeRepository import EmployeeRepository

bp = Blueprint("employee", __name__)


@bp.route("/api/add_employee", methods=["POST"])
@use_args(EmployeeSchema, location="json")
def add_supplier(args):
    """adding the store in db"""
    store = EmployeeBLC.adding_employee(args)
    # std = DepartmentSchema()
    # result = std.dump(category)
    return store, HTTPStatus.CREATED


@bp.route("/api/get_employee_SD", methods=["GET"])
@use_args({"_id": fields.Integer()}, location="query")
def get_employee_SD(args):
    try:
        employee = EmployeeBLC.getting_detailsEDS(args)

        return jsonify(employee), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/api/get_employee_SD_BY_schema", methods=["GET"])
@use_args({"_id": fields.Integer()}, location="query")
def get_employee_SD_BY_schema(args):
    with mongo.db.client.start_session() as session:
        employees = EmployeeRepository.get_by_ID_ESD(args, session)
        if not employees:
            raise Exception("Employee ID not found")
        schema = employee_ESD_schema(many=True)
        res = schema.dump(employees)
        return jsonify(res)
