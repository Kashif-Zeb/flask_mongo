from project.app.db import mongo


class StoreRepository:
    @staticmethod
    def get_next_sequence_store():
        storeCounter = mongo.db.storeCounter
        counter = storeCounter.find_one_and_update(
            {"_id": "storeCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_store(args):
        mongo.db.store.insert_one(args)
        res = mongo.db.store.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def check_store(args):
        res = mongo.db.store.find_one({"_id": args.get("store_id")})
        return res["_id"]
