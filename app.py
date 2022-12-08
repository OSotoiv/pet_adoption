from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, Species
from form import PetForm, AddSpeciesForm
from form_helpers import addPet, addSpecies, update_pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'thehouseisyellow'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def home():
    heading = 'All Pets'
    pets = db.session.query(Pet.name, Pet.photo_url,
                            Pet.available, Pet.id).all()
    return render_template('show_pets.html', pets=pets, heading=heading)


@app.route('/add', methods=['GET', 'POST'])
def new_pet():
    form = PetForm()
    # species = db.session.query(Species.id, Species.name)
    form.pet_species.choices = [(s.id, s.name) for s in Species.query.all()]
    if form.validate_on_submit():
        new_pet = addPet(form)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_form.html', form=form)


@app.route('/add_species', methods=['GET', 'POST'])
def new_species():
    form = AddSpeciesForm()
    if form.validate_on_submit():
        new_species = addSpecies(form)
        db.session.add(new_species)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_species_form.html', form=form)


@app.route('/available_pets')
def available_pets():
    heading = 'All Available Pets'
    pets = db.session.query(Pet.name, Pet.photo_url,
                            Pet.available, Pet.id).filter(Pet.available == True)
    return render_template('show_pets.html', pets=pets, heading=heading)


@app.route('/unavailable_pets')
def unavailable_pets():
    heading = 'All Unavailable Pets'
    pets = db.session.query(Pet.name, Pet.photo_url,
                            Pet.available, Pet.id).filter(Pet.available == False)
    return render_template('show_pets.html', pets=pets, heading=heading)


@app.route('/pet_info/<int:pet_id>', methods=['GET', 'POST'])
def pet_info(pet_id):
    pet = Pet.query.get(pet_id)
    form = PetForm(obj=pet)
    form.pet_species.choices = [(s.id, s.name) for s in Species.query.all()]
    if form.validate_on_submit():
        updated_pet = update_pet(form, pet)
        db.session.add(updated_pet)
        db.session.commit()
        return redirect(f'/pet_info/{pet_id}')
    else:
        return render_template('pet_info.html', pet=pet, form=form)
