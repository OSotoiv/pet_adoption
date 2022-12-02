from models import Pet, Species


def addPet(form):
    adoptable = True if form.available.data == 'True' else False
    new_pet = Pet(
        name=form.name.data,
        pet_species=form.pet_species.data,
        photo_url=form.photo_url.data,
        age=form.age.data,
        notes=form.notes.data,
        available=adoptable
    )
    return new_pet


def addSpecies(form):
    new_species = Species(id=form.species_id.data, name=form.species_name.data)
    return new_species


def update_pet(form, pet):
    adoptable = True if form.available.data == 'True' else False
    pet.name = form.name.data,
    pet.pet_species = form.pet_species.data,
    pet.photo_url = form.photo_url.data,
    pet.age = form.age.data,
    pet.notes = form.notes.data,
    pet.available = adoptable
    return pet
