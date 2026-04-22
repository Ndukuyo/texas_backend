from flask import jsonify,Blueprint,request
from app.bcrypt import bcrypt
from app.prisma import with_prisma


auth_bp=Blueprint("auth_bp",__name__)

#JWT -> 
#
@auth_bp.route("/login",methods=["POST"])
def login():
    return "login success"

@auth_bp.route("/sign-up",methods=["POST"])
@with_prisma
async def sign_up(prisma):

    # prisma=Prisma()

    # await prisma.connect()

    data=request.get_json()

    print("Request body ",data)

    name=data.get("name")
    email=data.get("email")
    password=data.get("password")

    if not name:
        return jsonify({"custom":True,"_message":"Name required"}),400
    
    if not email:
        return jsonify({"custom":True,"_message":"Email required"})

    if not password:
       return jsonify({"custom":True,"_message":"Password required"}),400
    
    #strong  atlest 4 characters
    # atlest a number
    if len(password)<3:
        return jsonify({"custom":True,"_message":"Password must have atleast 4 charcters"})
    #regex expession: check strong password
    # check if password has a number
    #Check if it has one capital letter

    hashed_passwod=bcrypt.generate_password_hash(password).decode("utf-8")

    #Everything is ok.
    print("User email is",email)
    print("User password is",password)
    print("User name is",name)
    print("Password hash",hashed_passwod)
    #Regex->reqular expressions
    #Regex check for email

    #check if email is aleredy in use
    player_exists=await prisma.player.find_unique(
        where={
            "email":email
        }
    )

    if player_exists:
        return jsonify({"custom":True,"_message":"Email already in use." })
    

    #money 5000 A to person B
    # A-> subtract 5000
    # B-> Add 5000 acount

    transaction=None

    async with prisma.tx() as tx:
    
        #Transaction -> db entries 
        new_player=await tx.player.create(
            data={
                "name":name,
                "email":email
            }
        )
        #print("value of k",k)
        # light go off->
        new_player_pass=await tx.player_password.create(data={
                "player_id":new_player.id,
                "password":hashed_passwod
            })
        
        transaction=new_player
        

    return jsonify(transaction.model_dump())