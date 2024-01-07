import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args
from project.app.db import mongo
from project.app.schemas.DepartmentSchema import DepartmentSchema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.DepartmentBLC import DepartmentBLC
from project.app.repositories.DepartmentRepository import DepartmentRepository

bp = Blueprint("department", __name__)


@bp.route("/api/add_department", methods=["POST"])
@use_args(DepartmentSchema, location="json")
def add_supplier(args):
    """adding the product in db"""
    dept = DepartmentBLC.adding_department(args)
    # std = DepartmentSchema()
    # result = std.dump(category)
    return dept, HTTPStatus.CREATED
