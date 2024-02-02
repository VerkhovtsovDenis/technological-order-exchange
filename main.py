from create_app import app
from databases_model import *
from routers import urls_blueprint


app.register_blueprint(urls_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
