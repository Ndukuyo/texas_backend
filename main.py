from dotenv import load_dotenv
from prisma import Prisma
from flask import jsonify, Blueprint, Flask
import asyncio
from student import student_bp





if __name__ == "__main__":
    
    app = Flask(__name__)

    app.register_blueprint(student_bp, url_prefix = '/student')

    app.run(debug=True)
    
 