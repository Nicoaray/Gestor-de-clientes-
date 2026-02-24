from datetime import datetime
from extensions import db

class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)

    motivo = db.Column(db.String(255), nullable=False)
    diagnostico = db.Column(db.Text, nullable=True)
    observaciones = db.Column(db.Text, nullable=True)

    paciente_id = db.Column(db.Integer, nullable=False)
    medico_id = db.Column(db.Integer, nullable=False)

    estado = db.Column(db.String(20), nullable=False, default="PROGRAMADA")

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)