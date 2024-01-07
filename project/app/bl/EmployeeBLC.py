from itertools import count
from project.app.repositories.EmployeeRepository import EmployeeRepository
from project.app.repositories.StoreRepository import StoreRepository
from project.app.repositories.DepartmentRepository import DepartmentRepository
from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class EmployeeBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def adding_employee(args):
        # session = SupplierBLC.get_session()
        new_id = EmployeeRepository.get_next_sequence_employee()
        args["_id"] = new_id
        checkdept = DepartmentRepository.check_dept(args)
        checkstore = StoreRepository.check_store(args)
        if checkstore:
            if checkdept:
                args["department_id"] = checkdept
                args["store_id"] = checkstore
                res = EmployeeRepository.creating_employee(args)
                return res
            else:
                raise Exception("department id not found")
        else:
            raise Exception("store id not found")

    @staticmethod
    def getting_detailsEDS(args):
        try:
            with mongo.db.client.start_session() as session:
                employees = EmployeeRepository.get_by_ID_ESD(args, session)
                if not employees:
                    raise Exception("Employee ID not found")

                for employee in employees:
                    employee.pop("store_id")
                    employee.pop("department_id")

                return employees
        except Exception as e:
            raise e
