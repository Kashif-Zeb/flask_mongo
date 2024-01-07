from project.app.db import mongo


class EmployeeRepository:
    @staticmethod
    def get_next_sequence_employee():
        employeeCounter = mongo.db.employeeCounter
        counter = employeeCounter.find_one_and_update(
            {"_id": "employeeCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_employee(args):
        mongo.db.employee.insert_one(args)
        res = mongo.db.employee.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def get_by_ID_ESD(args, session):
        pipline = [
            {"$match": {"_id": args["_id"]}},
            {
                "$lookup": {
                    "from": "store",
                    "localField": "store_id",
                    "foreignField": "_id",
                    "as": "store",
                }
            },
            {"$unwind": "$store"},
            {
                "$lookup": {
                    "from": "department",
                    "localField": "department_id",
                    "foreignField": "_id",
                    "as": "department",
                }
            },
            {"$unwind": "$department"},
        ]
        res = list(mongo.db.employee.aggregate(pipeline=pipline, session=session))
        return res
