from project.app.db import mongo


class SupplierRepository:
    @staticmethod
    def get_next_sequence_supplier():
        supplierCounter = mongo.db.supplierCounter
        counter = supplierCounter.find_one_and_update(
            {"_id": "supplierCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_supplier(args):
        mongo.db.supplier.insert_one(args)
        res = mongo.db.supplier.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def checksupplier(args):
        res = mongo.db.supplier.find_one({"_id": args.get("category_id")})
        return res["_id"]
