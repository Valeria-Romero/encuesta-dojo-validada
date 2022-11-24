
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s)"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, formulario)
        return result

    @classmethod
    def last(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        return result

    @staticmethod
    def validate_dojo(formulario):
        is_valid = True # asumimos que esto es true

        if len(formulario['nombre']) < 3:
            flash("Name must be at least 3 characters", 'formulario')
            is_valid = False

        if len(formulario['ubicacion']) < 3:
            flash("Location must be at least 3 characters", 'formulario')
            is_valid = False

        if len(formulario['idioma']) < 3:
            flash("Calories must be 3 or greater", 'formulario')
            is_valid = False

        if len(formulario['comentario']) < 3:
            flash("Comentaio must be at least 3 characters", 'formulario')
            is_valid = False

        return is_valid

    