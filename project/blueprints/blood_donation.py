# import json
# import os
# from flask import request, jsonify, send_file
# from webargs.flaskparser import use_args
# from project.app.schemas.BloodDonationSchema import (
#     BloodDonationDumpSchema_all,
#     BloodDonationSchema,
#     schema_for_update_BD,
#     schema_to_get_BD_donor,
# )
# from project.app.repositories.BloodDonationRepository import BloodDonationRepository
# from flask import Blueprint
# from http import HTTPStatus
# from marshmallow import fields, Schema, validate
# from project.app.bl.BloodDonationBLC import BloodDonationBLC

# from confluent_kafka import ConsumerGroupState, Producer
# from confluent_kafka import Consumer


# producer = Producer({"bootstrap.servers": "localhost:9092"})
# bp = Blueprint("blood_donation", __name__)


# @bp.route("/api/add_blooddonation", methods=["POST"])
# @use_args(BloodDonationSchema, location="json")
# def add_blooddonation(args):
#     """adding the blooddonation and associating with donor"""
#     args["DonationStatus"] = "Pending"
#     blood_D = BloodDonationBLC.creating_blooddonation(args)
#     if not blood_D:
#         return (
#             jsonify({"message": "plz provide your information using add donor api"}),
#             HTTPStatus.OK,
#         )
#     std = BloodDonationSchema()
#     result = std.dump(blood_D)
#     return result, HTTPStatus.CREATED


# @bp.route("/api/get_single_blooddonation", methods=["GET"])
# @use_args({"DonationID": fields.Integer()}, location="query")
# def get_single_bloodbank(args):
#     """getting blooddonation by id"""
#     # breakpoint()
#     res = BloodDonationBLC.getting_blooddonation(args)
#     if not res:
#         return jsonify({"message": "No data found"}), HTTPStatus.NOT_FOUND
#     std = schema_to_get_BD_donor(many=False)
#     # breakpoint()
#     result = std.dump(res)
#     return result, HTTPStatus.OK


# @bp.route("/api/blooddonations", methods=["GET"])
# def get_all_blooddonations():
#     """getting all blooddonations"""
#     # breakpoint()
#     res = BloodDonationBLC.getting_all_blooddonations()
#     if not res:
#         return jsonify({"message": "records not found"}), HTTPStatus.NOT_FOUND
#     std = schema_to_get_BD_donor(many=True)
#     result = std.dump(res)
#     return result, HTTPStatus.OK


# @bp.route("/api/update_blooddonation", methods=["PUT"])
# @use_args(schema_for_update_BD, location="json")
# def updating_blooddonation(args):
#     """updating the blooddonation"""
#     args["DonationStatus"] = "Pending"
#     res = BloodDonationBLC.updating_blooddonation(args)
#     if not res:
#         return jsonify({"message": "No data found"}), HTTPStatus.OK
#     std = schema_for_update_BD()
#     result = std.dump(res)
#     return result, HTTPStatus.OK


# @bp.route("/api/update_donationstatus", methods=["PUT"])
# @use_args(
#     {
#         "DonationID": fields.List(fields.Integer(), required=True),
#         "DonationStatus": fields.String(
#             validate=validate.OneOf(["Approved", "Rejected"]), required=True
#         ),
#         "BloodBankID": fields.Integer(),
#     },
#     location="json",
# )
# def update_donationstatus(args):
#     """updating the blooddonation status"""
#     if not len(args.get("DonationID")):
#         return (
#             jsonify({"DonationID": "Enter ths IDs "}),
#             HTTPStatus.UNPROCESSABLE_ENTITY,
#         )
#     res = BloodDonationBLC.updating_donationstatus(args)
#     report = BloodDonationBLC.getting_blooddonation(args)
#     std = BloodDonationDumpSchema_all()
#     # breakpoint()
#     report_data = std.dump(report)

#     # Convert report_data to string
#     report_data_str = json.dumps(report_data)

#     # Producer sends both report data as bytes and as a string
#     report_data_bytes = report_data_str.encode("utf-8")

#     producer.produce("blood_report_topic", value=report_data_bytes)
#     producer.flush()

#     # Consumer code (reads data from Kafka topic)
#     consumer = Consumer(
#         {
#             "bootstrap.servers": "localhost:9092",
#             "group.id": "blood-report-group",
#             "auto.offset.reset": "earliest",
#         }
#     )
#     consumer.subscribe(["blood_report_topic"])

#     while True:
#         msg = consumer.poll(1.0)

#         if msg is None:
#             continue
#         if msg.error():
#             print(f"Consumer error: {msg.error()}")
#             continue

#         data = msg.value()  # No need to decode assuming data is already bytes
#         report_content = data.decode("utf-8")
#         # recieved = str(report_content)
#         save_path = f"C:\\Users\\Kashf\\Desktop\\git\\New folder (2)\\BDS\\uploads\\blood_report{report.DonationID}.txt"

<<<<<<< Updated upstream
        # Save the report to the specified path
        with open(save_path, "w") as file:
            json.dump(report_content, file, indent=4)
        BloodDonationBLC.savefile(save_path, report)
        return res
=======
#         # Save the report to the specified path
#         with open(save_path, "w") as file:
#             json.dump(report_data, file, indent=4)
#         BloodDonationBLC.savefile(save_path, report)
#         return res
>>>>>>> Stashed changes


# @bp.route("/api/search_status", methods=["GET"])
# @use_args({"DonationStatus": fields.String()}, location="query")
# def search_status(args):
#     """get all blooddoantion by status"""
#     BD = BloodDonationBLC.get_search_status(args)
#     if not BD:
#         return (
#             jsonify({"message": "records not found"}),
#             HTTPStatus.UNPROCESSABLE_ENTITY,
#         )
#     std = BloodDonationSchema(many=True)
#     result = std.dump(BD)
#     return result, HTTPStatus.OK


# @bp.route("/api/download_report", methods=["GET"])
# @use_args({"DonationID": fields.Integer()}, location="query")
# def download_report(args):
#     check = BloodDonationRepository.get_file_by_Did(args)
#     # check = check.__str__()
#     try:
#         return send_file(
#             check,
#             as_attachment=True,
#             download_name=f"blood_report{args.get('DonationID')}.txt",
#         )
#     except Exception as e:
#         print(f"Error while sending file: {e}")
#         return "Error while sending file", 500
