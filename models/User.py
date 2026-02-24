from datetime import datetime
from extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), nullable=False)  # "MEDICO" o "PACIENTE"

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        # OJO: nunca devolver password_hash
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat()
        }