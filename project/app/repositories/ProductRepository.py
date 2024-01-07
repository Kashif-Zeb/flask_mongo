from project.app.db import mongo


class ProductRepository:
    @staticmethod
    def get_next_sequence_product():
        productCounter = mongo.db.productCounter
        counter = productCounter.find_one_and_update(
            {"_id": "productCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_product(args):
        mongo.db.product.insert_one(args)
        res = mongo.db.product.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def get_by_id(args, session):
        pipeline = [
            {"$match": {"_id": args.get("_id")}},
            {
                "$lookup": {
                    "from": "supplier",
                    "localField": "supplier_id",
                    "foreignField": "_id",
                    "as": "supplier_info",
                }
            },
            {"$unwind": "$supplier_info"},
            {
                "$lookup": {
                    "from": "category",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category_info",
                }
            },
            {"$unwind": "$category_info"},
        ]

        # Aggregate the data
        result = list(mongo.db.product.aggregate(pipeline, session=session))
        return result
