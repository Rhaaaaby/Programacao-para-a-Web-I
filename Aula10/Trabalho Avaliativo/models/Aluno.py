from database.bancotrabalho import db

class Aluno(db.Model):
    __tablename__ = 'aluno'

    id_matricula = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            "matricula": self.id_matricula,
            "nome": self.nome,
            "email": self.email
        }