from project.app.db import mongo


class DepartmentRepository:
    @staticmethod
    def get_next_sequence_department():
        departmentCounter = mongo.db.departmentCounter
        counter = departmentCounter.find_one_and_update(
            {"_id": "departmentCounter_id"},
            {"$inc": {"sequence_value": 1}},
            return_document=True,
            upsert=True,  # Add this parameter to insert a new document if it doesn't exist
        )
        return counter["sequence_value"] if counter else 1

    @staticmethod
    def creating_department(args):
        mongo.db.department.insert_one(args)
        res = mongo.db.department.find_one({"_id": args.get("_id")})
        return res

    @staticmethod
    def check_dept(args):
        res = mongo.db.department.find_one({"_id": args.get("department_id")})
        return res["_id"]
