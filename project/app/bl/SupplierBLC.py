from itertools import count
from project.app.repositories.SupplierRepository import SupplierRepository
from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class SupplierBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_supplier(args):
        # session = SupplierBLC.get_session()
        new_id = SupplierRepository.get_next_sequence_supplier()
        args["_id"] = new_id
        res = SupplierRepository.creating_supplier(args)
        return res
