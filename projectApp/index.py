from app import app
from utils.db import db
from sqlalchemy_utils import create_database, database_exists


with app.app_context():
	if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
		create_database(app.config['SQLALCHEMY_DATABASE_URI'])
	db.create_all()


if __name__ == '__main__':
    app.run(debug=True)


