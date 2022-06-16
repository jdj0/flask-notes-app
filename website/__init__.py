from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sneaky secret key"

    from .views import views
    from .auth import auth

    # registering blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app