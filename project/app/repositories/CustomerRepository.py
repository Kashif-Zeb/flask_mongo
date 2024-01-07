from project.app.db import mongo


class CustomerRepository:
    @staticmethod
    def get_next_sequence_customer():
        customerCounter = mongo.db.customerCounter
        counter = customerCounter.find_one_and_update(
            {"_id": "customerCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def add_customer(session, args):
        mongo.db.customer.insert_one(args)
        res = mongo.db.customer.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def find_one_customer(session, args):
        res = mongo.db.customer.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def get_all_customer():
        res = mongo.db.customer.find()
        return res

    @staticmethod
    def update_customer(args, customer, session):
        mongo.db.customer.find_one_and_update(
            {"_id": args.get("_id")},
            {"$set": args},
            return_document=True,
        )
        res = mongo.db.customer.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def removing_customer(args):
        mongo.db.customer.find_one_and_delete({"_id": args.get("_id")})
