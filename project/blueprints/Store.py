import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args
from project.app.db import mongo
from project.app.schemas.StoreSchema import StoreSchema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.StoreBLC import StoreBLC
from project.app.repositories.StoreRepository import StoreRepository

bp = Blueprint("store", __name__)


@bp.route("/api/add_store", methods=["POST"])
@use_args(StoreSchema, location="json")
def add_supplier(args):
    """adding the store in db"""
    store = StoreBLC.adding_store(args)
    # std = DepartmentSchema()
    # result = std.dump(category)
    return store, HTTPStatus.CREATED
