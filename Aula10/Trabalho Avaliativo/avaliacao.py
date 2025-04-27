from flask import Flask, request, jsonify
from database.bancotrabalho import db
from models.Aluno import Aluno 
from dotenv import load_dotenv #importando a biblioteca dotenv para proteção de dados sensíveis
import os

load_dotenv()

#seguindo os mesmos padrões criados em aula, mas adaptados para a situação da avaliação

avaliacao = Flask(__name__)
avaliacao.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY') #configurando a chave secreta
avaliacao.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') #banco de dados a partir das variáveis do ambiente
avaliacao.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(avaliacao)

@avaliacao.route('/cadastro', methods=['POST'])
def cadastrar_novo_aluno(): 
    data= request.get_json()
   
    #uma vez que os campos de cadastro são obrigatórios, cria-se uma exceção para os requisitos que não foram preenchidos:
    try:
        nome = data['nome']
        email = data['email']
        senha = data['senha']
    except KeyError as e:
        return jsonify({
            "erro": f"Campo obrigatório ausente: {e.args[0]}"
        }), 400  #código bad request
    
    novo_aluno= Aluno (nome=nome, email=email, senha=senha)
    db.session.add(novo_aluno)
    db.session.commit()

    return jsonify({ 
        "mensagem": "Aluno cadastrado com sucesso.",
        "aluno": novo_aluno.to_dict()
    }), 200 #código de sucesso

@avaliacao.route("/listagem", methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    lista_alunos = [aluno.to_dict() for aluno in alunos]
    output = {
        "Alunos_cadastrados": lista_alunos,
        "total_alunos": len(lista_alunos)
    }
    return jsonify(output)

if __name__ =="__main__":
    with avaliacao.app_context():
        db.create_all()


    avaliacao.run(debug=True, host="0.0.0.0")