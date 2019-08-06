import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config')
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'app.sqlite')
        DATABASE=os.path.join('./app/app.sqlite')
    )

    from app.web import db
    db.init_app(app)

    from app.web import auth,server
    app.register_blueprint(auth.bp)
    #app.register_blueprint(blog.bp)
    app.register_blueprint(server.bp)

    app.add_url_rule('/', endpoint='index')
    #app.add_url_rule('/server', endpoint='server')

    return app
