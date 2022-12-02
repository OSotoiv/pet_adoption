from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        return 'this is a pet'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    pet_species = db.Column(db.String(), db.ForeignKey(
        'species.id'), nullable=False)
    photo_url = db.Column(db.String(), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(), nullable=True)
    available = db.Column(db.Boolean(), default=True)


class Species(db.Model):
    __tablename__ = 'species'

    def __repr__(self):
        return 'only species allowed'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)

    pets = db.relationship('Pet', backref='species_type')
