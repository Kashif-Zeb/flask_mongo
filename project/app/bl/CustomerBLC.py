from itertools import count
from project.app.repositories.CustomerRepository import CustomerRepository
from http import HTTPStatus
from project.app.db import mongo
from flask import request, jsonify


class CustomerBLC:
    @staticmethod
    def get_session():
        with mongo.db.client.start_session() as session:
            return session

    @staticmethod
    def creating_customer(args):
        session = CustomerBLC.get_session()
        new_id = CustomerRepository.get_next_sequence_customer()
        args["_id"] = new_id
        res = CustomerRepository.add_customer(session, args)
        return res

    @staticmethod
    def fetching_a_customer(args):
        session = CustomerBLC.get_session()
        customer = CustomerRepository.find_one_customer(session, args)
        if customer is None:
            raise Exception("customer not found")
        return customer

    @staticmethod
    def Updating_customer(args):
        session = CustomerBLC.get_session()
        customer = CustomerRepository.find_one_customer(session, args)
        if customer:
            updated = CustomerRepository.update_customer(args, customer, session)
            return updated
        else:
            raise Exception("customer not found")

    @staticmethod
    def deleting_customer(args):
        session = CustomerBLC.get_session()
        customer = CustomerRepository.removing_customer(args)
        if customer is not None:  # Check if deletion operation returns a value
            return (
                jsonify({"message": f"Customer {args.get('_id')} has been deleted"}),
                HTTPStatus.OK,
            )
        else:
            # Assuming deletion succeeds even when the function returns None

            return (
                jsonify(
                    {
                        "message": f"Customer {args.get('_id')} has been deleted or not existed"
                    }
                ),
                HTTPStatus.OK,
            )
