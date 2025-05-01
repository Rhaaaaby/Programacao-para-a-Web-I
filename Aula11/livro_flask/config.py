import os 
import random, string

class Config(object):
    CSRF_ENABLED = True
    SECRET = 'ce22c680-eb91-4f50-aaa1-b648471837a6'
    TEMPLATE_FOLDER = os.path.join(os.pathdirname(os.path.abspath(__file__)), 'templates')
    APP = None
    SQALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:admin@localhost:3306/livro_flask'


    class DevelopmentConfig(Config):
        TESTING = True
        DEBUG = True
        IP_HOST = 'localhost'
        PORT_HOST = 8000
        URL_MAIN = 'http://%s:%s/' (IP_HOST, PORT_HOST)

    class TestingConfig(Config):
        TESTING = True 
        DEBUG = True
        IP_HOST = 'localhost' #aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina
        PORT_HOST = 5000
        URL_MAIN = 'http://%s:%s/'

    class ProductionConfig(Config):
        DEBUG = False
        TESTING = False
        IP_HOST = 'localhost' #aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina
        PORT_HOST = 8080
        URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

    app_config = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig()
    }

    app_active = os.getenv('FLASK_ENV')
