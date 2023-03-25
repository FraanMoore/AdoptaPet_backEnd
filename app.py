from flask import Flask, request, jsonify
from models import db , Rol, User, User_description, Pet, Favorites, Post

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
    rol = Rol.query.get(id)
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
def create_user():
    # Obtiene los datos del usuario de la solicitud
    name = request.json.get("name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")
    phone = request.json.get("phone")
    rol_id = request.json.get("rol_id")
    password = request.json.get("password")

    # Verifica si el correo ya existe en la base de datos
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return "El correo ya existe en la base de datos", 400

    # Crea un nuevo objeto User
    new_user = User(name=name, last_name=last_name, email=email, phone=phone, rol_id=rol_id, password=password)

    # Agrega el usuario a la sesión de la base de datos
    db.session.add(new_user)
    db.session.commit()

    # Devuelve una respuesta con código de estado HTTP 201
    return "Usuario guardado", 201

# GET

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

#PUT & DELETE

@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            user.name = request.json.get("name")
            user.last_name = request.json.get("last_name")
            user.password = request.json.get("password")
            user.email = request.json.get("email")
        
            db.session.commit()
        
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 404

#USER_DESCRIPTION

#POST

@app.route("/users/<int:user_id>/description", methods=["POST"])
def create_description(user_id):
    user_description = User_description()
    user_description.description = request.json.get("description")
    user_description.motivation = request.json.get("motivation")
    user_description.style = request.json.get("style")
    user_description.user_id = request.json.get("user_id")
    
    db.session.add(user_description)
    db.session.commit()
    
    return "Descrcripción guardada", 201

#GET

@app.route("/descriptions/list", methods=["GET"])
def get_description():
    user_descriptions = User_description.query.all()
    result = []
    for user_description in user_descriptions:
        result.append(user_description.serialize())
    return jsonify(result)

# GET user with description

@app.route("/users/description/list/<int:id>", methods=["GET"])
def get_user_with_description(id):
    user = User.query.filter_by(id=id).first()  # Obtener el usuario por su id
    if user is not None:
        user_description = User_description.query.filter_by(user_id=id).first()  # Obtener la descripción del usuario por su id
        if user_description is not None:
            # Crear un diccionario con los datos del usuario y su descripción
            result = {
                "user_id": user.id,
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "rol_id": user.rol_id,
                "description": user_description.description,
                "motivation": user_description.motivation,
                "style": user_description.style
            }
            return jsonify(result), 200
        else:
            return jsonify("Descripción del usuario no encontrada"), 404
    else:
        return jsonify("Usuario no encontrado"), 404

#PUT & DELETE

@app.route("/description/<int:id>", methods=["PUT", "DELETE"])
def update_description(id):
    user_description =  User_description.query.get(id)
    if user_description is not None:
        if request.method == "DELETE":
            db.session.delete(user_description)
            db.session.commit()
            
            return "Description eliminada", 204
        else:    
            user_description.description = request.json.get("description")
            user_description.motivation = request.json.get("motivation")
            user_description.style = request.json.get("style")
            user_description.user_id = request.json.get("user_id")
        
            db.session.commit()
        
            return jsonify("Descripción actualizada"), 200
    
    return jsonify("Descripción no encontrada"), 404
    
#PET

#POST

@app.route("/pets", methods=["POST"])
def create_pet():
    pet = Pet()
    pet.name = request.json.get("name")
    pet.gender = request.json.get("gender")
    pet.age = request.json.get("age")
    pet.description = request.json.get("description")
    pet.species = request.json.get("species")
    pet.size = request.json.get("size")
    pet.medical_history = request.json.get("medical_history")
    pet.is_adopted = request.json.get("is_adopted")
    pet.adress_id = request.json.get("adress_id")
    pet.rol_id = request.json.get("rol_id")
    
    db.session.add(pet)
    db.session.commit()
    
    return "Mascota guardada", 201

#GET

@app.route("/pets/list", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    result = []
    for pet in pets:
        result.append(pet.serialize())
    return jsonify(result)

#PUT & DELETE

@app.route("/pet/<int:id>", methods=["PUT", "DELETE"])
def update_pet(id):
    pet =  Pet.query.get(id)
    if pet is not None:
        if request.method == "DELETE":
            db.session.delete(pet)
            db.session.commit()
            
            return "Mascota eliminada", 204
        else:    
            pet.name = request.json.get("name")
            pet.gender = request.json.get("gender")
            pet.age = request.json.get("age")
            pet.description = request.json.get("description")
            pet.species = request.json.get("species")
            pet.size = request.json.get("size")
            pet.medical_history = request.json.get("medical_history")
            pet.is_adopted = request.json.get("is_adopted")
            pet.adress_id = request.json.get("adress_id")
            pet.rol_id = request.json.get("rol_id")
        
            db.session.commit()
        
            return jsonify("Mascota actualizada"), 200
    
    return jsonify("Mascota no encontrada"), 404

#FAVORITES

#POST

@app.route("/favorites", methods=["POST"])
def create_favorite():
    favorites = Favorites()
    favorites.pet_id = request.json.get("pet_id")
    favorites.user_id = request.json.get("user_id")
    
    db.session.add(favorites)
    db.session.commit()

    return "Favorito guardado", 201

#GET

@app.route("/favorites/list", methods=["GET"])
def get_favorites():
    favorites = Favorites.query.all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)

# GET favorite/user

@app.route("/favorites/user/<int:user_id>", methods=["GET"])
def get_favorite_user(user_id):
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)

#PUT & DELETE

@app.route("/favorites/<int:id>", methods=["PUT", "DELETE"])
def update_favorites(id):
    favorite =  Favorites.query.get(id)
    if favorite is not None:
        if request.method == "DELETE":
            db.session.delete(favorite)
            db.session.commit()
            
            return "Mascota eliminada", 204
        else:    
            favorite.pet_id = request.json.get("pet_id")
            favorite.user_id = request.json.get("user_id")
            
        
            db.session.commit()
        
            return jsonify("Favoritos actualizados"), 200
    
    return jsonify("Favoritos no encontrados"), 404

#POST

#POST

@app.route("/posts", methods=["POST"])
def create_post():
    posts = Post()
    posts.title = request.json.get("title")
    posts.description = request.json.get("description")
    posts.rol_id = request.json.get("rol_id")
    
    db.session.add(posts)
    db.session.commit()

    return "Publicación guardada", 201
    
#GET

@app.route("/posts/list", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    result = []
    for post in posts:
        result.append(post.serialize())
    return jsonify(result)










































with app.app_context():
    db.create_all()
    
    


app.run(host="localhost", port="8080")