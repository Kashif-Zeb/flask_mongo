from itertools import count
from project.app.repositories.CategoryRepository import CategoryRepository
from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class CategoryBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_category(args):
        # session = SupplierBLC.get_session()
        new_id = CategoryRepository.get_next_sequence_category()
        args["_id"] = new_id
        res = CategoryRepository.creating_category(args)
        return res
