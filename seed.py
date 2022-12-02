from models import db, Pet, Species
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

spec1 = Species(id='dog', name='Dog')
spec2 = Species(id='cat', name='Cat')
spec3 = Species(id='porcupine', name='Porcupine')


dog = Pet(name='Rocky', pet_species=spec1.id, age=4, notes='loves kids',
          photo_url='https://images.unsplash.com/photo-1593134257782-e89567b7718a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80')
cat = Pet(name='Tabitha', pet_species=spec2.id, age=7, notes='crazy cat',
          photo_url='https://images.unsplash.com/photo-1519052537078-e6302a4968d4?ixlib=rb-4.0.3&ixname=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80')
porcupine = Pet(name='Pickels', pet_species=spec3.id, age=2, notes='pokey little guy',
                photo_url='https://images.unsplash.com/photo-1605369179590-014a88d4560a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1185&q=80')

with app.app_context():
    db.session.add_all([spec1, spec2, spec3])
    db.session.commit()
    db.session.add_all([dog, cat, porcupine])
    db.session.commit()
