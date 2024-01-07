from itertools import count
from project.app.repositories.StoreRepository import StoreRepository

from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class StoreBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_store(args):
        # session = SupplierBLC.get_session()
        new_id = StoreRepository.get_next_sequence_store()
        args["_id"] = new_id

        res = StoreRepository.creating_store(args)
        return res
