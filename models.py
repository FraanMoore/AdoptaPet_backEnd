from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def serialize(self):
        return {
            "id" : self.id,  
            "name" : self.name, 
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol_id = db.Column(db.Integer, nullable=False)
    favorites = db.relationship("Favorites")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "rol_id": self.rol_id
        }
        
class User_description(db.Model):
    __tablename__ = 'user description'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    motivation = db.Column(db.String(500), nullable=False)
    style = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "motivation" : self.motivation,
            "style" : self.style,
            "user_id" :  self.user_id
        }
    
class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    pet_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image = db.Column(db.LargeBinary, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pet_id" : self.pet_id
        }
        
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)
    medical_history = db.Column(db.String(500), nullable=False)
    is_adopted = db.Column(db.Boolean, unique=False, default=False)
    adress_id = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    
    def serialize(self):
        return {
            "id" : self.id,  
            "name" : self.name, 
            "gender" : self.gender, 
            "age"  : self.age,
            "description" : self.description,
            "species" : self.species,
            "size" : self.size,
            "medical_history" : self.medical_history,
            "is_adopted" : self.is_adopted,
            "adress_id" :  self.adress_id,
            "user_id" : self.user_id
        }

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)
    description = db.Column(db.String(500), nullable=False)

def serialize(self):
        return {
            "id" : self.id,  
            "title" : self.title,
            "description": self.description
            
        }
    
class Adress(db.Model):
    __tablename__ = 'adress'
    id = db.Column(db.Integer, primary_key=True)
    commune = db.Column(db.String(50), nullable=False)

def serialize(self):
        return {
            "id" : self.id,  
            "title" : self.title,
            "description": self.description
            
        }