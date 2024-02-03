from create_app import app, db
from scripts import urls_blueprint


app.register_blueprint(urls_blueprint)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
