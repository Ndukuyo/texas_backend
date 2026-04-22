from app.auth import auth_bp

@auth_bp.route("/", methods = ["POST"])
async def login():
    print("Login endpoint hit")

    return "Login sucess"