from flask import jsonify, Blueprint

#Define the blueprint
student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/single", methods = ["GET"])
async def single_student():
    return "single_student"

    # Prisma = Prisma()
    # try:
    #     await Prisma.connect()

    #     student = await Prisma.student.find_first()

       
    #     return jsonify(student.model_dump())
    # finally:
    #     prisma.disconnect()

@student_bp.route("/add", methods= ["POST"])
async def add():
    return "Adding student"

@student_bp.route("/delete", methods= ["DELETE"])
async def delete_student():
    return "deleteing a student"

@student_bp.route("/list-all", methods= ["GET"])
async def list_all():
    return "list student"