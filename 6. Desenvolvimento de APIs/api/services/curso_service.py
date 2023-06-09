from ..models.curso_model import Curso
from api import db

def cadastrar_curso(curso):
    curso_bd = Curso(nome=curso.nome, descricao=curso.descricao, data_publicacao=curso.data_publicacao)
    db.session.add(curso_bd)
    db.session.commit()
    return curso_bd

def listar_cursos():
    cursos = Curso.query.all()
    return cursos

def listar_curso_id(id):
    curso = Curso.query.filter_by(id=id).first()
    return curso

def atualiza_curso(curso_anterior, curso_novo):
    curso_anterior.nome = curso_novo.nome
    curso_anterior.descricao = curso_novo.descricao
    curso_anterior.data_publicacao = curso_novo.data_publicacao
    db.session.commit()

def remove_curso(curso):
    db.session.delete(curso)
    db.session.commit()
