from flask import Flask

# Create a Flask instance
def create_app():
    app = Flask(__name__)
    # Import main blueprint from main.py
    # The . in .main means the file is on the same level as the current file
    from .main import main as main_bp
    # Allows us to run the code
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app

