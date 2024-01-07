from itertools import count
from project.app.repositories.ProductRepository import ProductRepository
from project.app.repositories.CategoryRepository import CategoryRepository
from project.app.repositories.SupplierRepository import SupplierRepository
from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class ProductBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_product(args):
        # session = SupplierBLC.get_session()
        new_id = ProductRepository.get_next_sequence_product()
        args["_id"] = new_id
        checkcategory = CategoryRepository.checkcategory(args)
        checksupplier = SupplierRepository.checksupplier(args)
        if checkcategory is not None:
            if checksupplier is not None:
                args["supplier_id"] = checksupplier
                args["category_id"] = checkcategory
                res = ProductRepository.creating_product(args)
                return res
            else:
                raise Exception("supplier not found")
        else:
            raise Exception("category not found")
