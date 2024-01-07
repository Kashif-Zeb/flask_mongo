from project.app.db import mongo


class CategoryRepository:
    @staticmethod
    def get_next_sequence_category():
        categoryCounter = mongo.db.categoryCounter
        counter = categoryCounter.find_one_and_update(
            {"_id": "categoryCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_category(args):
        mongo.db.category.insert_one(args)
        res = mongo.db.category.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def checkcategory(args):
        res = mongo.db.category.find_one({"_id": args.get("category_id")})
        return res["_id"]
