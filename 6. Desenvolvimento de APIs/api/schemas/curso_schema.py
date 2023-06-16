from api import ma
from ..models.curso_model import Curso
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Curso
        load_instance = True
        fields = ('id', 'nome', 'descricao', 'data_publicacao')

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_publicacao = fields.Date(required=True)