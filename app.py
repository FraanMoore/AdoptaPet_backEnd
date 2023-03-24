from flask import Flask, request, jsonify
from models import db , Rol, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)   

@app.route("/")
def home():
    return "Hello world"

#ROL
#POST

@app.route("/rols", methods=["POST"])
def create_rol():
    rol = Rol()
    rol.name = request.json.get("name")
    
    db.session.add(rol)
    db.session.commit()
    
    return "Usuario guardado", 201
    
#GET

@app.route("/rols/list", methods=["GET"])
def get_rols():
    rols = Rol.query.all()
    result = []
    for rol in rols:
        result.append(rol.serialize())
    return jsonify(result)


#PUT & DELETE

@app.route("/rols/<int:id>", methods=["PUT", "DELETE"])
def update_rol(id):
    rol = rol = Rol.query.get(id)
    if rol is not None:
        if request.method == "DELETE":
            db.session.delete(rol)
            db.session.commit()
            
            return "Usuario eliminado", 204
        else:    
            rol.name = request.json.get("name")
        
            db.session.commit()
        
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 404


#USER
#POST

@app.route("/users", methods=["POST"])
def create_user() :
    user = User()
    user.name = request.json.get("name")
    user.last_name = request.json.get("last_name")
    user.email = request.json.get("email")
    user.phone = request.json.get("phone")
    user.rol_id = request.json.get("rol_id")
    user.password = request.json.get("password")
    
    db.session.add(user)
    db.session.commit()
    
    return "User guardado", 201


with app.app_context():
    db.create_all()

app.run(host="localhost", port="8080")