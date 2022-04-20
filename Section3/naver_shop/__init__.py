from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path="/static")

    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app
