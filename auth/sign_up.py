from app.auth import auth_bp

@auth_bp.route("/", methods = ["POST"])
async def sign_up():
    print("Login endpoint hit")

    return "Signup sucess"