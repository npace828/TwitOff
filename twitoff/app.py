from flask import Flask

def create_app():
    """create and configure and instance of the Flask Application """
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello Twitoff!'
    return app
