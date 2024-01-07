import json
import os
from flask import request, jsonify, send_file
from webargs.flaskparser import use_args

from project.app.schemas.CategorySchema import CategorySchema
from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.CategoryBLC import CategoryBLC
from project.app.repositories.CategoryRepository import CategoryRepository

bp = Blueprint("category", __name__)


@bp.route("/api/add_category", methods=["POST"])
@use_args(CategorySchema, location="json")
def add_supplier(args):
    """adding the supplier in db"""
    category = CategoryBLC.adding_category(args)
    std = CategorySchema()
    result = std.dump(category)
    return result, HTTPStatus.CREATED
