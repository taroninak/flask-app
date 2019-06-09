from app.controllers import init_app as controllers

def create_app(app):
    """Configure an instance of the Flask application."""
    init_app(app)

def init_app(app):
    controllers(app)

    @app.route('/')
    def index():
        return "Hello World!"
 