import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args

from project.app.schemas.SupplierSchema import SupplierSchema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.SupplierBLC import SupplierBLC
from project.app.repositories.SupplierRepository import SupplierRepository

bp = Blueprint("supplier", __name__)


@bp.route("/api/add_supplier", methods=["POST"])
@use_args(SupplierSchema, location="json")
def add_supplier(args):
    """adding the supplier in db"""
    sup = SupplierBLC.adding_supplier(args)
    std = SupplierSchema()
    result = std.dump(sup)
    return result, HTTPStatus.CREATED
