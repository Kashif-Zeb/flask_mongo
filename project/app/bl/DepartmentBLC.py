from itertools import count
from project.app.repositories.DepartmentRepository import DepartmentRepository

from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class DepartmentBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_department(args):
        # session = SupplierBLC.get_session()
        new_id = DepartmentRepository.get_next_sequence_department()
        args["_id"] = new_id

        res = DepartmentRepository.creating_department(args)
        return res
